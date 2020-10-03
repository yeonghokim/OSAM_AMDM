from socket import *
from util.serverLog import *
from send.send import *

host = "127.0.0.1"
port = 12345

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((host,port)) 
serverSocket.listen(1)

LogD("서버 생성완료. 대기중입니다.")

while(1==1):
    connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림

"""
print(str(addr),"에서 접속함")

data =connectionSocket.recv(1024)

print("받은 것 : ",data.decode("utf-8"))

connectionSocket.send("I am server".encode("utf-8"))
print("메세지 보냄")

serverSocket.close();
"""
