#from util.jsonManager import *

import sqlite3
con = sqlite3.connect('/home/codespace/workspace/AMDMserver.sqlite3')

class sqlManager:
    def __init__(self):
        print("");
    
    def updateIoTData(self,DM):
        # IoT테이블의 id인것을 찾아 Lock과 PhoneLock을 업데이트
        cur = con.cursor()
        cur.execute("UPDATE PHONECASE SET IS_LOCK=? WHERE PHONECASE_PR=?;",(DM.getData("Lock"),DM.getData("id")))
        cur.execute("SELECT * FROM PHONECASE WHERE PHONECASE_PR=1;")
        for row in cur:
            print(row)

        return True;
