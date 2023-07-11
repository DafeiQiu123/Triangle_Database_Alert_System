import pandas as pd
import sqlite3
import pymysql

#DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee

class getExcel:

    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.map = self.serialize(data_frame)
        self.DBA = self.getDBA(self.data_frame, self.map)
        self.CorpType = self.getCorp(self.data_frame, self.map)
        self.ConName = self.getContactName(self.data_frame, self.map)
        self.ConNum = self.getContactNumber(self.data_frame, self.map)
        self.phone = self.getPhone(self.data_frame, self.map)
        self.fax = self.getFax(self.data_frame, self.map)
        self.email = self.getEmail(self.data_frame, self.map)
        self.state = self.getState(self.data_frame, self.map)
        self.county = self.getCounty(self.data_frame, self.map)
        self.address = self.getAddress(self.data_frame, self.map)
        self.fee = self.getFee(self.data_frame,self.map)



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
            item = row[row_num]
            DBAlist.append(item)

        return DBAlist

    def getCorp(self, data_frame, attribute):
        row_num = attribute['CorpType']
        Corp = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            Corp.append(item)

        return Corp

    def getContactName(self, data_frame, attribute):
        row_num = attribute['contact name']
        cn = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            cn.append(item)

        return cn

    def getPhone(self, data_frame, attribute):
        row_num = attribute['phone']
        phone = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            phone.append(item)

        return phone

    def getContactNumber(self, data_frame, attribute):
        row_num = attribute['contact number']
        cn = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            cn.append(item)

        return cn


    def get1040(self, data_frame, attribute):
        row_num = attribute['1040 type']
        tenfortytype = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            tenfortytype.append(item)

        return tenfortytype

    def getFax(self, data_frame, attribute):
        row_num = attribute['fax']
        fax = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            fax.append(item)

        return fax


    def getEmail(self, data_frame, attribute):
        row_num = attribute['email']
        email = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            email.append(item)

        return email

    def getState(self, data_frame, attribute):
        row_num = attribute['state']
        state = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            state.append(item)

        return state


    def getCounty(self, data_frame, attribute):
        row_num = attribute['county']
        county = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            county.append(item)

        return county


    def getAddress(self, data_frame, attribute):
        row_num = attribute['address']
        address = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            address.append(item)

        return address

    def getFee(self, data_frame, attribute):
        row_num = attribute['fee']
        fee = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            fee.append(item)

        return fee


if __name__ == '__main__':
    data_frame = pd.read_excel('test.xlsx')
    a = getExcel(data_frame)
    print(a.DBA)
