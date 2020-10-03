import json
from collections import OrderedDict

class DataManager:
    def __init__(self):
        self.file_data = OrderedDict()

    def setData(self,key,data):
        self.file_data[key]=data

    def getData(self,key):
        return self.file_data[key]

    def setDatasFirst(self,key):
        self.file_data[key]={}

    def setDatas(self,key,subkey,data):
        self.file_data[key][subkey]=data

    def getFile(self):
        return self.file_data

    def getFileStr(self):
        return json.dumps(self.file_data,ensure_ascii=False,indent="\t")

# DM = DataManager()
# DM.setData("name","Computer")
# DM.setData("language","kor")
# DM.setDatasFirst("words")
# DM.setDatas("words",'ram','램')
# DM.setDatas("words",'process','프로세스')
# DM.setDatas("words",'processor','프로세서')
# DM.setDatas("words",'CPU','씨피유')
# DM.setData("number",4)
# print(DM.getFileStr())
