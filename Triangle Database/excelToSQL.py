import pandas as pd
import sqlite3
import pymysql
import getExcel
import openpyxl


# DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee


class excelToSQL:

    def createAttribute(self):
        createAttribute = """
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

        insertAllRows = """
        """


if __name__ == '__main__':
    data_frame = pd.read_excel('test.xlsx')
    a = getExcel
    a = a.getExcel(data_frame)
    row = len(a.state)
    col = len(a.map)

    array_2d = []
    for _ in range(row):
        row = [0] * col
        array_2d.append(row)

    for i in range(len(array_2d)):
        for j in range(len(array_2d[i])):
            element = array_2d[i][j]


    Key_list = list(a.map)

    print(Key_list)
    print(a.map)
