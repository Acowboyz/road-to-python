from socket import *
from multiprocessing import Process
import re

# set static web root folder 
HTML_ROOT_DIR = "./html"

# tcp server
def clientHandler(clientSocket, clientAddr):
    """handle the request of the client"""
    recvData = clientSocket.recv(1024)
    print(recvData)

    recvData_lines = recvData.splitlines()
    for line in recvData_lines:
        print(line)

    # Get / HTTP/1.1
    recv_start_line = recvData_lines[0]

    # get the request page
    file_name = re.match(r"\w+ +(/[^ ]*) ", recv_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"

    # open the file
    try :
        file_ = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: My Server\r\n"
        response_body = "This file is not found!"
    else: 
        file_content = file_.read()
        file_.close()
        
        # response data to web client
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My Server\r\n"
        response_body = file_content.decode("utf-8")
    finally:
        response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)

    clientSocket.send(bytes(response, "utf-8"))
    clientSocket.close()
    
    # encapsulation
    # Inheritance
    # Polymorphism
    
    
    
def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ("",8000)
    serverSocket.bind(localAddr)
    serverSocket.listen(128)

    try:
        while True:
            clientSocket, clientAddr = serverSocket.accept()
            print("[%s, %s] client connected" %clientAddr)
            clientProcess = Process(target=clientHandler, args=(clientSocket, clientAddr))
            clientProcess.start()
    finally:
        serverSocket.close()

if __name__ == "__main__":
    main()
