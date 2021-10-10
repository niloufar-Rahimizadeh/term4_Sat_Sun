import pymysql

con = pymysql.connect(host="localhost", user="root", password="root", database="contacts")

sql = " CREATE TABLE person(id int auto_increment, name varchar(120) not null, number varchar(11) not null, primary key(id))"


try:
    with con.cursor() as cur:
        cur.execute(sql)
except:
    print("Access denied!")