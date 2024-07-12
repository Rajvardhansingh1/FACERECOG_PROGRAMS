import mysql.connector as s
connector = s.connect(host="localhost",user="root",password="Thehero2004",database="images")

mc = connector.cursor()
sql_query = "CREATE TABLE images (id varchar(10000),student_id int(100), name VARCHAR(255), Age int, Gender varchar(6))"
mc.execute(sql_query)

sql_query = """ALTER TABLE images
    ADD PRIMARY KEY (student_id);"""
mc.execute(sql_query)
