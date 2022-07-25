
javoblar = 0
hato = 0
a = -1
baho = 0
raqam = 0
viktarina = """  savol tiko qasi zavodi avtamabili \nlada  \ndewo \nkia 
                .savol osmon jisimlaridan kattasini topin   \nyulduz  \noy  \nmars  
                .savol ota onasiga mehribon yirtqich hayvon  \narslon  \nbori  \ntulki 
                .savol gulikozani ornini bosuchi mava  qasi \nanor \nolma \nnok \nuzum  
                .savol odam tanasida birinchi ishdan chiquchi azo \nquloq \nkindik \ntish 
                .savol ozidan gaz chiqaruchi mahsulot \nkomir \nkarbit \nbenzin \nbarchasi 
                 """.split(".")

javob = "DEWO.YULDUZ.BORI.UZUM.KINDIK.BARCHASI".split(".")

for i in viktarina:
    a+=1
    raqam +=1
    savol = input(f"{raqam}{viktarina[a]}").upper()
    if savol == javob[a]:
        baho +=5
        print(f"siz toptingiz javob  {javob[a]}")
        javoblar +=1
    else:
        print("afsus topalmadiz")
        hato +=1
print(f"siz {baho} bal topladiz")
print(f'siz topgan javoblar{javoblar}\n"siz topalmagan javoblar"{hato} \n togri javob{javob}')

x = "assalo544##n".isalnum()
print(x)


summa = 0
while True:
    x = input("son kiritin yoki stop").strip().replace(" ","")
    if x == "stop":
        break                                                                                                                                                                                                                                               
    if x [0] == "-":
        if x [1:].isdigit():
            summa += int(x)
        else:
            print("faqat son kiritin")
    else:
        if x.isdigit():
            summa +=int(x)
        else:
            print("faqat son kiritin")
    
print(summa)




x = range(10)
s = [1,2,3,45,"py",x,1.5,["k","D"]]

h = ["ok",5,88,66,88,]

d = s + h
s += h


print(h)
print(s[-1][1])

x = [
[1,8,9],
[4,5,6],
[7,8,9]

]
print(x[1][1],x[2][2])

d = list(range(15))
print(d)
for i in x:
    for f in i:
        print(f)

d = list(range(15))
import random
print(d)
random.shuffle(d)
# s = random.sample(d,5)
# print(s)

# d.append(99)
print(d)
import random
f = []
d = []
for i in range(20):
    x = random.randint(1,100)
    f.append(x)
    
print(f)
for i in f:
    if i <=50:
        d.append(i)
print(d)



f = random.sample(list(range(1,100)),20)
print(f)

d = [ "ok",15,"py",-15,"java",8,-99,15,"php"]
f = []
for i in d:
    if type(i)== int:
        if i >= 0:
            f.append(i)
    else:
        pass

# print(d[2:5])

g = []
g.extend(d[2:4])
print(g)
print(d)

import random
katta = 0 
kichik = 1000
f = random.sample(list(range(100)),20)
for i in f:
    if i > katta:
        katta = i
    if i < kichik:
        kichik = i
print(f"katta raqam {katta} \nkichik raqam {kichik}")


harif= 0
d = ["php","python",15,78,"java",79, "go"]
for i in d:
    if  type (i) == str:  
        a = len (i)
        harif += a 
    else:
        pass
print(f"d list ichidagi hariflar {harif}")


list1 = ["rasim.jpg","img.png","code.cpp","image.py",
        "fon.jpg", "bmp.jpg","sicript.js","rasim.jpg",]
list2 = []
for i in list1:
    a = i.split(".")
    if a [1] not in list2 :
        list2.append(a[1])
print(list2)

