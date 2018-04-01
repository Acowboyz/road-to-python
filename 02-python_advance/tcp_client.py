from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

serverAddr = ("127.0.0.1",8899)

clientSocket.connect(serverAddr)

clientSocket.send("hello".encode("utf-8"))

recvData = clientSocket.recv(1024)

print("recvData:", recvData)

clientSocket.close()


