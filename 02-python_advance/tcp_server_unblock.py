from socket import *
from threading import Thread
from time import sleep

def main():
    
    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ("127.0.0.1",7788)
    serSocket.bind(localAddr)
    serSocket.listen(100)

    # set the process unblocking
    serSocket.setblocking(False)
    
    # save the client infomation
    clientAddrList = []
    while True:

        #print("wait for a new client")
        try:
            clientSocket, clientAddr = serSocket.accept()
        except:
            pass
        else:
            print("a new client, :", str(clientAddr))
            clientSocket.setblocking(False)
            clientAddrList.append((clientSocket, clientAddr))

        for clientSocket, clientAddr in clientAddrList:
            try:
                recvData = clientSocket.recv(1024)
            except:
                pass
            else:
                if len(recvData) > 0:
                    print("%s:%s"%(str(clientAddr), recvData))
                else:
                    clientSocket.close()
                    clientAddrList.remove((clientSocket, clientAddr))
                    print("offline:", clientAddr)


if __name__ == "__main__":
    main()

            
