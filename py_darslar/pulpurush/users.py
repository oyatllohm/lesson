def fayil(**kwargs):
    """ funcsiuani chaqiryatib dict qiymat qoshishimiz mumkun 
    masalan talabanin malumotlari bu talaba kam tamillangan """
    fayl= open("users.txt","r")
    son = len(fayl.read().split("."))
    print(fayl.read())
    j = son-1
    fayl = open("users.txt","a")
    while True:
        j +=1
        ism = input("ismizni kiritin yo  stop")
        if ism == "stop":
            break
        familya = input("familyangizni  kiritin")
        tel = input("tel nomerizni kiritin")
        fayl.write(f"{j} ")
        fayl.write(f"{ism}  ")
        fayl.write(f"{familya}  ")
        fayl.write(f"{kwargs} ")
        fayl.write(f"{tel} .\n ")
    fayl.close()
    return kwargs
fayil()


# f = open("users.txt","a") # w  write  yozish  
#                         #  r  read   o'qish
#                         #  a  append   davomiga yozish
# f.write("717324646\n")
# # result = f.read()

# # print(result)
# f.close()

# def check_id(user_id):
#     f = open("users.txt","r")
#     users_list = f.readlines()
#     print(users_list)
#     check_user = False
#     for i in users_list:
#         s = i.strip()
#         if s == user_id:
#             check_user = True
#             break

#     if not check_user:
#         f = open("users.txt","a")
#         f.write(f"{user_id}\n")
#         f.close()   
#     return check_user
# check_id("717324646")    


# f = open("xujjat.docx","rb")# w r x a b rb   w+ r+

# with open("users.txt") as f:
#     print(f.read() )
# print(4)

import os
# print(os.__doc__)

abs_path = os.getcwdb()

# with open(f"{abs_path}\\andijon.txt","r+")as f:
    # print(f.read)
# print(os.listdir() )# barcha fayiillarni korsatadi
# print(os.mkdir("papka") )# papka ochadi
# print(os.rmdir("papka") )# papka ochiradi

# f = open("xujjat.docx","rb")
# if not os.path.exists("xujjat.docx"): # agar hujjat bolmasa ochadi
#     f = open("xujjat.docx","w")

import json 

dikt = {

    "olma":{"priche":5000,"kg":86},
    "banan":{"priche":15000,"kg":60},
    "mandarin":{"priche":35000,"kg":55},
    "uzum":{"priche":25000,"kg":16}
}
f = open("baza.json")
json.dump(dikt,f)
res = json.load(f)
res["kivi"]={"priche":25000,"kg":16}


# users_list =["muborak","marziya"]
# f = open("baza.json","r")
# json.dump(users_list,f)
# a = json.load("baza.json")
