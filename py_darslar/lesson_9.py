import random
yshirin_raqam = random.randint(1,15)
for i  in range(3):
    son = int (input("son kiritin"))
    if son == yshirin_raqam:
        print("toptingiz")
        break
    else:
        print("topolmadiz")

y = int (input("kichika son"))
x = int (input("katta son"))


for i in range(y,x+1):
    if x > y :
        print(i)
        

f = "pyt7h5o582 ja1v2a 44h2p"
a = 0
summa = 0 

for i in f :
    if i.isdigit():
        i = int (i) 

        summa +=i
       
print(summa)
print(f)

import random

a = ["olma", "onor", "anjir", "uzum"]

list_1 = ["qovun", "torvuz", "handalak", "obi navvot"]
list_2 = ["shirin ", "achchiq ", "mazzalik", "be maza"]
list_3 = ["gozal ", "chiroylik ", "be takror", "keraksiz"]
x = random.choice(a)
# print(x)
for i in range(1,501):
    soz = input("soz kiritin")
    if soz == "stop":
        break
    
    s = random.choice(list_1)
    d = random.choice(list_2)
    f = random.choice(list_3)
    print( "siz",s ,d,f,"ekansiz" )


a = 28
b = 0
i = 0
while i<a:
    i +=3

    b +=1
    if i>=a:
        break
    i -=2

print(b)

a = 0
b = 100
while b > a:
    a += 1
    print(a)



rice = 1000//10
oil = 300//10
carrot =1000//10
meta = 1000//10
onion = 500//10

guruch = 25000//10 # som
gosht = 70000//10  # som
yog = 7000//10   # som
sabzi = 3000//10  # som
piyoz = 2000//10  # som

mahsulot_narhi = guruch + yog + sabzi + gosht + piyoz
foyda = mahsulot_narhi/10*12

zakaz = int(input("odam soniga yarasha  osh zakaz  qilin"))

print("guruch",rice*zakaz,"gram")
print("yog'",oil*zakaz,"gram")
print("sabzi",carrot*zakaz,"gram")
print("gosht",meta*zakaz,"gram")
print("piyoz",onion*zakaz,"gram")
print("osh harajati",mahsulot_narhi*zakaz)
print("hizmat 20%")
print(foyda*zakaz , "som")