import pandas as pd
import pymysql
import getExcelSchedule


# DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee
class excelToSQL:

    def __init__(self, data, name):
        a = getExcelSchedule
        self.tableName = name
        self.data_frame = a.getExcelSchedule(data)
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
                DBA VARCHAR(100),
                State VARCHAR(10),
                Pay_Roll VARCHAR(20),
                941D VARCHAR(2),
                SALES VARCHAR(50),
                County_Tax VARCHAR(20),
                941F VARCHAR(2),
                STATE_WITHHOLDING VARCHAR(20),
                STATE_UI VARCHAR(2),
                940Form VARCHAR(2),
                BOOKKEEPING VARCHAR(50),
                Accountant VARCHAR(50));"""

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
        row = len(self.data_frame.state)
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
        att = "DBA, State, Pay_Roll, 941D, SALES, County_Tax, 941F, STATE_withholding, STATE_UI, 940Form, BOOKKEEPING, Accountant"

        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='triangle_accounting',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()

        # Define the values for the new row
        row = len(self.data_frame.state)

        for index in range(0, row):
            DBA = self.data_frame.DBA[index]
            State = self.data_frame.state[index]
            pr = self.data_frame.payroll[index]
            NFOD = self.data_frame.NFOD[index]
            sales = self.data_frame.SALES[index]
            countyTx = self.data_frame.countyTax[index]
            NFOF = self.data_frame.NFOF[index]
            sw = self.data_frame.sw[index]
            su = self.data_frame.su[index]
            NFO = self.data_frame.NFO[index]
            book = self.data_frame.bk[index]
            acc = self.data_frame.acc[index]

            # swap the actual name for info, the same as above with create table
            query = "INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(
                self.tableName,
                att)

            # Execute the SQL query with the values
            cursor.execute(query, (
                DBA, State, pr, NFOD, sales, countyTx, NFOF, sw, su, NFO, book, acc))

        conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    data_frame = pd.read_excel('test2.xlsx')
    b = excelToSQL(data_frame, "info")
    #b.deleteTable()
    #b.createTable()
    #b.insertARow()

