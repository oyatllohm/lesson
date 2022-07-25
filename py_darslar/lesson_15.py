nomer =input("tel nomerizni kiritin")


tel = nomer[1:].isdigit()


if len(nomer)==13 or len(nomer)==9:
    print("raqamingiz teksiril moqda ")
    if nomer [0:6]=="+99899"or nomer[0:2]=="99":
        print("sizni kompaniangiz Uzmabile")
    elif nomer [0:6]=="+99893"or nomer[0:2]=="93":
        print("sizni kompaniangiz ucell")
    elif nomer [0:6]=="+99891"or nomer[0:2]=="91"or nomer [1:6]=="+99890 "and nomer[0:2]=="90":
        print("sizni kompaniangiz Bileine")
    elif nomer [0:6]=="+99897"or nomer[0:2]=="97":
        print("sizni kompaniangiz UMS")
    elif nomer [0:6]=="+99833"or nomer[0:2]=="33":
        print("sizni kompaniangiz Humans ")
    else:
        print("xato raqam")
else:
    print("raqam notogri")


strin = """assalomu alekun (kirish)
hurmatlik aziz mehmonlar(balki mehmon emassizlar)
sizlarni bu erda korganimizdan hursanmiz (kozimiz uchib turgani yoq)
"""
a = strin.find("(")
s = strin.find(")")
d = strin.find("(",a+1)
f = strin.find(")" ,s+1)
g = strin.find("(" ,d+1)
h = strin.find(")" ,f+1)
print(strin[:a],strin[s+1:d],strin[f+1:g],strin[h+1:])


coment = """assalomu alekum hurmatlik  hokim buva   biz sizni juda hurmat qilamiz. \n
umringizdan baraka topin. otangizga rahmat \n
lekin shu kochamizdagi ablah T isimli kishi juda\n 
va iflos odam. shunin ustidan chora korisizni sorayamiz\n """.split()#.splitlines()


_list = ["ablah", "iflos","porahor","maraz" ]
for i in coment:
    for j  in _list:
        if j in i.lower():
            print(i)
            break
            
        
            
   


for i in coment:
    if i in _list:
        print(i,"yomon soz bor")


strin = """assalomu alekun (kirish)
hurmatlik aziz mehmonlar(balki mehmon emassizlar)
sizlarni bu erda korganimizdan hursanmiz (kozimiz uchib turgani yoq)
"""

while "(" in strin or ")" in strin:
    left = strin.find("(")
    right = strin.find(")",left)

    w = strin[left:right +1]
    strin = strin.replace(w,"")
print(strin)    


s = "py js java".replace("py","c++")
s = "py js java".count("py")


s = """ py dasturlash tili haqida.
        py hozirda en ommalashgan til.
        py 1991 yil relizga chiqqan """.split()
res =""
for i in s:
    c = s.count(i)
    data = f"{i} {c} {':'}"
    if i not in res:
        res+=data

print(res)

g = 0
k = None
for i in res.split():
    s = i.split(":")
    if int (s[1]) > g:
        g = int(s[1])
        k = s[0]
print(f"en kkop ishtirok etgan soz{k} u {g} marta ishlagan")


k =  "ассалом"
res = transliterate.translit(k,reversed=False)
print(res)

s = ["olma","behi","anor","limon"]
nev = " ".join(s)     
print(nev)
print(s)


a = -1
baho = 0
javoblar = [" "]
hato =  [" "]
viktarina = """1 savol tiko qasi zavodi aftamabili lada  dewo kia 
                .2 savol osmon jisimlaridan kattasini topin   yulduz  oy  mars  
                .3 savol ota onasiga mehribon yirtqich hayvon  arslon  bori  tulki 
                .4 savol gulikozani ornini bosuchi mava anor olma nok uzum  
                .5 savol odam tanasida birinchi ishdan chiquhi azo quloq kindik tish 
                 """.split(".")

javob = """dewo.yulduz.bori.uzum.kindik""".split(".")

for i in viktarina:
    a+=1
    savol = input(viktarina[a])
    if savol == javob[a]:
        baho +=5
        print(f"siz toptingiz javob  {javob[a]}")
        javoblar.append(javob[a])
    else:
        print("afsus topalmadiz")
        hato.append(javob[a])
print(f"siz {baho} bal topladiz")
print('siz topgan javoblar',javoblar)
print()
print("siz topalmagan javoblar",hato)





