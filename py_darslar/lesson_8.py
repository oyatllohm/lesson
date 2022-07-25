# p = "1234b5c678a"
# for i in p:
#     if  len(p)>=8:print()
#     if  len(p)<=13: print()
#     if i in "a":print()
#     if i in "b":print()
#     if i in "c":print()
       
       
# print("2 xush kelibsiz")
 
                       
        
        


# import string

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)



# a = string.ascii_lowercase
# b = string.ascii_uppercase
# c = "9876543210"
# p = input("parol kiritin")
# if len(p)>8 and len(p)<=13:print()

# else:
#     print("xato")
# for i in p:   
#     if i.isdigit() and i ==  string.ascii_lowercase and i == string.ascii_uppercase:
#         continue
#         print("xush kelibsiz")
#     print(i)


# print(string.ascii_lowercase)


# p = "kkDglkd554"
# k = string.ascii_lowercase
# j = string.ascii_uppercase
# katta = 0
# kichkina = 0
# raqam = 0
# if len(p)>=8 and len(p)<=15:
#     for i in p:
#         if i in string.ascii_uppercase: katta +=1
#         if i in string.ascii_lowercase : kichkina +=1
#         if i in "0123456789":raqam +=1
#     if katta and kichkina and raqam:
#         print("qabul")
#     else:
#         print("qabul emas")
# else:
#     print("parol uzunligi 8 kam 15 kop bolmasin")

# x = 10

# if x >0:
#     print("turu")
# else:
#     print("fold")
# class_9sinif = 64
# talaba9 =31

# s = 100/64
# a = 31*s

# class_10sinif = 67
# talaba10 = 35


# class_10sinif = 56
# talaba10 = 41


# j = 64+67+56
# k = 35+ 41+31
# l = 100/j
# z = l*k
# print(round(z))




# oq = 0
# harakat= 0
# tegdi = 0 
# for i in range(1,200):
#     if tegdi==18:
#         break
#     harakat+=1
#     oq+=3
#     if i % 2 ==0:
#         tegdi+=1
# print("oq",oq)
# print("harakat",harakat)
# print("tegdi",tegdi)


# import random
# print( random.random())
# print( random.randint(1,10))
# print( random.randrange(1,100,10))
# a = string.ascii_lowercase

# kod = ""

# for i in range(6):
#     a = random.randint(1,9)
#     kod += str(a) 
# print(kod)



# y = 0 
# z = 3
# a = random.randint(1,2)
# for i in range(3):
#     x = int(input("son kiritin"))
#     if a == x:
#         print("tabriklaymiz javob", a, "sizning javobingiz",x,"\n tugadi")
        
#         break
#     else:
#         print("topalmadiz javob" )
#         y+=1
#     if a != x and y < z:
#         print("yana imkoniz bor")
   
#     else:
#         print("tugadi",a)

import string
d = string.ascii_uppercase
s = string.ascii_lowercase

parol = "FSJLKfdklj564"
x = 0
y = 0
z = 0
if len(parol)>=8 and len(parol) <=15:
    for i in parol:
        if i in "0123456789":z+=1
        if i in  string.ascii_uppercase : y+=1
        if i in string.ascii_lowercase: x += 1
           
           
            
    if x and y and z:
        print("hush kelib diz")
    else:
        print("hato")
else:
    print("parolingiz 8 > < 15 bolsin")