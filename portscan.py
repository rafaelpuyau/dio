import socket
from time import sleep

host = input('Type the host or IP addrees to be verified: ')
ports = input('Type the port number: ').split(',')

for port in ports:
    # AF_INET : connection type for IPv4
    # SOCk_STREAM : connection type TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((host, int(port.lstrip())))
    print(f'Scanning port {port.lstrip()}...')
    sleep(2)
    if code == 0:
        print(f'{port.lstrip()} - Port opened')
    else:
        print(f'{port.lstrip()} - Port closed')
else:
    print(f'Finished scan')
