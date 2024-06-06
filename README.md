# Network Scanner

## Description

A Python-based network scanner that discovers all the devices connected to a network and displays their IP addresses. This tool can be used for network monitoring, security assessments, and troubleshooting.

## Features

- Scans a given network range to discover active hosts.
- Displays IP addresses of active hosts.
- Uses multithreading to speed up the scanning process.

## Prerequisites

Before you start, make sure you have:

- Basic understanding of Python programming.
- Python installed on your machine.
- Basic knowledge of networking concepts.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/network-scanner.git
    cd network-scanner
    ```

2. **Install required packages (if any):**

    This script uses only Python's built-in modules, so no additional packages are required.

## Usage

1. **Run the script:**

    ```sh
    python network_scanner.py
    ```

2. **Enter the network range when prompted:**

    When you run the script, it will prompt you to enter the network range to scan. For example, enter `192.168.1.0/24` to scan the 192.168.1.x subnet.

3. **View the results:**

    The script will output a list of active hosts in the specified network range.

## Example

```sh
$ python network_scanner.py
Enter the network to scan (e.g., 192.168.1.0/24): 192.168.1.0/24
Active hosts:
192.168.1.1
192.168.1.5
192.168.1.12
