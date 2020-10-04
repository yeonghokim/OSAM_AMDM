from socket import *
import threading
from util.serverLog import *
from send.send import *
from util.jsonManager import *
from util.DBManager import updateIoTData
from util.DBManager import updateAndroidData
from util.jsonManager import JsonToDataManager
from util.jsonManager import DataManager
from util.serverLog import LogD
from util.serverLog import LogE

Debug = 1

host = "127.0.0.1"
port = 12345

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((host,port)) 
serverSocket.listen(1)

LogD("서버 생성완료. 대기중입니다.")

DM = DataManager()
DM.setData("type","Android")
DM.setData("id","1")
DM.setData("Lock",1)
DM.setData("requestType",1)
DM.setData("Time","20201004_13:49:12")

DBLocation= '/home/codespace/workspace/AMDMserver.sqlite3'

while(True):

#    connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림
#    LogD(str(addr) + "에서 접속함")
#    data =connectionSocket.recv(1024)
#    dataDM = JsonToDataManager(data.decode("utf-8"))

    data = DM.getFileStr()
    dataDM = JsonToDataManager(data)

    if(dataDM.getData("type")=="Android"):

        if(dataDM.getData("requestType")==1):
            LogD("Android_받은 것 : " + dataDM.getFileStr())
            t = threading.Thread(target=updateAndroidData, args=(dataDM,DBLocation))
            t.daemon = True
            t.start()
            
        elif(dataDM.getData("requestType")==2):
            LogD("Android 데이터 요청")

    elif(dataDM.getData("type")=="IoT"):
        LogD("IoT_DATA " + dataDM.getFileStr())
        t = threading.Thread(target=updateIoTData, args=(dataDM,DBLocation))
        t.daemon = True
        t.start()

    connectionSocket,addr = serverSocket.accept() #accept 할동안 기다림

serverSocket.close()

