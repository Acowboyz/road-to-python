import struct
from socket import *

def main():

    # 0. get the upload file name 
    uploadfilename = input("please input the file name:")

    # 1. create socket
    udpsocket = socket(AF_INET, SOCK_DGRAM)

    requestfiledata = struct.pack("!H%dsb5sb"%len(uploadfilename), 2, uploadfilename.encode("utf-8"), 0, "octet".encode("utf-8"), 0)

    # 2. send request to server
    udpsocket.sendto(requestfiledata, ("127.0.0.1",69))

    flag = True
    num = 0
    f = open(uploadfilename, "rb")

    while True:
        # 3. receive the request from server 
        responsedata = udpsocket.recvfrom(1024)

        #print(responsedata)

        recvdata, serverinfo = responsedata

        opnum = struct.unpack("!H", recvdata[:2])

        packetnum = struct.unpack("!H", recvdata[2:4])

        #print("opnum:",opnum)
        #print("server_info:",serverinfo)

        # ack
        if opnum[0] == 4:

            if num == 65536:
                num = 0

            #print(num,packetnum[0])
            if num == packetnum[0]:
                content = f.read(512)
                num = num + 1

                uploadfiledata = struct.pack("!HH%ds"%len(content), 3, num, content) 
                udpsocket.sendto(uploadfiledata, serverinfo)

                if len(content) < 512:
                    break

        elif opnum[0] == 5:
            print("error")
            flag = False

    f.close()

    
if __name__ == "__main__":
    main()
