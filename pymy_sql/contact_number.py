import tkinter as tk
import tkinter.ttk as ttk
import pymysql



def add():
    con = pymysql.connect(host="localhost", user="root", password="root", database="contacts")
    sql = f"INSERT INTO person(name, number) VALUES ('{var1.get()}', '{var2.get()}')"
    try:
        with con.cursor() as cur:
            cur.execute(sql)
            con.commit()
    except:
        print("Access Denied")

def update():
    p_id = int(var3.get())
    con = pymysql.connect(host="localhost", user="root", password="root", database="contacts")
    sql = f"UPDATE person set name='{var1.get()}', number='{var2.get()}' WHERE id={p_id}"
    try:
        with con.cursor() as cur:
            cur.execute(sql)
            con.commit()
    except:
        print("Access Denied")

def select():
    p_id = int(var3.get())
    con = pymysql.connect(host="localhost", user="root", password="root", database="contacts")
    sql = f"SELECT * FROM person WHERE id={p_id}"
    try:
        with con.cursor() as cur:
            cur.execute(sql)
            print(cur.fetchone())
    except:
        print("Access Denied")


def delete():
    p_id = int(var3.get())
    con = pymysql.connect(host="localhost", user="root", password="root", database="contacts")
    sql = f"DELETE FROM person WHERE id={p_id}"
    try:
        with con.cursor() as cur:
            cur.execute(sql)
            con.commit()
    except:
        print("Access Denied")

        
root = tk.Tk()
root.geometry('400x200')
tk.Label(root, text="Name").grid(row=0, column=0)
var1 = tk.StringVar()
tk.Entry(root, textvariable=var1).grid(row=0, column=1)

tk.Label(root, text="Number").grid(row=1, column=0)
var2 = tk.StringVar()
tk.Entry(root, textvariable=var2).grid(row=1, column=1)
tk.Label(root, text="Id").grid(row=2, column=0)
var3 = tk.StringVar()
tk.Entry(root, textvariable=var3).grid(row=2, column=1)

tk.Button(root, text="Add", command=add).grid(row=3, column=0,sticky='we')
tk.Button(root, text="Update", command=update).grid(row=3, column=1,sticky='we')
tk.Button(root, text="Select", command=select).grid(row=3, column=2,sticky='we')
tk.Button(root, text="Delete", command=delete).grid(row=3, column=3,sticky='we')
root.mainloop()

