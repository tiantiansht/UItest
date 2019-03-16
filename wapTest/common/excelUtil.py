# coding:utf-8
import xlrd
class excelUtil():
    def __init__(self):
        self.file_path = "G:/pycharm/PycharmProjects/wapTest/common/data.xls"
        self.data = xlrd.open_workbook(self.file_path)
        self.table = self.data.sheet_by_index(0)
        self.nrows = self.table.nrows
        self.cols = self.table.ncols
        self.key = self.table.row_values(0)

    def getData(self):
        r = []
        j = 1
        for i in range(self.nrows-1):
            s = {}
            values = self.table.row_values(j)
            for x in range(self.cols):
                s[self.key[x]] = values[x]
            r.append(s)
            j+=1
        return r

if __name__ == "__main__":
    excelUtil = excelUtil()
    print(excelUtil.getData())