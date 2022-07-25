
nomber1 = int(input("1 soni kiritin"))
operator = input(" Matematik amallarni kiritin + - * / :")
nomber2 = int(input("2 soni kiritin"))

if operator  == "+":
    print(nomber1 + nomber2)
elif operator == "-":
    print(nomber1 - nomber2)
elif operator == "*":
     print(nomber1 * nomber2)
elif operator == "/":
     print(nomber1 / nomber2)

d = 45
d += 15
d *= 15
d /= 15
d -= 15
print(d)

a = 0
x = int(input("1 soni kiritin"))
y = int(input("2 soni kiritin"))
z = int(input("1 soni kiritin"))

if x > 10:
    a += 1 
if y > 10:
    a += 1
if z > 10:
    a *= 10
print(a)

f = "olma"
for f in range(15):
    print(f * "#*")


z = input("teskari soz")
palindrom = z[::-1]
if z == palindrom:
    print("bu palindrom soz ")
else:
    print("bu palindrom emas")


y = "oshqovoq"
z = input(" parol va xabar kiritin")

if y == z[:8]:
    print(z[8:])
else:
    print("parol xato")


x = int(input("1 soni kiritin"))
y = int(input("2 soni kiritin"))
z = int(input("3 soni kiritin"))

if x > y and z < y:
    print("y orta raqam")
elif x < y and z > y:
    print("y orta raqam")
elif x > z and y < z:
    print("z orta raqam")
elif x < z and y > z: 
    print ("z orta raqam")
elif z > x and y < x:
    print("x orta raqam")
elif z < x and y > x:
    print ("x orta raqam")
else:
    print("raqamlarda tenglik kuzatildi")

son = 1
while son <=31:
    print(son)
    son +=1

from random import randint
kodlar =[111, 115, 113, 117]
yangi_kod = randint(110,118)

i = 0
while yangi_kod in kodlar:
    i += 1
    yangi_kod = randint(110,118)
print("tak",i)
print(yangi_kod)

son = input("son kiritin")
while son:
    if son .isdigit():
        print("tashakkur")
        break
    
    else:
        son = input("son kiritin")

son = input("son kiritin")
while not son.isdigit():
    print("hatolik")
    son = input("boshqalattan kiritin")
    print("rahmat")

n = int(input("son kiritin"))
t = 0
for son in range(2,n+1):
    k = son %2
    if k == 0:
        t += son
    else:
        continue
print("jami",t)

soz = input("soz kiritin")

for s in soz:
    if s.isdigit():
        continue
        print("s,",s)
        break
    print(s)

# from turtle import Turtle, Screen
# oyna = Screen()
# chiziq = Turtle()
# chiziq.pensize(5)
# chiziq.speed(0)
# chiziq.color('red')
# chiziq.up()
# chiziq.goto(200,200)
# chiziq.down()
# chiziq.goto(200,-200)
# chiziq.goto(-200,-200)
# chiziq.goto(-200,200)
# chiziq.goto(200,200)


# oyna.mainloop()

