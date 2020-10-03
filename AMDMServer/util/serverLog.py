from util.ServerTime import *

logdirectory = "/home/codespace/workspace/AMDMServer/logs/"

logDefaultName = "D"+serverlogFile()+".txt"
logErrorName = "E"+serverlogFile()+".txt"
logWarningName = "W"+serverlogFile()+".txt"

#평상시 로그
def LogD(message):
    print(serverlog()+" "+message)
    try:
        f = open(logdirectory+logDefaultName, 'a')
    except FileNotFoundError:
        f = open(logdirectory+logDefaultName, 'w')
        
    f.write(serverlog()+" "+message+"\n")
    f.close()
    return;

#에러 로그
def LogE(message):
    print(serverlog()+" "+message)
    try:
        f = open(logdirectory+logErrorName, 'a')
    except FileNotFoundError:
        f = open(logdirectory+logErrorName, 'w')
        
    f.write(serverlog()+" "+message+"\n")
    f.close()
    return;

#경고 로그
def LogW(message):
    print(serverlog()+" "+message)
    try:
        f = open(logdirectory+logWarningName, 'a')
    except FileNotFoundError:
        f = open(logdirectory+logWarningName, 'w')
        
    f.write(serverlog()+" "+message+"\n")
    f.close()
    return;