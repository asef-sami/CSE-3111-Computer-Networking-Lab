# Design and implement a non-idempotent operation using exactly-once
# semantics that can handle the failure of request messages, failure of
# response messages and process execution failures.With error handling.

# client code with time
import socket
import time

# Server’s IP address
serverName = '10.33.3.9'
# Port for communication
serverPort = 5353

# Creating Client Socket
try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print("Socket creation failed with error %s" % (err))
# Record the start time
start_time = time.time()

# Connecting to the server
try:
    clientSocket.connect((serverName, serverPort))
    print("Connected with Tanvir’s server successfully1")
except Exception as err:
    print("Connection with server failed! Error is: %s" % (err))

# Record the connection time
connection_time = time.time() - start_time
#print(f"Connection time: {connection_time} seconds")

while True:
    print(clientSocket.recv(1024).decode())
    # send account name
    name = input()
    clientSocket.send(name.encode())
    print(clientSocket.recv(1024).decode())
    # send account pin
    pin = input()
    clientSocket.send(pin.encode())
    print(clientSocket.recv(1024).decode())
    while True:
        command = input()
        clientSocket.send(command.encode())
        print(clientSocket.recv(1024).decode())
        if command == '4': # exit
            break
        elif command == '3' or command == '2': # deposit / withdraw
            amount = input()
        clientSocket.send(amount.encode())
        print(clientSocket.recv(1024).decode())
        print("Connection closed!")
        # Record the end time
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time: {total_time} seconds")
        break
    clientSocket.close()