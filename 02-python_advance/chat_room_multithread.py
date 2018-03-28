from threading import Thread
from socket import *

def revdata():
    while True:
        data, addr = udpsocket.recvfrom(1024)
        print("\r>>%s:%s"%(str(addr), data))

def senddata():
    while True:
        senddata = input("<<")
        udpsocket.sendto(senddata.encode("utf-8"), (destip, destport))

udpsocket = None
destip = ""
destport = 0

def main():

    global udpsocket
    global destip
    global destport

    destip   = input("ip:")
    destport = int(input("port:")) 

    udpsocket = socket(AF_INET, SOCK_DGRAM)

    udpsocket.bind(("",4567))

    sd = Thread(target = senddata)
    rv = Thread(target = revdata)

    sd.start()
    rv.start()

    sd.join()
    rv.join()

if __name__ == "__main__":
    main()
