import pandas as pd
import pymysql
import getExcelInfo


class excelToSQLforInfo:

    def __init__(self, fileName, name):
        a = getExcelInfo
        self.tableName = name
        self.data_frame = a.getExcelInfo(fileName)
        self.table = self.create2D()
        self.keylist = self.getList()

    def getList(self):
        keyList = list(self.data_frame.map)
        return keyList

    def createTable(self):
        name = self.tableName
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='triangle_accounting',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        cursor = conn.cursor()
        Attribute = """
            CREATE TABLE """ + name + """(
                Client_Business_Name VARCHAR(100),
                Client_Name VARCHAR(20),
                Annual_Service_Fee FLOAT,
                Business_Industry VARCHAR(50),
                Business_Type ENUM('S', 'C'),
                Business_Size INT,
                Contact_Info VARCHAR(20),
                Service_Status ENUM('active', 'closed', 'pending'),
                Google_Drive_Folder_Link VARCHAR(200));"""

        cursor.execute(Attribute)
        conn.commit()

        cursor.close()
        conn.close()

    def deleteTable(self):
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='triangle_accounting',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        cursor = conn.cursor()
        query = "DROP TABLE IF EXISTS {}".format(self.tableName)

        cursor.execute(query)
        conn.commit()

        cursor.close()
        conn.close()

    def create2D(self):
        row = len(self.data_frame.clientbn)
        col = len(self.data_frame.map)

        array_2d = []
        Key_list = list(self.data_frame.map)

        for i in range(0, row):
            li = []
            for j in range(0, col):
                result = self.data_frame.out(Key_list[j])
                if result is not None:
                    li.append(result[i])
                else:
                    li.append(None)
            array_2d.append(li)

        return array_2d

    def insertARow(self):
        #        att = ''
        #        for index in self.keylist:
        #            att = att + index + ',' + ' '
        #        att = att[:-2]
        att = "Client_Business_Name, Client_Name, Annual_Service_Fee, Business_Industry, Business_Type, Business_Size, Contact_Info, Service_Status, Google_Drive_Folder_Link"

        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='triangle_accounting',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()

        # Define the values for the new row
        row = len(self.data_frame.clientbn)

        for index in range(0, row):
            CBN = self.data_frame.clientbn[index]
            CN = self.data_frame.clientName[index]
            fee = self.data_frame.fee[index]
            bi = self.data_frame.bi[index]
            bt = self.data_frame.bt[index]
            bs = self.data_frame.bs[index]
            ci = self.data_frame.ci[index]
            st = self.data_frame.st[index]
            gg = self.data_frame.gg[index]

            # swap the actual name for info, the same as above with create table
            query = "INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)".format(
                self.tableName,
                att)

            # Execute the SQL query with the values
            cursor.execute(query, (
                CBN, CN, fee, bi, bt, bs, ci, st, gg))

        conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    b = excelToSQLforInfo('test2.xlsx', "info")
    b.deleteTable()
    b.createTable()
    b.insertARow()

