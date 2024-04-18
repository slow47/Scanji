# QuickMap

---

### Nmap Automation Script

This script makes it easy to run Nmap scans for discovering and analyzing open TCP ports on any given IP address.

## Features

- **Quick Scans**: Quickly identifies open ports on an IP.
- **Detailed Analysis**: Runs detailed scans on found ports for extra insights like service versions and OS details.
- **Save Results**: Option to save scan results to a file.
- **Verbose Output**: Provides detailed output for more insight during scans.

## Quick Setup

**Requirements**: Python and Nmap need to be installed on your computer.

- **Install Nmap**:
  - Linux: `sudo apt install nmap`
  - macOS: `brew install nmap`

- **Check Python**:
  - Usually pre-installed on Linux and macOS.

**Download the Script**: Clone this repo or download the `QuickMap.py` file. If you want to run it as an executable, make sure to make it executable with the following command:

```bash
chmod +x QuickMap.py
```
Also if You want to run it quickly every time you can do that by just adding it to your binaries path using this command :
```bash
mv QuickMap.py /usr/local/bin/QuickMap
```


## How to Use

You might need sudo privileges to run Nmap scans depending on your system's configuration. Here are two ways to run the script:

**As an Executable**:
```bash
sudo ./QuickMap.py 192.168.1.1 -v
```

**Or if did add it to the binaries path**:
```bash
sudo QuickMap 192.168.1.1 -v
```

**Save Output**: To save the output to a file:
```bash
sudo QuickMap 192.168.1.1 -o results.txt
```

**Using Python**:
```bash
sudo python QuickMap.py 192.168.1.1 -v
```



Use this script for straightforward network scanning with minimal setup.

This will provide step-by-step details of the scanning process.

By @SloW47 with the help of @Dexter24601 ♡
