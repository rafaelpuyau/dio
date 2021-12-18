import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'Client socket has been created successfully')

host = 'localhost'
port = 5433
message = 'Hey there Server, what\'s up?\n'

try:
    s.sendto(message.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print(f'Client: {data}')
finally:
    print(f'Closing the current connection')
    s.close()
