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

**Download the Script**: Clone this repo or download the `QuickMap.py` file.

## How to Use

**Basic Scan**: Run the script with an IP address:
```bash
python QuickMap.py 192.168.1.1
```

**Save Output**: To save the output to a file:
```bash
python QuickMap.py 192.168.1.1 -o results.txt
```

**Verbose Output**: For a more detailed output:
```bash
python QuickMap.py 192.168.1.1 -v
```

Use this script for straightforward network scanning with minimal setup.

This will provide step-by-step details of the scanning process.

By SloW47 ♡
