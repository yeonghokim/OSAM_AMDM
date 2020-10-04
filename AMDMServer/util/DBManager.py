#from util.jsonManager import *

import sqlite3
from util.serverLog import LogD

def updateIoTData(DM,DBLocation):
    con = sqlite3.connect(DBLocation)
    cur = con.cursor()
    cur.execute("UPDATE PHONECASE SET IS_LOCK=? WHERE PHONECASE_PR=?;",(DM.getData("Lock"),DM.getData("ID")))
    LogD("UpdateIoTSQL 완료(id : "+str(DM.getData("ID"))+",Lock : "+str(DM.getData("Lock"))+")")
    con.commit();
    con.close();
    return True

def updateAndroidData(DM,DBLocation):
    con = sqlite3.connect(DBLocation)
    cur = con.cursor()
    cur.execute("UPDATE PHONE SET IS_LOCK=? WHERE PHONE_PR=?;",(DM.getData("Lock"),DM.getData("ID")))
    cur.execute("INSERT INTO LOCKMANAGE(PHONE_UNIQUENUM,MANAGETIME, IS_LOCK) VALUES(?,CURRENT_TIMESTAMP,?);",(DM.getData("ID"),DM.getData("Lock")))
    con.commit();
    con.close();
    LogD("UpdateAndroidSQL 완료(id : "+str(DM.getData("ID"))+",Lock : "+str(DM.getData("Lock"))+")")
    return True

def requestAndroidDataToIoT(DM,DBLocatio,androidSocket):
    print(DM.getFileStr())
    con = sqlite3.connect(DBLocation)
    cur = con.cursor()
    cur.execute("UPDATE PHONECASE SET IS_LOCK=? WHERE PHONECASE_PR=?;",(DM.getData("Lock"),DM.getData("IoTID")))
    con.commit();
    con.close();

    #androidSocket에 완료되었다고 보내기
    #androidSocket.send(data)

    LogD("requestAndroidSQL 완료(AdminID : "+str(DM.getData("ID"))+",IoTID : "+str(DM.getData("IoTID"))+"Lock : "+str(DM.getData("Lock"))+")")
    return True

