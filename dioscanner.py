from nmap import nmap
import sys

scanner = nmap.PortScanner()
print(f'Welcome to DIOScanner')
print('-' * 21)
host = input('Type the host to be verified: ')

while True:

    option = int(input(f"""\nChoose the type of scan:
    1 - SYN Scan
    2 - UDP Scan
    3 - Intense Scan
    4 - Exit

    Type your option: """))

    if option == 1:
        print(f'Nmap version: {scanner.nmap_version()}')
        scanner.scan(host, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print(f'Host Status: {scanner[host].state()}')
        print(scanner[host].all_protocols())
        print(f'')
        print(f'Opened ports: {scanner[host]["tcp"].keys()}')
        break
    elif option == 2:
        print(f'Nmap version: {scanner.nmap_version()}')
        scanner.scan(host, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print(f'Host Status: {scanner[host].state()}')
        print(scanner[host].all_protocols())
        print(f'')
        print(f'Opened ports: {scanner[host]["udp"].keys()}')
        break
    elif option == 3:
        print(f'Nmap version: {scanner.nmap_version()}')
        scanner.scan(host, '1-1024', '-v -sC')
        print(scanner.scaninfo())
        print(f'Host Status: {scanner[host].state()}')
        print(scanner[host].all_protocols())
        print(f'')
        print(f'Opened ports: {scanner[host]["tcp"].keys()}')
        break
    elif option == 4:
        print(f'Exiting...')
        sys.exit()
    else:
        print(f'\nChoose a valid option'.upper())
