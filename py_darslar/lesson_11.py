import string
import random
pasword = "guly"
a = 0

while True:
    p =""
    for i in range(4):
        tahmin = random.choice(string.ascii_lowercase)
        p+= tahmin
    a +=1 
    if pasword == p:
        print("toptingiz", "parol", p ,a , "martada")
        break

    else:
        print(a ,p)



a = 1
d = 0 
s = 9  
while s >=d :
    a+=1
    d+=1
    print("")
    print(d ,"karra")
    for a in range(2,10):
        x = a*d
        print( d,"*",a , "=", x )




import random
words = ["c++" ,"c# ", " java" ,"python"  ,"go" , "js" , "php"]
s = random.choice(words)
matin = "yoq siz mag'lubsiz"
limit = 5
x = 0 
d = 4 
while x <= d  :
    a = input( f"oylagan sozizni kiritin{limit} imkiniz bor" )
    limit -=1
    x +=1
    if limit == 0:
       limit = matin
    if s == a :
        print("toptingiz javob" , s)
        break
    else:
        print("topalmadiz imkoniz ",limit)





import string
import random
pasword = "22oy"
a  = 0 
while True:
    a+=1
    for i in range(1,5):
        if i == 1 or i == 2 :
            x = random.randint(0,9)
            pasword+=str(x)
        else:
            s = random.choice(string.ascii_lowercase)
            pasword += s
    if x == pasword:
        break
    print(a)

a =0

for i in range(10):
    if i% 2 ==0:
        a +=2
    else:
        a+=3
    print(a)
    
max_ = 10000000000
a = 0
a = [11,55,54,99,77,33,44,47]
for i in a:
    print()
    if i < max_:
        max_=i
print(max_ , "kichik") 

while 1 > 0:
    print(15)
    break
else:
    print(25)

              




x = None 
result = "55" if x  else  "error"
print(result)