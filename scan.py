# -*- coding: utf-8 -*-

#   ────────────────────────────────────────────────
# │                  UTF-8 Encoding Active           │
# │                  Project: Port Scanner           │
# │                   Coded by: R00T-KID             │
# │           GitHub: https://github.com/rootcity    │
# │                      TG: @kidofcity              │
#   ────────────────────────────────────────────────

import socket
import colorama
from colorama import Fore, Style
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear()
die =  input('[+] Show Inactive Results? (y/n >  ')
colorama.init(autoreset=True)

def port_scan(target, port):
    """
    Scans a specific port on a target IP address.

    Args:
    target (str): The IP address to scan.
    port (int): The port number to scan.

    Returns:
    None
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"{Fore.YELLOW}• Port > {port} > {Fore.WHITE} IP {Fore.GREEN}>  {Fore.GREEN}{target} {Fore.WHITE}is {Fore.GREEN}Open")
        else:
            if die in 'n':
                 pass
            elif die in 'y':
                 print(f"{Fore.YELLOW}• Port > {port} > {Fore.WHITE} IP {Fore.GREEN}> {Fore.RED}{target} {Fore.WHITE}is {Fore.RED}Closed")
            else:
                 exit(f'{Fore.RED} [x] Fill in correctly...!')
        sock.close()
    except KeyboardInterrupt:
        print("Scan stopped by user")
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved")
        exit()
    except socket.error:
        print("Couldn't connect to server")
        exit()

def scan_range(start_ip_parts, num_addresses, port):
    """
    Scans a range of IP addresses for a specific port.

    Args:
    start_ip_parts (list): The starting IP address split into its parts.
    num_addresses (int): The number of IP addresses to scan.
    port (int): The port number to scan.

    Returns:
    None
    """
    # Extract the base IP parts (e.g., '10.190.0')
    base_ip = start_ip_parts[:3]
    start_ip_num = int(start_ip_parts[3])

    # Loop through the range of IP addresses and scan each one
    for i in range(num_addresses):
        current_ip_num = start_ip_num + i
        fourth_octet = current_ip_num % 256
        third_octet = (current_ip_num // 256) % 256
        current_ip = f"{base_ip[0]}.{base_ip[1]}.{base_ip[2]}.{fourth_octet + 256 * third_octet}"
        port_scan(current_ip, port)


def main():
    """
    Main function to run the port scanner.

    Prompts the user for input and initiates the scanning process.

    Returns:
    None
    """
    clear()
    start_ip = input("Enter the starting IP address > ")
    num_addresses = int(input("Enter the number of IP addresses (Max:255) > "))
    port = int(input("Enter the port to scan > "))

    start_ip_parts = start_ip.split('.')

    if len(start_ip_parts) != 4:
        print("Invalid IP address format")
        return

    print(f"\nScanning port {port} from {start_ip} for the next {num_addresses} addresses...\n")
    scan_range(start_ip_parts, num_addresses, port)

if __name__ == "__main__":
    main()
