from socket import *
import select
import sys

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", 7788))
    serverSocket.listen(5)

    inputs = [serverSocket]

    while True:

        readable, writeable, exceptional = select.select(inputs, [], [])

        for sock in readable:

            if sock == serverSocket:
                newSocket, newAddr = serverSocket.accept()

                inputs.append(newSocket)
            elif sock == sys.stdin:
                pass
           
            else:
                data = sock.recv(1024)
                if data:
                    sock.send(data)
                else:
                    inputs.remove(sock)
                    sock.close()




if __name__ == "__main__":
    main()

