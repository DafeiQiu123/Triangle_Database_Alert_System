import math
import pandas as pd
from pandas import Timestamp


# DBA (LEGAL) (client name)	State	Pay Roll	941D	SALES	County Tax	941F	STATE withholding	STATE UI	940	BOOKKEEPING	Accountant

class getExcelSchedule:

    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.map = self.serialize(data_frame)
        self.DBA = self.getDBA(self.data_frame, self.map)
        self.state = self.getState(self.data_frame, self.map)
        self.payroll = self.getPayroll(self.data_frame, self.map)
        self.NFOD = self.get941D(self.data_frame, self.map)
        self.SALES = self.getSales(self.data_frame, self.map)
        self.countyTax = self.getCountyTax(self.data_frame, self.map)
        self.NFOF = self.get941F(self.data_frame, self.map)
        self.sw = self.getStateWithHolding(self.data_frame, self.map)
        self.su = self.getStateUI(self.data_frame, self.map)
        self.NFO = self.get940(self.data_frame, self.map)
        self.bk = self.getBookkeeping(self.data_frame, self.map)
        self.acc = self.getAccountant(self.data_frame, self.map)

    def serialize(self, data_frame):
        attribute = dict()

        att = data_frame.columns
        count = 0
        for index in att:
            attribute[index] = count
            count = count + 1
        return attribute

    def getDBA(self, data_frame, attribute):
        row_num = attribute['DBA']
        DBAlist = []

        for index, row in data_frame.iterrows():
            item = row['DBA']
            item = self.toZero(item)
            DBAlist.append(item)

        return DBAlist

    def getState(self, data_frame, attribute):
        row_num = attribute['State']
        state = []

        for index, row in data_frame.iterrows():
            item = row['State']
            item = self.toZero(item)
            state.append(item)

        return state

    def getPayroll(self, data_frame, attribute):
        row_num = attribute['Pay Roll']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Pay Roll']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def get941D(self, data_frame, attribute):
        row_num = attribute['941D']
        state = []

        for index, row in data_frame.iterrows():
            item = row['941D']
            item = self.toZero(item)
            state.append(item)

        return state

    def getSales(self, data_frame, attribute):
        row_num = attribute['SALES']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['SALES']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getCountyTax(self, data_frame, attribute):
        row_num = attribute['County Tax']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['County Tax']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def get941F(self, data_frame, attribute):
        row_num = attribute['941F']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['941F']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getStateWithHolding(self, data_frame, attribute):
        row_num = attribute['STATE withholding']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['STATE withholding']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getStateUI(self, data_frame, attribute):
        row_num = attribute['STATE UI']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['STATE UI']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def get940(self, data_frame, attribute):
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['940Form']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getBookkeeping(self, data_frame, attribute):
        row_num = attribute['BOOKKEEPING']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['BOOKKEEPING']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getAccountant(self, data_frame, attribute):
        row_num = attribute['Accountant']
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Accountant']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def out(self, str):
        if str == 'DBA':
            return self.DBA
        elif str == 'State':
            return self.state
        elif str == 'Pay Roll':
            return self.payroll
        elif str == '941D':
            return self.NFOD
        elif str == 'SALES':
            return self.countyTax
        elif str == '941F':
            return self.NFOF
        elif str == 'STATE withholding':
            return self.sw
        elif str == 'STATE UI':
            return self.su
        elif str == '940Form':
            return self.NFO
        elif str == 'BOOKKEEPING':
            return self.bk
        elif str == 'Accountant':
            return self.acc

    def toZero(self, item):
        if isinstance(item, Timestamp):
            if item is None:
                return 'empty'
        if isinstance(item, str):
            if item == "":
                return 'empty'
        if isinstance(item, float):
            if math.isnan(item):
                return 'empty'

        return item

if __name__ == '__main__':
    data_frame = pd.read_excel('test2.xlsx')
    a = getExcelSchedule(data_frame)
    print(list(a.map))
