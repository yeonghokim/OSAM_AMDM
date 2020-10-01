import datetime

def serverlog():
    d = datetime.datetime.now()
    return '[AMServer '+d.strftime('%Y-%m-%d %H:%M:%S')+']'

def serverlogFile():
    d = datetime.datetime.now()
    return d.strftime('%Y%m%d')

