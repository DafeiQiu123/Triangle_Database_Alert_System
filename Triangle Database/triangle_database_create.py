import pymysql.cursors
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='triangle_accounting',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
def create_database_structure():
    cursor = conn.cursor()
    create_customer = """
CREATE TABLE customer (
  customer_EIN INT PRIMARY KEY,
  customer_name VARCHAR(100),
  city VARCHAR(50),
  state VARCHAR(50),
  customer_industry VARCHAR(100),
  customer_type ENUM('sole proprietorships', 'partnerships', 'limited liability companies', 'corporations', 'individual'),
  employee_num INT,
  gross_sale INT,
  annual_service_fee DECIMAL(10, 2),
  service_status ENUM('active', 'closed', 'pending'),
  google_drive_folder_url VARCHAR(255),
  service_1120 DATE,
  service_941_biweekly DATE,
  service_941_nonbiweekly DATE,
  service_business_tax DATE,
  service_1040 DATE
);
"""
    create_staff = """
CREATE TABLE staff(
  staff_name VARCHAR(100) PRIMARY KEY,
  staff_password VARCHAR(20)
);
"""
    create_incharge_relation = """
CREATE TABLE incharge(
   staff_name VARCHAR(100),
   customer_EIN INT,
   primary key (staff_name, customer_EIN),
   foreign key (staff_name) references staff (staff_name) on delete cascade on update cascade,
   foreign key (customer_EIN) references customer (customer_EIN) on delete cascade on update cascade
);
"""
    cursor.execute(create_customer)
    conn.commit()
    cursor.execute(create_staff)
    conn.commit()
    cursor.execute(create_incharge_relation)
    cursor.close()

if __name__ == "__main__":
    create_database_structure()