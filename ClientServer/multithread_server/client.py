import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))

    message = bytes('message to convert', 'utf-8')


    while True:
        s.send(message)

        data = s.recv(1024)
        print('Data received ', data)

        answer = input('Do you want to continue ?')
        if answer == 'Y':
            continue
        else:
            break
    
    s.close()

# import socket
# SERVER = "127.0.0.1"
# PORT = 8080
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((SERVER, PORT))
# client.sendall(bytes("This is from Client",'UTF-8'))
# while True:
#     in_data =  client.recv(1024)
#     print("From Server :" ,in_data.decode())
#     out_data = input()
#     client.sendall(bytes(out_data,'UTF-8'))
#     if out_data=='bye':
#         break
# client.close()
