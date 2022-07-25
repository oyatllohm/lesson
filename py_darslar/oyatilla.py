# # 1

# def m_sanovchi(satir):
#     m = 0
#     for i in satir:
#         if i == "m" or i == "m":
#             m+=1
#         else:
#             pass
#     return print(m)
# m = "birinchi amali javob"
# m_sanovchi(m)

# # 2
# a =-1
# listt = [11,"kkdkd",22,"kfk",88,"kgfk"]
# for i in listt:
#     a+=1
#     if  type(i) == str :
#         listt.pop(a)
#     else:
#         pass
# print(listt)

# #3
# dictt = {"kalit":"qiymat","mano":"mazmun","yosh":1}
# for i in dictt:
#     dictt[i]=1
# print(dictt)

# #4
# son = 0 
# list_1=[11,88,11,5252,"f",88,[55,66,],["kk",55],65]
# for i in list_1:
#     if type(i) == int:
#         son +=i
#     elif type(i)== list:
#         for j in i:
#             if type(j) == int:
#                 son +=j
#     else:
#         pass
# print(son)

# # 5
# hisob = 0
# d = {"a":15,"b":78,"c":89,"z":"ok","w":45,"t":56}
# for i in d.values():
#     if type(i) == int:
#         hisob+=i
#     else:
#         pass
# print(hisob)

#6
kattaisim = ""
DIKT = {"user1":"fahriddin","user2":"fayhhhhozbek","user3":"oliijojiopij45641631m","user4":"sardor"}
for i in DIKT.values():
    # print(i)
    if len(i)>len(kattaisim):
        kattaisim = i
print(kattaisim)




# #9
# def katta_harif(strr):
#     s = []
#     for i in strr:
#         if i.isupper():
#             s.append(i)
#     return print(s) 
# katta_harif("kjgsd;lgkFKLJSkgkLOLF")


