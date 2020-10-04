import sqlite3
con = sqlite3.connect('/home/codespace/workspace/AMDMserver.sqlite3')

cur = con.cursor()
cur.execute("UPDATE USER SET USER_NAME='김땡호' WHERE USER_PR=1;")
cur.execute("SELECT * FROM USER")
for row in cur:
    print(row);