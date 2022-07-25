
import string
import random
pasword = "22o"
a  = 0 
while True:
    a+=1
    for i in range(1,4):
        if i == 1 or i == 2 :
            x = random.randint(0,9)
            pasword+=str(x)
        else:
            s = random.choice(string.ascii_lowercase)
            pasword += s
            # print(pasword)
    if x == pasword:
        break
    print(a)
    # parol topish



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
# uzun soz topish




s = "parol1254"
shifir = ""
for i in s :
    shifir += chr(ord(i)+5)

print(shifir)
# parol shifirlash



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
#parol shifirlash

a = 0
d = [15,8,[89,78],"48","ok",[78,"a",98],"power",89,77,[45,89]]
for i in d :
    if type(i)==int:
        a+=i
    elif type(i) == list:
        for j in i :
            if type(j)==int:
                a+=j
print(a)
# barcha raqamlarni jamlovchi cod



a = "we recommend reading this tutorial, in the sequence listed in the menu."
m = 0
indeks = 0
while indeks <len(a):
    x = a[indeks]
    indeks+=1
    if x == "m":
        m += 1
print(m,a)
#"m harfini sanovchi cod"



import random
def generator_random_list(limit):
    l = []
    while True:
        if len(l)==limit:
            break 
        r = random.randint(0,100)
        if r not in l:
            l.append(r)
    return l 
s=generator_random_list(10)
print(s)
# list qaytaradi 




def jamlash(a,b,c):
    if type(a) == list and type(b)== list and type(c)==list:
        return a + b + c
    else:
        return "a b c list bolishi keraks"

list_1 = ["ok","py","non"]
list_2 = [ 15,55,66,66,]
list_3 = [[5],["python"],[88]]

s = jamlash(list_1,list_2,list_3)
print(s)

# listlarni jamlobchi funciya




def ohshahs(word,orginalword):
    x=len(word)
    y=len(orginalword)
    yuz = 100
    foiz = 0
    hisob = -1
    if x == y:
        for i in word:
            hisob+=1
            if i == orginalword[hisob]:
                foiz+=1
    else: 
        return print("satirlardagi hariflarini soni ten emas")
    print(f"satirlar {yuz/x*foiz} % ohshash {word}  {orginalword} ")
ohshahs("aandajon","andijon")
# satirlarni ohshsahini tekshiradi




d=[4,5,1,7,12,2,8,3,20,6,9,10]
s = []
for i in range(min(d) ,max(d)+1):
    if i in d:
        # print(i)
        s.append(i)
print(s)
#  listni tahlovchi for



d=[4,5,1,7,12,2,8,3,6,9,10]
n = len(d)
print(n)
for i in range(n-1):
    for j in range(n-i-1):
        if d[j] > d[j+1]:
            d [j] ,d [j+1] = d[j+1]  ,d[j]
print(d)
#  listni tahlovchi for

