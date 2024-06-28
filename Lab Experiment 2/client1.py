# Capital letter to Small letter conversion for a line of text
# Clent 
from socket import *

serverName = '10.42.0.111'
serverPort = 4553

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input('Enter a uppercase sentence: ')
clientSocket.send(message.encode())

modifiedMsg = clientSocket.recv(2048)
print('From Server: ', modifiedMsg.decode())

clientSocket.close()
