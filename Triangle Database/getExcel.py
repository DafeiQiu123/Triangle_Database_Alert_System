import pandas as pd
import sqlite3
import pymysql

#DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee

class getExcel:

    @staticmethod
    def serialize(data_frame):
        attribute = dict()

        att = data_frame.columns
        count = 0
        for index in att:
            attribute[index] = count
            count = count + 1
        return attribute

    @staticmethod
    def getDBA(data_frame, attribute):
        row_num = attribute['DBA']
        DBAlist = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            DBAlist.append(item)

        return DBAlist

    @staticmethod
    def getContactName(data_frame, attribute):
        row_num = attribute['contact name']
        cn = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            cn.append(item)

        return cn

    @staticmethod
    def getPhone(data_frame, attribute):
        row_num = attribute['phone']
        phone = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            phone.append(item)

        return phone

    @staticmethod
    def getContactNumber(data_frame, attribute):
        row_num = attribute['contact number']
        cn = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            cn.append(item)

        return cn

    @staticmethod
    def get1040(data_frame, attribute):
        row_num = attribute['1040 type']
        tenfortytype = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            tenfortytype.append(item)

        return tenfortytype

    @staticmethod
    def getFax(data_frame, attribute):
        row_num = attribute['fax']
        fax = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            fax.append(item)

        return fax

    @staticmethod
    def getEmail(data_frame, attribute):
        row_num = attribute['email']
        email = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            email.append(item)

        return email

    @staticmethod
    def getState(data_frame, attribute):
        row_num = attribute['state']
        state = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            state.append(item)

        return state

    @staticmethod
    def getCounty(data_frame, attribute):
        row_num = attribute['1040 county']
        county = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            county.append(item)

        return county

    @staticmethod
    def getAddress(data_frame, attribute):
        row_num = attribute['address']
        address = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            address.append(item)

        return address

    @staticmethod
    def getFee(data_frame, attribute):
        row_num = attribute['fee']
        fee = []

        for index, row in data_frame.iterrows():
            item = row[row_num]
            fee.append(item)

        return fee



