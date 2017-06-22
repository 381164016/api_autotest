import os
import unittest

import time
import xlwt
import xlrd
from xlutils import copy

from db_fixture import test_data
from db_fixture.read_xls_data import readExcel
from db_fixture.test_api import testApi
import sys

style_ok = xlwt.easyxf(
    "font: name Arial;"
    "pattern: pattern solid, fore_colour green;"
    )
style_wrong = xlwt.easyxf(
    "font: name Arial;"
    "pattern: pattern solid, fore_colour red;"
    )


class testAll(unittest.TestCase):
    def testLoginApi(self):
        '''测试快信接口'''
        p_path = os.path.dirname(os.path.abspath(__file__))  # 文件目录
        path=p_path+'\\test_data.xls'
        # testcase=readExcel(path).getSheetNames()
        testcase=['airPortInfo']
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        file_name = now + "cake.xls"
        #写入测试结果
        # wb=xlwt.Workbook(encoding='ascii')
        self.xl = xlrd.open_workbook(path)
        excel = readExcel(path)
        #每次都复制一份测试用例，以写入测试结果
        wb = copy.copy(self.xl )
        for i in testcase:
            print(' *************测试接口 ：', i, '*********************************')
            my_sheet = excel.getSheet(i)
            name = excel.getName
            send_data = excel.getSendData
            url = excel.getUrl
            method =excel .getMethod
            ret = excel.getRet
            msg = excel.getMsg
            row = excel.getRows
            MYsheet = wb.get_sheet(i)
            for j in range(0, row-1):
                url_full = test_data.test_url + url[j]
                api = testApi(method[j], url_full, send_data[j])
                api_ret = api.getRet
                api_msg = api.getMsg
                api_code=api.getCode
                api_json = api.getJson
                print("msg" ,api_msg)
                print("ret", api_ret)
                api_res=str(api_json)
                if api_ret == ret[j] and api_msg == msg[j]:
                    print('√--------{}、{}:测试成功。status_code为：{}  json数据为:{}'.format(j + 1, name[j], api_code,api_json))
                    try:
                        MYsheet.write(j+1, 7, api_res,style_ok)
                        MYsheet.write(j+1, 8, "通过",style_ok)
                    except:
                        print('写入数据失败')
                        exit()
                else:
                    print('×--------{}、{}:测试失败。status_code为：{}  json数据为:{}'.format(j + 1, name[j], api_code, api_json))
                    MYsheet.write(j+1, 7, api_res,style_wrong)
                    MYsheet.write(j+1, 8, "不通过",style_wrong)
            print("\n")
        #保存测试结果
        wb.save(file_name)



if __name__ == '__main__':
    unittest.main(verbosity=2)


