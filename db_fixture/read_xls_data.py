import time
from  xlutils import copy

import xlrd
import xlwt

class readExcel(object):
    def __init__(self, path):
        self.path = path
        self.xl=xlrd.open_workbook(self.path)

    def getSheet(self,i):
        # 获取索引
        self.sheet=self.xl.sheet_by_name(i)
        return self.sheet


    def getSheetNames(self):
        # 获取sheet列表
        sheets = self.xl.sheet_names()
        return sheets

    def setResult(self,sheet_name,row,col,data,style,file_name):
        #写入测试结果
        # wb=xlwt.Workbook(encoding='ascii')
        wb=copy.copy(self.xl)

        MYsheet = wb.get_sheet(sheet_name)
        try:
            my_data=str(data)
            MYsheet.write(row,col,my_data)
            print("写入",my_data,row,col)
            # MYsheet.put_cell(row,col,1,data,0)
            wb.save(file_name)
        except:

            print('写入数据失败')
            exit()
    @property
    def getRows(self):
        # 获取行数
        row = self.sheet.nrows
        return row

    @property
    def getCol(self):
        # 获取列数
        col = self.sheet.ncols
        return col

    # 以下是分别获取每一列的数值
    @property
    def getName(self):
        TestName = []
        for i in range(1, self.getRows):
            # print(self.getSheet.cell_value(i, 0))
            TestName.append(self.sheet.cell_value(i, 0))
        return TestName

    @property
    def getSendData(self):
        SendData = []
        for i in range(1, self.getRows):
            SendData.append(self.sheet.cell_value(i, 1))
        return SendData

    @property
    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows):
            TestUrl.append(self.sheet.cell_value(i, 2))
        return TestUrl

    @property
    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.sheet.cell_value(i, 3))
        return TestMethod

    @property
    def getRet(self):
        TestRet = []
        for i in range(1, self.getRows):
            TestRet.append(self.sheet.cell_value(i, 4))
        return TestRet
    @property
    def getMsg(self):
        TestMsg = []
        for i in range(1, self.getRows):
            TestMsg.append(self.sheet.cell_value(i, 5))
        return TestMsg
    @property
    def getData(self):
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.sheet.cell_value(i, 6))
        return TestData

