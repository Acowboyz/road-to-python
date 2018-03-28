import struct
from socket import *

def main():

    # 0. get the download file name 
    downloadfilename = input("please input the file name:")

    # 1. create socket
    udpsocket = socket(AF_INET, SOCK_DGRAM)

    requestfiledata = struct.pack("!H%dsb5sb"%len(downloadfilename), 1, downloadfilename.encode("utf-8"), 0, "octet".encode("utf-8"), 0)

    # 2. send request to server
    udpsocket.sendto(requestfiledata, ("127.0.0.1",69))

    flag = True
    num = 0
    f = open(downloadfilename, "wb")

    while True:
        # 3. receive the request from server 
        responsedata = udpsocket.recvfrom(1024)

        #print(responsedata)

        recvdata, serverinfo = responsedata

        opnum = struct.unpack("!H", recvdata[:2])

        packetnum = struct.unpack("!H", recvdata[2:4])

        #print("opnum:",opnum)
        #print("server_info:",serverinfo)

        if opnum[0] == 3:
            num = num + 1

            if num == 65536:
                num = 0

            #print(num,packetnum[0])
            if num == packetnum[0]:
                f.write(recvdata[4:])
                num = packetnum[0]

            ackdata = struct.pack("!HH", 4, packetnum[0])
            udpsocket.sendto(ackdata, serverinfo)
        elif opnum[0] == 5:
            print("sorry, the file is not exit")
            flag = False

        if len(recvdata) < 516:
            break

    if flag == True:
        f.close()
    else:
        os.unlink(downloadfilename)

    
if __name__ == "__main__":
    main()
