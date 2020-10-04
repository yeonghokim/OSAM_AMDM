from socket import *
import threading
from util.serverLog import *
from send.send import *
from util.jsonManager import *
from util.DBManager import updateIoTData
from util.DBManager import updateAndroidData
from util.DBManager import requestAndroidDataToIoT
from util.jsonManager import JsonToDataManager
from util.jsonManager import DataManager
from util.serverLog import LogD
from util.serverLog import LogE

Debug = 1

host = "127.0.0.1"
port = 12345

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((host,port)) 
serverSocket.listen(5)

LogD("서버 생성완료. 대기중입니다.")

DM = DataManager()
DM.setData("Type","Android")
DM.setData("RequestType",2)
DM.setData("ID",1)
DM.setData("IoTID",1)
DM.setData("Lock",1)
DM.setData("Time","2020-10-04 13:49:12")

DBLocation= '/home/codespace/workspace/AMDMserver.sqlite3'

while(True):

#    connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림
#    LogD(str(addr) + "에서 접속함")
#    data =connectionSocket.recv(1024)
#    dataDM = JsonToDataManager(data.decode("utf-8"))

    data = DM.getFileStr()
    dataDM = JsonToDataManager(data)

    if(dataDM.getData("Type")=="Android"):
        LogD("Android Data " + dataDM.getFileStr())

        if(dataDM.getData("RequestType")==1):
            # 핸드폰이 잠길때
            # 핸드폰이 열릴때
            LogD("Android 데이터 수신")
            t = threading.Thread(target=updateAndroidData, args=(dataDM,DBLocation))
            t.start()
            
        elif(dataDM.getData("RequestType")==2):
            # Iot가 열릴때 (관리자) Android -> Server -> IoT
            LogD("Android 데이터 전송 요청")
            LogD("IoT Data " + dataDM.getFileStr())
            t = threading.Thread(target=requestAndroidDataToIoT, args=(dataDM,DBLocation,"NULL"))
            t.start()
        
        elif(dataDM.getData("RequestType")==3):
            # 핸드폰 잠금 유무 확인(관리자)
            LogD("Android 데이터 요청")

    elif(dataDM.getData("Type")=="IoT"):
        # Iot가 잠길때
        LogD("IoT Data " + dataDM.getFileStr())
        t = threading.Thread(target=updateIoTData, args=(dataDM,DBLocation))
        t.start()

    connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림

serverSocket.close()

# Iot 강제 잠금(관리자) 서버가 요청

