import mysql.connector as s
connector = s.connect(host="localhost",user="root",password="Thehero2004",database="images")

mc = connector.cursor()
sql_query = "CREATE TABLE course (student_id int (100), course_id int PRIMARY KEY, course_name varchar(255), Teacher_name varchar(255))"
mc.execute(sql_query)

#sql_query = """ALTER TABLE personal_info
#    ADD PRIMARY KEY (student_id);"""