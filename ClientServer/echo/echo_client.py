import socket

HOST = '127.0.0.1'
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        text = input()

        b = bytes(text, 'utf-8')
        print(b)
        s.sendall(b)
        # s.sendall(b'Hello world')
        data = s.recv(1024)

        print('Received data ', data)