
"""
Abdullah Abubakar
Computer Networking Coursework Assignment 2021/22


Client module
"""

#imports socket module
import socket

#program prompts for positive integer, which is checked to be an integer
i = input("Please enter a positive integer: ")

"""
if i != int:
    print("i must be an integer")
"""

#client utilises socket fucntion
clientSocket = socket.socket()

#client connects to localhost port number 9999
clientSocket.connect(("localhost", 4444))

clientSocket.send(i)


clientSocket.listen(n)
clientSocket.send(bytes(i * n, 0, 'utf-8'))
print("waiting for connections")
print(i)
print(n)
print(i * n, 0)

print(clientSocket.recv(1024).decode())




