import mysql.connector as s
connector = s.connect(host="localhost",user="root",password="Thehero2004",database="images")

mc = connector.cursor()
sql_query = "CREATE TABLE personal_info (student_id int (100), gender varchar(10),Address varchar(255), Father_name varchar(255), mother_name varchar(255), father_income int, mother_income int, father_dob date, mother_dob date)"
mc.execute(sql_query)

sql_query = """ALTER TABLE personal_info
    ADD PRIMARY KEY (student_id);"""
mc.execute(sql_query)
