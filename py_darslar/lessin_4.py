
print(15 == 5 )
print(15 != 5 )

d = True, False,None # boolean = 101

speed = 70 
print(speed > 70 or  speed < 100)

adres = "kollej"

print(adres == "maktab" or adres == "kollej" and adres == "inustut")


if speed <=70:
    print("jarima yoq")
elif speed >70 and speed <100:
    print("100min")
elif speed > 100 and speed < 120:
    print("jarima 200 min")
elif speed > 120:
    print("jarima 300min")
else:
    print("natija topilamadi")

age = int(input("yoshingizni kiritin"))

if age < 7:
    print("siz bohcha bolasi ekansiz")
elif age >= 7 and age < 18:
    print("maktab bolasi ekansiz")
elif age > 18 and age < 35:
    print("siz orta yoshdasiz")
elif age > 35 and age < 50:
    print ("siz katta odam ekansiz")
else:
    print("siz oq soqolsiz")

y = 15 

if y < 24:
    print("Okey")
else:
    print("Error")

result = None
print(result)

result = "ok" if y > 10 else "error";print(result)

x = 9
print("x+2",x+2)
print("x-2",x-2)
print("x*2",x*2)
print('x/2',x/2)
print('x**2',x**2)
print('x//2',x//2)
print('x%2',x%2)

t = int(input("son kiritin"))

if t % 2 == 0:
    print("juft son")
else:
    print("toq son")



t = int(input("son kiritin"))
print(t*t)

print(round(3.5))
print(pow(10,2))

e = "laylak"
s = len(e)
print(s)

s = bool(e)
print(s)

a = int(input("1 soni kiritin"))
b = int(input("2 soni kiritin"))

if a % b == 0:
    print("qoldiqsiz")
else:
    print("qoldiqli")


x = int(input("1 soni kiritin"))
y = int(input("2 soni kiritin"))
z = int(input("3 soni kiritin"))

if x > y and x > z: 
    print("x  katta")
elif y > x and y > z :
    print("y katta")
elif z > x and z > y:
    print("z katta")
else:
    print("katta raqamlar ten")

if x < y and x < z:
    print("x kichik")
elif y < x and y < z:
    print("y kichik")
elif z < x and z < y:
    print("z kichik")
else:
    print("kichik raqamlar ten")


a = int(input("1 soni kiritin"))
b = int(input("2 soni kiritin"))

if a > 0 and b > 0 :
    print("a  +  b  +  I katak")
elif a > 0 and b < 0:
    print("a  +  b  - II katak ")
elif a < 0 and b < 0:
    print("a  -  b  -  III katak")
else:
    print("a  -  b  + IV katak")

