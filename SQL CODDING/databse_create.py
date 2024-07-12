import mysql.connector as s
connector = s.connect(host="localhost",user="root",passwd="Thehero2004")

mc = connector.cursor()
mc.execute("CREATE database images")