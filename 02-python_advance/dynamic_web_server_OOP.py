from socket import *
from multiprocessing import Process
import re
import sys
# set static web root folder 
HTML_ROOT_DIR = "./html"

WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    """"""
    def __init__(self):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    
    def bind(self, port):
        """"""
        self.serverSocket.bind(("",port))

    def start(self):
        self.serverSocket.listen(128)

        try:
            while True:
                clientSocket, clientAddr = self.serverSocket.accept()
                print("[%s, %s] client connected" %clientAddr)
                clientProcess = Process(target=self.clientHandler, args=(clientSocket, clientAddr))
                clientProcess.start()
        finally:
            self.serverSocket.close()

    def start_response(self, status, headers):
        response_headers = "HTTP/1.1" + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        # HTTP/1.1 200 OK\r\nContent-Type: text/plain
        self.response_headers = response_headers

    def clientHandler(self, clientSocket, clientAddr):
        """handle the request of the client"""
        recvData = clientSocket.recv(1024)
        print(recvData)

        recvData_lines = recvData.splitlines()
        for line in recvData_lines:
            print(line)

        # Get / HTTP/1.1
        recv_start_line = recvData_lines[0]
        print("recv_startline:", recv_start_line)

        # get the request page
        file_name = re.match(r"\w+ +(/[^ ]*) ", recv_start_line.decode("utf-8")).group(1)
        method = re.match(r"\w+ +(/[^ ]*) ", recv_start_line.decode("utf-8")).group(1)

        # implement wsgi
        if file_name.endswith(".py"):
            try:
                module_ = __import__(file_name[1:-3])
            except Exception:
                self.response_headers = "HTTP/1.1 404 Not Found\r\n"
                response_body = "not found"
            else:
                #env = {
                #    "PATH_INFO": file_name,
                #    "METHOD": method
                #}
                env = {}

                response_body = module_.application(env, self.start_response)

            response = self.response_headers + "\r\n" + response_body
        else:
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
    
def main():
    sys.path.insert(0 ,WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()
    

if __name__ == "__main__":
    main()
