import pymysql

con = pymysql.connect(host="localhost", user="root", password="root", database="mt_db_n")

sql = "UPDATE user set name='Amir' where id=1"

try:
    with con.cursor() as cur:
        cur.execute(sql)
        con.commit()
except:
    print("Access Denied")