# from os import curdir

import sqlite3


connect = sqlite3.connect("db40.sqlite3")

crate_table = """CREATE TABLE  IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                surname TEXT NULL,
                phone  INTEGER UNIQUE,
                email  TEXT NULL,
                adres TEXT NULL,
                reg_daate REAL NOT NULL
                


)"""

couser = connect.cursor()
# couser.execute(crate_table)
# couser.close()


# from time import*
# hozirgi_vaqt_sekunnta = time()
# name = "oyatillo"
# surname = "karimberdiev" 
# phone = +998999002533
# emeil = ""
# adres  =  ""
# reg_daate =  hozirgi_vaqt_sekunnta  
# data = 25


from time import*
hozirgi_vaqt_sekunnta = time()
""
name = input("name")
surname = input("surname")
phone =input("phone")
reg_daate = hozirgi_vaqt_sekunnta

insert_into =f""" INSERT INTO users(name,surname,phone,reg_daate)
                    VALUES ('{name}','{surname}' ,{phone},{hozirgi_vaqt_sekunnta})
            """

selet = """SELECT * FROM users """


# crate_table =""" ALTER TABLE users RENAME TO clents"""
crate_table =""" ALTER TABLE users  ADD COLUMN age INTEGER"""
# selekt = """SELECT name FROM usrers"""


try:
    couser.execute(insert_into)
    # r = couser.fetchall()
    # print(r)
except sqlite3.DatabaseError as err:
    print("hato")
else:
    print("susers")

connect.commit()
connect.close()