s = "pythonphp"
index= 0 
while index < len(s):
    print( s[index] )
    index += 1


data = "2019-03-30"

month = None 
     
if data [5:7] == "01":
    month = "yanvar" 
    
elif data [5:7] == "02":
    print(data[5:7]," febral oyi",data[0:4],data[8:] ,"cana")
elif data [5:7] == "03":
    print(data[8:],data[5:7],data [0:4], "cana")


import random
words = ["c++" ,"c# ", " java" ,"python"  ,"go" , "js"]
s = random.choice(words)
x = 0 
d = 5 
print(s)
while x <= d :
    a = input("oylagan sozizni kiritin")
    x +=1
    if s == a :
        print("toptingiz")
        break

    else:
        print("topalmadiz")


pasword = "1111"
a = 0

while True:
    p =""  

    for i in range(4):
        rand_int = random.randint(0,9)
        p+= str(rand_int)
    a +=1 
    if pasword == p:
        print("toptingiz", "parol", p ,a , "martada")
        break

    else:
        print(a)


d = "py#th#on"
f = ""
for i in d :
    if i == "#":
        f +="0"      
    else:    
        f +=i
print(f)
