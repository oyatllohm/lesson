print()
list1 = [11,55,54,99,77,33,54,47]
s = len(list1)
d = 0 
for i in list1 :
    d += i
f = d // s 
print("list1 ozgaruchidagi sonlar ortacha yigindisi ",f)
print()


    

uzun_soz = ""
max_ = 0
a = ["php","python","java","go","javasikiript"]
for i in a :
    a = len(i)
    if a > max_ :
        max_= a
        uzun_soz = i
print(max_ ,"harif bilan ")
print(uzun_soz,"uzun soz")
print()
    

kalta_soz = ""
min_ = 999999
a = ["php","python","java","go","javasikiript"]
for i in a :
    a = len(i)
    if a < min_ :
        min_= a
        kalta_soz = i
print(min_,"harif bilan ")
print(kalta_soz,"qisqa soz")
print()



chempion = "" 
boho = 0   
musobaqa =["89 sobirjon", "83odiljon","85 ozodbek", "80 ahmadulloh" ,"82oyatulloh"]

for i in musobaqa:
    if i [:2].isdigit():
        pass
    if int (i[:2])>boho:
        boho = int(i[:2])
        chempion=i

    
print(boho," bal bilan  g'olibimiz")
print(chempion)



a = 1  # asosi aylanib kopayadigan  raqam 
d = 1  # 1 wihle aylantiruchi 
s = 8  # 1 wihle tohtatuchi

g = 0  # 2 wihle aylantiruchi
h = 8  # 2 wihle tohtatuchi

while s >=d :
    if g == 9 :
        g = 0
    if a == 10:
        a -= 9
    d+=1
    print("")
    print(d ,"karra")
    while g <= h :
        a+=1 
        g +=1
        x = a*d
        print( d,"*",a , "=", x )



s = "parol1254"
shifir = ""
for i in s :
    shifir += chr(ord(i)+5)

print(shifir)


a =""
for i in shifir:
      a += chr(ord(i)-5)
print(a)


import hashlib


pasword = b"tehnopark2021"
md5 = hashlib.md5()
md5.update(pasword)
print(md5.hexdigest())

p = input(b"parol kiritin")
d5 = hashlib.md5()
d5.update(bytes(p, encoding = "cp1254"))
if md5.hexdigest() == d5.hexdigest():
    print("qabul qilindi")
print(p)



x = int ("45")
c = 45
y = float("12.5")
print(y)
list1 = [11,55,54,99,77,33,54,47]
d = max(list1)
d = min(list1)
d = sum(list1)
d = divmod(15,2)
print(d)

s = round(10.3)
print(s)
import math
s = 10.3
p = math.ceil(s)
print(p)
a = 10.2
p = math.floor(a)
print(p)

s =100
x = 5.9
p = math.sqrt(s)
print(p)
print((x).is_integer())
c = 0
x = "assalom".count("s")
x = "assalom".replace("s","$")

print(x)



  
    
    
        

