# d = ["Olma","olmos","Olam" , "olim", "olmonya","oltin"]
# # 
# def sarala(list):
#     s = []
#     for i in d:
#         if i.lower().startswith("olm") :
#             s.append(i)
#     return s
# print(sarala(d))

import sqlite3
# from tkinter import INSERT
# print(dir(sqlite3))
connect = sqlite3.connect("db40.sqlite3")
# connect = sqlite3.connect("database.db")
cursor = connect.cursor()

# create_table = """CREATE TABLE IF NOT EXISTS users(
# 			 name TEXT,
# 			 surname TEX NULL,
# 			 age  INTEGER DEFAAULT ,
# 			 phone INTEGER NIT NULL
			 
# )"""
# cursor.execute(create_table)
# cursor = connect.cursor()
# connect.close()

insert_into = """ INSERT INTO clents(name,surname,age,phone,reg_daate)
                    VALUES ('abdillo','olimov' ,15,998999002533,354697865485)
            """
cursor = connect.cursor()
cursor.execute(insert_into)
connect.commit()
connect.close()


# from time import*
# hozirgi_vaqt_sekunnta = time()
# print(hozirgi_vaqt_sekunnta)



# create_table = """CREATE TABLE IF NOT EXISTS comments(
# 			user_id INTEGER ,
# 			comment INTEGER TEXT,
#             data  REAL
			 
# )"""

# drop_table = """DROP TABLE comments"""
# cursor = connect.cursor()
# cursor.execute(drop_table)
# # connect.commit()
# connect.close()

create_table = """CREATE TABLE students(
			  name TEXT,
			  last_name TEXT,
			  brinth_date  DATE,
			  aderes TEXT,
			  phone  TEXT,
			  parents_phone  TEXT,
			  parents_info  TEXT,
			  parents_status TEXT,
			  course_name TEXT,
			  status TEXT,
			  active BOOL,
			  dismissal BOOL,
			  discount INTEGER,
			  reg DATE


)"""

# insert_table = """INSERT INTO  students( name,status) VELVES("ABDULLO ,OLIMOV ") """
# cursor = connect.cursor()
# cursor.execute(create_table)
# connect.close()


