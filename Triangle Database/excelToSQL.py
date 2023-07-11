import math

import pandas as pd
import sqlite3
import pymysql
import getExcel
import openpyxl


# DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee


class excelToSQL:

    @staticmethod
    def create2D(data):
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

    B = excelToSQL()

    array_2d = B.create2D(data_frame)

    for index in array_2d:
        print(' '.join(map(str, index)))

