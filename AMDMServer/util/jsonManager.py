import json
from collections import OrderedDict

#Json을 관리해주는 클래스
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
        return json.dumps(self.file_data,ensure_ascii=False,indent="").replace("\n", "")

#Json 데이터를 DataManager 객체로 변환
def JsonToDataManager(str):
    NDM = DataManager()
    NDM.file_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(str)
    return NDM

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
