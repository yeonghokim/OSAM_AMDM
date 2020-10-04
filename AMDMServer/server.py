from socket import *
from util.serverLog import *
from send.send import *
from util.jsonManager import *
from util.DBManager import *

Debug = 1

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

SQLManager = MysqlManager()

while(1==1):
    if(Debug==0):
        connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림
        LogD(str(addr) + "에서 접속함")
        data =connectionSocket.recv(1024)
        dataDM = JsonToDataManager(data.decode("utf-8"))
    else:
        data = DM.getFileStr()
        dataDM = JsonToDataManager(data)

    if(1==2):
        # 안드로이드 데이터 요청
        LogD("Android 데이터 요청") 
        connectionSocket.send("I am server".encode("utf-8")) 
        
    elif(dataDM.getData("type")=="IoT"):
        LogD("IoT_DATA " + dataDM.getFileStr().replace("\n", ""))
        #id의 Lock과 phoneLock을 업데이트
        if(SQLManager.updateIoTData(dataDM)):
            LogD("업데이트가 정상적으로 이루어졌습니다.") 
            if(Debug==0):
                connectionSocket.send("Success Comment".encode("utf-8"))
        else:
            LogE("업데이트에 오류가 생겼습니다.")
            if(Debug==0):
                connectionSocket.send("Error Comment".encode("utf-8"))

    else:
        # 안드로이드 데이터 보냄
        LogD("Android_받은 것 : " + data.decode("utf-8"))   
        connectionSocket.send("I am server".encode("utf-8"))

    if(Debug==1):
        connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림

serverSocket.close();

