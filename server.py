"""
Abdullah Abubakar
Computer Networking Coursework Assignment 2021/22

Server module
"""
import random
import socket



serverSocket = socket.socket()
print("Socket Created")

serverSocket.bind(("localhost", 4444))

serverSocket.listen()
print("waiting for connections")

while True:
    clientSocket, address = serverSocket.accept()

    n = random.randint(1, 13)

    name = clientSocket.recv(1024).decode()

    print("Connected with ", address, name)

    clientSocket.send(bytes(n))

    clientSocket.close()

serverSocket.close()