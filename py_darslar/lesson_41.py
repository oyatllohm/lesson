from ensurepip import version
import sqlite3
connect = sqlite3.connect("db41.sqlite3")
from time import time ,ctime
hozirgi_vaqt_sekunnta = time()

crate_table = """CREATE TABLE  IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                reg_daate REAL NOT NULL
                
)"""

crate_table = """CREATE TABLE  IF NOT EXISTS users1(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                price    INTEGER NOT NULL,
                catigorye INTEGER NOT NULL,
                reg_daate REAL NOT NULL
                


)"""
inser_table = f"""INSERT INTO users 
    (name,reg_daate) 
    VALUES ("madem",{hozirgi_vaqt_sekunnta})"""

inser_table = f"""INSERT INTO users1 
    (name,price , catigorye,reg_daate) 
    VALUES ("usdQIMMATI",500,2,{hozirgi_vaqt_sekunnta})"""

crate_table =""" ALTER TABLE users1  ADD COLUMN quantity INTEGER NOT NOLL DEFAULT 0"""
selet = f"""SELECT * FROM  users1  """
# selet = f"""SELECT * FROM  users1  WHERE price > 47  """
# selet = f"""SELECT * FROM  users1  WHERE catigorye = 2 """
# selet = f"""SELECT * FROM  users1 WHERE catigorye=2  ORDER BY price  DESC   """
# selet = f"""SELECT * FROM  users1  ORDER BY price  DESC   """
couser = connect.cursor()
# couser.execute(selet)
r = couser.fetchall()



def insert_baza(table,name,narh,category):
    """bu punsiyani ishlatishdan oldin time  modilini  
       va sqlite3 impirt qivolin
       bu funsiya sqlite3 bazaga tavar qoshadi """
    hozirgi_vaqt_sekunnta = time()
    couser = connect.cursor()
    inser_into = f"""INSERT INTO {table}
        (name,price , catigorye,reg_daate) 
        VALUES ("{name}",{narh},{category},{hozirgi_vaqt_sekunnta})"""
    couser.execute(inser_into)
    connect.commit()
    couser.close()
# insert_baza("users1","x",250,1,)

def fayilga_yozish(table,fayil):
    tablitsa_usunlari  = "N#  NOMI     NARXI    KATEGORIYASI    SANASI \n"
    selet = f"""SELECT * FROM  {table} ORDER BY price  DESC  """
    couser.execute(selet)
    r = couser.fetchall()
    matin = ""
    for i in range(len(r)):
        id = r[i][0]
        name = r[i] [1]
        narh = r[i][2]
        catigorya = r[i][3]
        data = ctime(r[i][4]) 
        
        matin+=f"{id}   {name}   {narh}    {catigorya}    {data} \n"
    f = open(fayil,"a")
    f.write(tablitsa_usunlari) 
    f.write(matin)
    f.close()
# fayilga_yozish("users1","vazifa.txt")

# print(r[i] [0], r[i] [1] , r[i] [2] ,r[i] [3] ,ctime(r[i] [4]))
# print(r[0][-1])
# f =r [0][0]


# print(ctime(r[0][-1]))

# N# NOMI         NARXI    KATEGORIYASI    SANASI
# selet = f"""SELECT MIN(price) FROM  users1  WHERE  price ={f} """
# couser.execute(selet)
# v = couser.fetchall()
# # print(v)
connect.commit()
connect.close()
    