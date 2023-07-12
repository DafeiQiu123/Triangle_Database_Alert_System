import pandas as pd
import pymysql
import getExcel


# DBA	CorpType	1040 type	submission date	contact name	contact number	phone	fax	email	state	county	address	fee
class excelToSQL:

    def __init__(self, data):
        a = getExcel
        self.data_frame = a.getExcel(data)
        self.table = self.create2D()
        self.keylist = self.getList()
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

    def getList(self):
        keyList = list(self.data_frame.map)
        return keyList

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
        att = ''
        for index in self.keylist:
            att = att + index + ',' + ' '
        att = att[:-2]

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
            cursor.execute("INSERT INTO INFO (" + att + ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                DBA, CorpType, tenFortyType, subDate, conName, conNum, phone, fax, email, state, county, address, fee))

            conn.commit()

            cursor.close()
            conn.close()


if __name__ == '__main__':
    data_frame = pd.read_excel('test.xlsx')
    B = excelToSQL(data_frame)
    array_2d = B.table

    for index in array_2d:
        print(' '.join(map(str, index)))

    att = ''
    for index in B.keylist:
        att = att + index + ',' + ' '
    att = att[:-2]
    print(att)
