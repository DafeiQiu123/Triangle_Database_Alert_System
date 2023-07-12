import pandas as pd
from pandas import Timestamp
import math
class getExcelInfo:
    #Client business name	Client name	Annual service fee	Business industry	Business Type	Business size	Contact info	Service status	Google drive folder link

    def __init__(self, fileName):
        data_frame = pd.read_excel(fileName, sheet_name= 2)
        self.data_frame = data_frame
        self.map = self.serialize(data_frame)
        self.clientbn = self.getCBN(data_frame)
        self.clientName = self.getClientName(data_frame)
        self.fee = self.getAnnualServiceFee(data_frame)
        self.bi = self.getBusinessIndustry(data_frame)
        self.bt = self.getBusinessType(data_frame)
        self.bs = self.getBusinessIndustry(data_frame)
        self.ci = self.getBusinessType(data_frame)
        self.st = self.getServiceStatus(data_frame)
        self.gg = self.getGoogleDrive(data_frame)

    def serialize(self, data_frame):
        attribute = dict()

        att = data_frame.columns
        count = 0
        for index in att:
            attribute[index] = count
            count = count + 1
        return attribute

    def getCBN(self, data_frame):
        DBAlist = []

        for index, row in data_frame.iterrows():
            item = row['Client business name']
            item = self.toZero(item)
            DBAlist.append(item)

        return DBAlist

    def getClientName(self, data_frame):
        state = []

        for index, row in data_frame.iterrows():
            item = row['Client name']
            item = self.toZero(item)
            state.append(item)

        return state

    def getAnnualServiceFee(self, data_frame):
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Annual service fee']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getBusinessIndustry(self, data_frame):
        state = []

        for index, row in data_frame.iterrows():
            item = row['Business industry']
            item = self.toZero(item)
            state.append(item)

        return state

    def getBusinessType(self, data_frame):
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Business Type']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getBusinessSize(self, data_frame):
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Business size']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getContactInfo(self, data_frame):
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Contact info']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getServiceStatus(self, data_frame):
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Service status']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def getGoogleDrive(self, data_frame):
        itemList = []

        for index, row in data_frame.iterrows():
            item = row['Google drive folder link']
            item = self.toZero(item)
            itemList.append(item)

        return itemList

    def out(self, str):
        if str == 'Client business name':
            return self.clientbn
        elif str == 'Client name':
            return self.clientName
        elif str == 'Annual service fee':
            return self.fee
        elif str == 'Business industry':
            return self.bi
        elif str == 'Business Type':
            return self.bt
        elif str == 'Business size':
            return self.bs
        elif str == 'Contact info':
            return self.ci
        elif str == 'Service status':
            return self.st
        elif str == 'Google drive folder link':
            return self.gg

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
    a = getExcelInfo('test2.xlsx')
    print(list(a.map))

