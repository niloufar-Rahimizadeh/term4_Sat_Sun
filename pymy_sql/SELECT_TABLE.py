import pymysql

con = pymysql.connect(host="localhost", user="root", password="root", database="mt_db_n")

sql = "SELECT * FROM user"



try:
    with con.cursor() as cur:
        cur.execute(sql)
        print(cur.fetchall())
except:
    print("Access Denied")