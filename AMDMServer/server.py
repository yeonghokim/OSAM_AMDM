from socket import *
from util.serverLog import *
from send.send import *
from util.jsonManager import *

host = "127.0.0.1"
port = 12345

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((host,port)) 
serverSocket.listen(1)

LogD("서버 생성완료. 대기중입니다.")

DM = DataManager()
DM.setData("type","IoT")
DM.setData("id","1234567")
DM.setData("Lock",0)
DM.setDatasFirst("PhoneLock")
DM.setDatas("PhoneLock",'19-760730001',0)
DM.setDatas("PhoneLock",'19-760730002',0)
DM.setDatas("PhoneLock",'19-760730003',1)
DM.setDatas("PhoneLock",'19-760730004',0)
print(DM.getFileStr())

while(1==1):
    connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림

    LogD(str(addr) + "에서 접속함")
    
    data =connectionSocket.recv(1024)

    if(1==2):
        # 안드로이드 데이터 요청
        LogD("Android 데이터 요청") 
        connectionSocket.send("I am server".encode("utf-8")) 
    elif(1==1):
        # IoT 데이터 보냄
        # 몇번째 휴대폰 케이스 잠금유무
        # 이 휴대폰 케이스에서 어떤것들이 반납 되었는지(케이스 반납 유무)
        LogD("IoT_받은 것 : " + data.decode("utf-8"))   
        connectionSocket.send("I am server".encode("utf-8"))
    else:
        # 안드로이드 데이터 보냄
        LogD("Android_받은 것 : " + data.decode("utf-8"))   
        connectionSocket.send("I am server".encode("utf-8"))

serverSocket.close();

