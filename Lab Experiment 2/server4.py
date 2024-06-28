# Design and implement a non-idempotent operation using exactly-once
# semantics that can handle the failure of request messages, failure of
# response messages and process execution failures.With error handling

# Server
import socket
import random

serverName = '10.42.0.111'
serverPort = 5353

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print("Socket creation failed with error %s" % (err))

# Attempting to bind the socket to the server address and port
try:
    s.bind((serverName, serverPort))
    print("Successfully Binded")
except Exception as err:
    print("Binding failed! Error is: %s" % (err))

# Attempting to start listening for incoming connections
try:
    s.listen(20)
    print("Server is listening")
except Exception as err:
    print("Listening failed! Error is: %s" % (err))

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    account_list = [
        ['Farhan', '1234', '1169'],
        ['Sami', '1234', '45720'],
        ['Moyeed', '1234', '70000'],
        ['Kader', '1234', '1200']
    ]

    c.send('Enter Your Account Name : '.encode())
    account_name = c.recv(1024).decode()
    c.send('Enter Your Account Pin : '.encode())
    pincode = c.recv(1024).decode()

    verification_status = False
    account_info = []

    # Verifying the account credentials
    for acc in account_list:
        if acc[0] == account_name and acc[1] == pincode:
            verification_status = True
            account_info = acc
            break

    if verification_status:
        command_prompt = """
            Enter the commands below:
            1. To check your account balance -> Press '1'
            2. To withdraw from your account -> Press '2'
            3. To deposit money in your account -> Press '3'
            4. To terminate the transaction -> Press '4'
        """
        c.send(f"Successfully Logged in\n{command_prompt}".encode())
        transaction_count = 0

        while True:
            command = c.recv(1024).decode()

            if command == '1':
                c.send(f'Current balance is {account_info[2]}'.encode())
            elif command == '4':
                print('Disconnected from', addr)
                c.close()
                break
            elif command == '3' or command == '2':
                c.send("Enter Amount : ".encode())
                amount = c.recv(1024).decode()

                # Simulating a random transaction error (30% chance)
                random_number = random.randint(1, 10)
                if random_number <= 3:
                    c.send('Transaction error. Please try again.'.encode())
                else:
                    if command == '3':
                        new_amt = int(account_info[2]) + int(amount)
                        account_info[2] = str(new_amt)
                        c.send(f'New balance is {account_info[2]}'.encode())
                    elif command == '2':
                        cur_balance = int(account_info[2])
                        if cur_balance >= int(amount):
                            cur_balance -= int(amount)
                            account_info[2] = str(cur_balance)
                            c.send(f'New balance is {account_info[2]}'.encode())
                        else:
                            c.send('Insufficient Balance'.encode())

                    transaction_count += 1
                    if transaction_count == 10:
                        c.send('10 Successful transactions done'.encode())
                        break
            else:
                c.send('Enter a valid command'.encode())
    else:
        c.send("Incorrect account name/pin\n".encode())

    c.close()
