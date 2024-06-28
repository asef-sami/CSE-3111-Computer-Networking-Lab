#Capital letter to Small letter conversion for a line of text.
# Server

import socket
serverName = '10.42.0.111'
serverPort = 4553
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((serverName, serverPort))
s.listen(3)
print("Server is ready to receive")

while True:
    connectionSocket, addr = s.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    smaller_sentence = sentence.lower()
    connectionSocket.send(smaller_sentence.encode())
    connectionSocket.close()
