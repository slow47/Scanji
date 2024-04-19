#!/usr/bin/env python3
import argparse
import subprocess
import sys
import ipaddress
from time import sleep

def validate_ip_address(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        print("Validating IP address:", ip_address)  # Always show IP validation
        return True
    except ValueError:
        return False

def run_nmap_scan(ip_address, verbose):
    command = ["sudo", "nmap", "--open", "-sS", "--min-rate=1000", "--max-retries=2", "-p-", ip_address]
    print("Running initial Nmap scan on IP:", ip_address)  # Always show initial scan action
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if verbose and result.stderr:
        print("Nmap scan errors:", result.stderr)
    return result.stdout

def extract_ports(nmap_output,verbose):
    lines = nmap_output.strip().split('\n')
    ports = []
    print("Extracting open TCP ports from scan results...")  # Always show port extraction process
    for line in lines:
        if '/tcp' in line and 'open' in line:
            port = line.split('/')[0].strip()
            ports.append(port)
    if verbose:
        if len(ports)>0: print("Open ports from 1st scan:", ', '.join(ports))
    return ports

def create_nmap_command(ports, ip_address,verbose):
    ports_string = ','.join(ports)
    command = ["nmap", "-p" + ports_string, "-A", "-sV", ip_address]    
    if verbose :
        print("Generated detailed Nmap command for further analysis.", command)
    return command

def execute_nmap_command(command, verbose):
    if verbose :
        print("Executing Nmap command...")  
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Nmap Command Output:")  
    print(result.stdout)
    if verbose and result.stderr:
        print("Errors from detailed Nmap command:", result.stderr)

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Data saved to {filename}")  

def main():
    print()
    print("""
%%%%%%%%%*+%+=##%%%%#=@=+#+==**%#*%%@*+*:+=++====*%####=#%*-+=+%==#%%%%%%%%%%%%%
%%%%%%%%%=#*+=*#*%%%=*#**=+#+**%*%%%#=*-==*+++**#=#%##%+=%%-+==#==*%%%%%%%%%%%%%
%%%%%%%%*+**++**#%%*-*+*++%*++#*#%%%++-#+#=*%*+**+######=*%=++-*=*+%%%%%%%%%%%%%
%%%%%%%%=++*+**+%%%=-**%+*%+++%*%%%++=-*+#++#####%%%%%%%++%==*=*=#+*%%%%%%%%%%%%
%%%%%%%%-*+*+#++#*+=#%%%+%#+=*%%%%%*==+#+:+===++++=====+==#==%++=*#=%%%%%%%%%%%%
%%%%%%%#=++*+%++*#%+%%%#+%*+=#%%%%*---+#+++:.::..::::::---#++%+==*#:*%%%%%%%%%%%
%%%%%%%++++++%+=%%#+%%#+*%*+=%%%**::++=##%#:--:===::=**=-:*-*%*==*#==#%%%%%%%%%%
%%%%%%%+*==++%#-###+%%*=#%*+*%%#*-:=#%#*###*=--++=:-=+===-+-#%#==**+%#%%%%%%%%%%
%%%%%%%+**==*#*=++#+##*+#%%**%%*=:-*###=+%###+===++=++++**=-+#%+++*+%%%%%%%%%%%%
%%%%%%%+***:**=+=+#*#**+%#%+=%#+=##%###--####%%#########%#-==*#=+=++%%%%%%%%%%%%
%%%%%%%+#=#=*+-===**#*++%*=++#*-*%#####==#################:+-+*:==*+%%%%%%%%%%%%
%%%%%%%**+*++:====+*+*=*#-=#*++-######**#*###############*-#=+-=+-=+%%%%%%%%%%%%
%%%%%%%%+++==-=+=-++++-#=-###*--######%%#%##############%*=#=-=++-=:*%%%%%%%%%%%
%%%%%%%%*==-+#+=+====+==*######*#####****+++*#############**=:====@+=%%%%%%%%%%%
%%%%%%%%#-*+=*=*+*--+###%%#####%###*++*++***+++*###########*-===-*%%#%%=+%%%%%%%
%%%%%%%%%-=*==+===--*#*#++***#######%%##***#***+=*########**=++=+%%%%%%- -#%%%%%
%%%%%##**++**+=+=++++**- .=+++++=++==-=======+++-=########***+=+%%%%%#%=  .*%%%%
##***+***#*****+++****#+=+++*++=-=+*#####################*#-=++#%%%%%%%-..  *%%%
+****##***+-*:++++++-*##%%%####*###**+++==++**##########*#+-+%%%%%%#*=:.. . .#%%
******++*#+*%*===*++=:*##+*####**++++***: =############**=:-##*+=-:.   :.  . :%%
*##**+##%##%#%#.##+*+-:-++*##########%%%: :%#########*=---:...      .. ..   . =%
**+*#%%%%%%%%%%*%%*-+==:-:-=+*#######-+-  .-.-.*#*+=--:---:      .. . .: .  . :%
**#%%##%%%%%%%%%%%%*#=#-=---::--==++:   ... ...-=::--------****+-. .. :: .  . -%
%%%%%%%%%%%%%%%%%%#%*=%*+====--::::::::::::-----:--------=:%@@@@@%: . :.    . +%
%%%%%%%%%%%%####***#*+###**++===-==---------------=-------.#@%@@%#: ..:    . .#%
%%%%%%%%%%#+#%@@@@@@%=######****++====-----=-========----+:=%@%*#*.  .. .  . -%%
%%%%%%%%%%#=%%**##%%+=########****+================---=-=+--+*=*#: . :.    . *%%
%%%%%%%%%%%=%%**+++==+##########****+==+*****+=+==---=-====-==%#*=: .: .  . :%%%

""")
    print("Scanji v0.1")
    sleep(0.2)
    print("by SloW47")
    sleep(0.2)
    print("github.com/slow47/Scanji/")
    sleep(0.2)
    print()
    print()
    parser = argparse.ArgumentParser(description="Run and process Nmap scans more efficiently.")
    parser.add_argument("ip", type=str, help="IP address for the initial fast scan.")
    parser.add_argument("-o", "--output", type=str, help="Save output of the detailed scan to a file.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output for more detailed process information.")
    args = parser.parse_args()

    if not validate_ip_address(args.ip):
        print("Error: Invalid IP address provided.")
        parser.print_help()
        sys.exit(1)

    nmap_output = run_nmap_scan(args.ip, args.verbose)
    ports = extract_ports(nmap_output,args.verbose)
    if ports:
        command = create_nmap_command(ports, args.ip,args.verbose)
        execute_nmap_command(command, args.verbose)
        if args.output:
            save_to_file(' '.join(command), args.output)
    else:
        print("No open ports found in the scan.")

if __name__ == "__main__":
    main()

