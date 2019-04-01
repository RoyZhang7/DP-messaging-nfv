from threading import Thread
from socket import *

# Sending messages
class SendMsg(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__selfPort = 1024
        self.__targetPort = 1025
        self.__socket = socket(AF_INET, SOCK_DGRAM)
        self.getInfo()

    # Acquire target IP
    def getInfo(self):
        # Acquire IP
        self.__targetIp = input("Enter IP address：")
        # Bind local port
        self.__socket.bind(("",self.__selfPort))
        self.__targetAddr = (self.__targetIp, self.__targetPort)

    # Send message
    def run(self):
        while True:
            msg = input("\rEnter Message:")
            self.__socket.sendto(msg.encode("utf-8"),self.__targetAddr)

# Receive message
class RecvMsg(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__selfPort = 1025
        self.__socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket.bind(("",self.__selfPort))

    # Send message
    def run(self):
        while True:
            msg,addrInfo  = self.__socket.recvfrom(1024)
            print("\r%s：%s"%(addrInfo[0],msg.decode("utf-8")))
            print("\rEnter Message:")

if __name__ == '__main__':
    send = SendMsg()
    recv = RecvMsg()
    send.start()
    recv.start()
