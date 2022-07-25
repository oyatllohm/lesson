
d = [1,2,3,4,"java",15,45,"php","js",78]
a = -1
for i in d :
    print(i)
    if type(i) != int:
        indeks = d.index(i)
        print(indeks)
        d[indeks] = 0  
print(d)

s = tuple ("python")
a = list ("python")
print(s)
print(a)

d = list(range(50,250))
d = dict(a=15)

x = 15
y = 23
d = {"key":x,"kalit":y}

s = dict(name="oyatullo",fam="karimbrediev")

a = {"name":"oyatulloh","fam":"karimberdiev"}
print(a["name"])

info = {}
name = "oyatulloh"
surname = "karimberdiev"
age = 33
if name or surname or age:
    info["isim"] = name
    info["fam"] = surname
    info["age"] = age
print(info.keys())

# for i in info.keys():
for i in info.values():
    print(i)

a = {"a":15,"b":150,"x":88}



"m harfini sanovchi cod"
a = "we recommend reading this tutorial, in the sequence listed in the menu."
m = 0
indeks = 0
while indeks <len(a):
    x = a[indeks]
    indeks+=1
    if x == "m":
        m += 1
print(m,a)

# str ochiruchi cod 
a = [1,55,5,3,"ok",[88],"java",("php"),len("you"),"crack"]
for i in a :
    if type(i)==str:
        a.remove(i)
print(a)

# qiymatni alishtiruchi cod
a = {"key1":None,"key2":None,"key3":None,"key4": None}
for i in a:
    a [i]=1
print(a)

# barcha raqamlarni jamlovchi cod
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
