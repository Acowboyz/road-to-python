from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

destIp   = input("IP:")
destPort = int(input("port:"))
sendData = input("Data:") 


udpSocket.sendto(sendData.encode("utf-8"), (destIp, destPort))
