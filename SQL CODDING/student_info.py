import mysql.connector as s
connector = s.connect(host="localhost",user="root",password="Thehero2004",database="images")

mc = connector.cursor()
sql_query = "CREATE TABLE student_info (student_id int (100), name VARCHAR(255), Roll_No int, DOB date)"
mc.execute(sql_query)

sql_query = """ALTER TABLE student_info
    ADD PRIMARY KEY (student_id);"""
mc.execute(sql_query)
