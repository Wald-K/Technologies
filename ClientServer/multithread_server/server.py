import socket
import threading
from _thread import *

# print_lock = threading.Lock()

#thread function
def threaded(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            # print_lock.release()
            break
        
        # reverse received string
        data = data[::-1] 
        conn.sendall(data)
    
    conn.close()




if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 5)
    s.bind((HOST, PORT))
    print('Server is listening')

    while True:
        s.listen(1)
        conn, addr = s.accept()
        # print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1]) 
        start_new_thread(threaded, (conn,))
    s.close()



# import socket, threading
# class ClientThread(threading.Thread):
#     def __init__(self, clientAddress, clientsocket):
#         threading.Thread.__init__(self)
#         self.csocket = clientsocket
#         print ("New connection added: ", clientAddress)
#     def run(self):
#         print ("Connection from : ", clientAddress)
#         #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
#         msg = ''
#         while True:
#             data = self.csocket.recv(2048)
#             msg = data.decode()
#             if msg=='bye':
#               break
#             print ("from client", msg)
#             self.csocket.send(bytes(msg,'UTF-8'))
#         print ("Client at ", clientAddress , " disconnected...")


# LOCALHOST = "127.0.0.1"
# PORT = 8080
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind((LOCALHOST, PORT))
# print("Server started")
# print("Waiting for client request..")
# while True:
#     server.listen(1)
#     clientsock, clientAddress = server.accept()
#     newthread = ClientThread(clientAddress, clientsock)
#     newthread.start()


