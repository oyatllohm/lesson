
os_oyini =  """



 ________
  |       | 0
  |       
  |
  |____
  ,

  ________
  |       | 1
  |       
  |
  |____
  ,

  ________
  |       | 2
  |       O 
  |     
  |____  
  ,
  ________
  |       | 3
  |       O 
  |       |
  |____
  ,
  ________
  |      | 4
  |      O
  |     /|\\
  |____ 
  ,
  ________
  |      | 5
  |      O
  |     /|\\
  |____ / \\






""".split(",")

import random
jumboq = ["php","js","c++","c#","go"]
a = 1
s = random.choice(jumboq)
for i in range(5):
    javob = input("php js c++ c# go   birini tallen")
    if s == javob:
         print(os_oyini[0],"qutqardingiz")
         break
    else:
        print(os_oyini[a])
        a+=1


x = "####G'LHKJOTH###"
f = x.rstrip("#")
f = x.lstrip("#")
f = x.strip("#")
print(f)


x = "salom \ndunya \nhello"
s = x.split()
s = x.splitlines()
print(s)


x = "pa#ro#l#".replace("#","",2)

print(x)


d = ["pag_1","pag_2", "chapter_3","unit_4"]
for i in d:
  s=i.split("_")
  print(s[1])

sms = "flkgjs;  g;g oshqovoq:tavar_kelmadi sldkfj"
f=sms.split()

  
for i in f:
    if i.startswith("oshqovoq"):
        s = i.split(":")
        print(s[1].replace("_"," "))



x = "salom".upper()
s = "FJADKS;L".lower()
f = "assalomu alekum".title()
g = 'assalomu \nalekum'.capitalize()
print(f)
print(g)

name = input("ismingizni kiritin")
d = name.strip().title()

print(d)


d = ""
s = 1
n = "assalomu alekum"
for i in n:
  s+=1
  if i.isalpha():# harifligini tekshiiradi
    if s % 2== 0 :
      d+=i.upper()
    
    else:
      d+=i.lower()
print(d)


s = "salom".islower()
s = "GJJHG".isupper()
s='qweiri'.isalpha()
s='dfld64#kv5'.isalnum()

print(s)


f = input("habar kiritin")
s = "habar"
if f.lower() == s:
  print("ok")


x = "olma $behi$i"
f = x.find("$")
s = x.find("$", f+1)
print(f,s)
print(x[f+1:s])
a = "hfasdh alfjakj lfhgj".strip("a")
print(a)