import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print(f'Connection failed!!!')
        print(f'Error: {e}')
        sys.exit()
    else:
        print(f'Socket created successfully')


    target_host = input('Type the host or IP to be connected: ')
    target_port = int(input('Type the port to be connected: '))

    try:
        s.connect((target_host, target_port))
        print(f'TCP Client connected successfully to the host {target_host} at port {target_port}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Connection failed!!!')
        print(f'Unable to connect on {target_host}:{target_port}')
        print(f'Error: {e}')
        sys.exit()

if __name__ == '__main__':
    main()


