belgi = 0
nazorat = 3
habar = input("habar kiritin # 3 kop bolmasin")

for i in habar:
    if i =="#":belgi +=1 
if belgi > nazorat:
    print("xabar ichida # 3 kop")
else:
    print("xabar qabul qilindi")
print(belgi)



summa = 0
nazorat = "*****"
for i in nazorat:
    som = int(input("som kiritin"))
    if i == "*":summa+=som
print("jami",summa)


tel_nomer = input(" tel_nomer kiritin ")

if len(tel_nomer)==13:
    if tel_nomer[0] in "+"and tel_nomer[1:4]in"998":
        if tel_nomer[1:].isdigit():
            print("qabul qilindi")
        else:
            print("nomerda hatolik bor")
    else:
        print("nomerda hatolik bor")
else:
    print("nomer hatoliko")

a = input("a soz")
b = input("b soz")
c = input("c soz")

s = len(a)
n = len(b)
v = len(c)
if s > n and s > v:
    print("a katta ",a)
elif n > s and n > v:
    print("b katta",b)
elif v > n and v >s:
    print("c katta",v)
else:
    print("sozlarda tenlik bor")

s = ord("k")
print(s)


d = chr(107)
print(d)

x = input("xarif kiritin a - z ")
s = (ord(x)-97)
print(s) 
x = int(input("raqam kiritin 1 dan n gacha "))
s = chr(x)

print(s)


d= ("qandaydu^rot(e)x")
a = 1
for i in d:
    if i =="^":
        print("^")
        break
    
    a +=1
print(a)



c = 0
for i in [1,55,88,66,77,22,77,2,6,]:
    if i % 2 == 0:
        print(i)
    else:
        continue
    c += 1
print("sikil",c,"aylandi")


langth = 28
day = 0
c = 0
for i in range(1,200):
    c+=3
    if c >= langth:
        print(day,"yettik")
        break
    c -=2
    day +=1
    
print(i)

d = "ghegklsgfrgerhdhedjdg&%*))(irug"
h = len(d)
s = 0
import string
x = string.ascii_lowercase
b = string.ascii_uppercase
a = string.ascii_letters
print(x)
print(a)
print(b)
for i in d:
    if i in string.ascii_lowercase:
        s += 1
print(s)
print(h)