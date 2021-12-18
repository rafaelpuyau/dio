import os
from time import sleep

with open('hosts.txt', 'r') as file:
    dump = file.read()
    dump = dump.splitlines()

    for addr in dump:
        print(f'Verifying the address {addr}')
        os.system(f'ping -c 3 {addr}')
        sleep(5)
