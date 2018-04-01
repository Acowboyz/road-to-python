from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", 8899))

serverSocket.listen(5)

# clientSocket : accept new client to accoiate
# clientSocket : information of new client ip, port
clientSocket, clientInfo = serverSocket.accept()

recvdata = clientSocket.recv(1024)

clientSocket.send("welcome".encode("utf-8"))

print("clientinfo", clientInfo)
print("data:", recvdata)

clientSocket.close()
serverSocket.close()
