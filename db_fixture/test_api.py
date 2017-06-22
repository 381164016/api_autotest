import requests
import json

class testApi(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data

    @property
    def testApi(self):
        # 根据不同的访问方式来访问接口
        try:
            if self.method == 'post':
                r = requests.post(self.url, data=json.dumps(eval(self.data)), headers=self.headers)
            elif self.method == 'get':
                r = requests.get(self.url, params=eval(self.data))
            return r
        except:
            print('获取接口访问方式失败')

    @property
    def getRet(self):
        # 获取返回信息ret
        try:
            ret= self.testApi.json()['ret']
            return ret
        except:
            print("获取返回信息ret失败")

    @property
    def getMsg(self):
        # 获取返回信息msg
        try:
            msg= self.testApi.json()['msg']
            return msg
        except:
            print("获取返回信息msg失败")

    @property
    def getData(self):
        # 获取返回信息data
        try:
            data= self.testApi.json()['data']
            return data
        except:
            print("获取返回信息data失败")

    @property
    def getCode(self):
        # 获取返回信息的code数据
        try:
            json_data = self.testApi
            return json_data.status_code
        except:
            print("获取返回信息status_code数据失败")

    @property
    def getJson(self):
        # 获取返回信息的json数据
        try:
            json_data = self.testApi
            return json_data.json()
        except:
            print("获取返回信息json数据失败")
