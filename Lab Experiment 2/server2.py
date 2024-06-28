# Send an integer and operation name (either ‘prime’ or ‘palindrome’)
# to the server and check whether it’s a prime (or palindrome) or not.
# Server

import socket

def is_prime(num):
    if num < 2:
        return "NonPrime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "NonPrime"
        return "Prime"
    
def is_palindrome(num):
    str_num = str(num)
    return "Palindrome" if str_num == str_num[::-1] else "NonPalindrome"

serverName = '10.42.0.111'
serverPort = 5353

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket is created')
s.bind((serverName, serverPort))
print('Server is binding with ip and port')
s.listen(3)

print('Server is listening')
print("Server is ready to receive the integer and check prime/nonprime or palindrone/NonPalindrome")
while True:
    connectionSocket, addr = s.accept()
    data = connectionSocket.recv(1024).decode().split()
    if len(data) == 2:
        try:
            num = int(data[0])
            operation = data[1].lower()
            result = None
            if operation == 'prime':
                result = is_prime(num)
            elif operation == 'palindrome':
                result = is_palindrome(num)
                connectionSocket.send(result.encode())
        except ValueError:
            connectionSocket.send("Invalid input. Please send an integer and operation.".encode())
    else:
        connectionSocket.send("Invalid input.Please send an integer and operation.".encode())
    connectionSocket.close()
