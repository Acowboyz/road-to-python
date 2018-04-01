from socket import *
from threading import Thread
from time import sleep

def dealWithClient(newSocket, destAddr):
    while True:
        recvData = newSocket.rec(1024)
        if len(recvData) > 0:
            print("recv[%s]:%s"%(str(destAddr), recvData))
        else:
            print("[%s] the client is close"%str(destAddr))


def main():
    
    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ("",7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            print("main thread, wait for a new client")
            newSocket, destAddr = serSocket.accept()

            print("main thread, create a new thread to deal with the data of new client")
            client = Thread(target = dealWithClient, arg=(newSocket, destAddr))
            client.start()
            
    finally:
        serSocket.close()

if __name__ == "__main__":
    main()

            
