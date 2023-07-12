import pandas as pd
import pymysql
import getExcel


# DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee
class excelToSQL:

    def __init__(self, data, name):
        a = getExcel
        self.tableName = name
        self.data_frame = a.getExcel(data)
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
                CorpType VARCHAR(10),
                1040_type VARCHAR(20),
                submission_date DATE,
                contact_name VARCHAR(50),
                contact_number VARCHAR(50),
                phone VARCHAR(50),
                fax VARCHAR(20),
                email VARCHAR(50),
                state VARCHAR(50),
                county VARCHAR(50),
                address VARCHAR(50),
                fee INT);"""

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
        att = "DBA, CorpType, 1040_type, submission_date, contact_name, contact_number, phone, fax, email, state, county, address, fee"

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
            CorpType = self.data_frame.CorpType[index]
            tenFortyType = self.data_frame.tenFortyType[index]
            subDate = self.data_frame.subDate[index]
            conName = self.data_frame.ConName[index]
            conNum = self.data_frame.ConNum[index]
            phone = self.data_frame.phone[index]
            fax = self.data_frame.fax[index]
            email = self.data_frame.email[index]
            state = self.data_frame.state[index]
            county = self.data_frame.county[index]
            address = self.data_frame.address[index]
            fee = self.data_frame.fee[index]

            # swap the actual name for info, the same as above with create table
            query = "INSERT INTO {} ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(
                self.tableName,
                att)

            # Execute the SQL query with the values
            cursor.execute(query, (
                DBA, CorpType, tenFortyType, subDate, conName, conNum, phone, fax, email, state, county, address, fee))

        conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    data_frame = pd.read_excel('test.xlsx')
    b = excelToSQL(data_frame, "info")
    #b.deleteTable()
    b.createTable()
    b.insertARow()

