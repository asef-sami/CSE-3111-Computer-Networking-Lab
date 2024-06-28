#Send an integer and operation name (either ‘prime’ or ‘palindrome’) to the server and check whether it’s a prime (or palindrome) or not.
# Server

from socket import *

serverName = '10.42.0.111'
serverPort = 5353

#creating socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

integernum = input('Enter a integer number: ')
operation = input('Enter operation name (prime/palindrome): ')

#sending integer and operation to the server
data = f"{integernum} {operation}"
clientSocket.send(data.encode())
result = clientSocket.recv(1024).decode()

print(f"Result from server: {result}")
clientSocket.close()