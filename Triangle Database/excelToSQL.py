import math

import pandas as pd
import sqlite3
import pymysql
import getExcel
import openpyxl


# DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee


class excelToSQL:

    def __init__(self, data):
        self.table = self.create2D(data)
        self.keylist = self.getList(data)
        self.Attribute = """
        CREATE TABLE INFO(
            DBA VARCHAR(100),
            CorpType VARCHAR(10),
            1040 type VARCHAR(20),
            submission date DATE,
            contact number INT,
            fax INT,
            email VARCHAR(50),
            state VARCHAR(50),
            county VARCHAR(50),
            address VARCHAR(50),
            fee INT);"""
        self.Insert = """
        """


    def getList(self, data):
        a = getExcel
        a = a.getExcel(data)
        keyList = list(a.map)
        return keyList


    def create2D(self, data):
        a = getExcel
        a = a.getExcel(data)
        row = len(a.state)
        col = len(a.map)

        array_2d = []
        Key_list = list(a.map)

        for i in range(0, row):
            li = []
            for j in range(0, col):
                result = a.out(Key_list[j])
                if result is not None:
                    li.append(result[i])
                else:
                    li.append(None)
            array_2d.append(li)

        return array_2d


    def insertARow(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='triangle_accounting',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()



if __name__ == '__main__':
    data_frame = pd.read_excel('test.xlsx')
    B = excelToSQL(data_frame)
    array_2d = B.table

    for index in array_2d:
        print(' '.join(map(str, index)))

