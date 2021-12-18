import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'Socket has been created successfully')

host = 'localhost'
port = 5432

s.bind((host, port))
message = 'Server: Heyyyy buddy, how are you doing today?'

while True:
    data, addr = s.recvfrom(4096)

    if data:
        print(f'Server is sending a message...')
        s.sendto(data + (message.encode()), addr)
