"""echo_client"""

import socket

host = 'localhost'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

client_socket.send(b"hello server")

received_msg = client_socket.recv(4096)
print(received_msg.decode())

client_socket.close()