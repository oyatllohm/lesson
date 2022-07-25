a = "*"
z = 111
print(z*a)

x = 15 
y = 14
s = x != y
print(s)

x = input("son kiritin")
print(  int (x) < 100)

x = "okey bollar"
y = "okey"
print("okey" not  in x )

print(x == y)
d = x !=y
print(x > y)
 
print(100==100)

x = input("yosizni kiritin")
x = int(x)
if x <7:
    print("siz bohcha bolasisiz")
if x >= 7 and x < 16:
    print("siz maktab oquchisisiz")

elif x > 16  and x < 100: 
    print("siz katta bo'lib qolibsiz")
    


s = input("paspurtiz bormi xa/yoq dep yozin")
if s == "xa":
    print("pasport bor")
else:    
    print("pasport yoq")

tezlik = int (input("tezligizni kiritin"))

if tezlik <= 70 :
    print("okey")
elif tezlik > 70 and tezlik <=100:
    print("jarima 100 min ")
elif tezlik > 100 and tezlik <= 120:
    print("jarima 200 min")
elif tezlik > 120 and tezlik <= 150:
    print("jarima 300 min")
else:

    print("bu tezlik xayot uchun xaflik va haydovchilik guvohnomani vaqtinchalik olibqoyiladi")
