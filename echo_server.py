"""echo server"""

import socket
import threading

port = 9999

def handle(client_socket, client_addr):
    print(client_addr)
    received_msg = client_socket.recv(4096) #number of bytes this function can receive at a time
    received_msg = received_msg.decode()
    print(received_msg)
    client_socket.send(received_msg.upper().encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('', port)) #uses a tuple #'' means to accept any request

    server_socket.listen()

    print("Server is listening")
    while True:
        (client_socket, client_addr) = server_socket.accept()
        #handle(client_socket, client_addr)
        thread = threading.Thread(target = handle, args = [client_socket, client_addr])
        thread.start()

    server_socket.close()

main()