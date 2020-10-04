#from util.jsonManager import *

import sqlite3
from util.serverLog import LogD

def updateIoTData(DM,DBLocation):
    con = sqlite3.connect(DBLocation)
    cur = con.cursor()
    cur.execute("UPDATE PHONECASE SET IS_LOCK=? WHERE PHONECASE_PR=?;",(DM.getData("Lock"),DM.getData("id")))
    LogD("UpdateIoTSQL 완료(id : "+DM.getData("id")+",Lock : "+str(DM.getData("Lock"))+")")
    return True

def updateAndroidData(DM,DBLocation):
    con = sqlite3.connect(DBLocation)
    cur = con.cursor()
    cur.execute("UPDATE PHONE SET IS_LOCK=? WHERE PHONE_PR=?;",(DM.getData("Lock"),DM.getData("id")))
    cur.execute("INSERT INTO LOCKMANAGE (PHONE_UNIQUENUM,MANAGETIME, IS_LOCK) VALUES(?,?,?);",(DM.getData("id"),DM.getData("Time"),DM.getData("Lock")))
    LogD("UpdateAndroidSQL 완료(id : "+DM.getData("id")+",Lock : "+str(DM.getData("Lock"))+")")
    return True