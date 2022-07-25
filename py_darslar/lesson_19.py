
store = {
    "olma":{"narh":10000,"left":81},
    "anor":{"narh":15000,"left":19},
    "banan":{"narh":17000,"left":48},
    "limon":{"narh":25000,"left":29},
    "mandarin":{"narh":38000,"left":45},
    "nok":{"narh":25000,"left":30},
    "uzum":{"narh":25000,"left":27},
    "kivi":{"narh":25000,"left":0}
}

# print(store["olma"]["narh"])
notebook = {
    "2022-01-8":{"krim":0,"chiqim":0,"foyda":0}
}

klent= input("qasi meva kerak yozin")
if klent in store:
    if store[klent]["left"]<= 0:
        print(klent,"qomadi")
    else:
        print(klent, store[klent]["narh"],"min som")
        kg = input("necha kilo olasiz").strip()
        if not kg.isdigit():
            print("faqat son kiritin")
        else:
            kg = int(kg)
            if kg > store[klent]["left"]:
                print("kechirasiz bizda bori",store[klent]["left"])
            else:
                natija = store[klent]["narh"] * kg
                store[klent]["left"]-=kg
                notebook["2022-01-8"]["krim"]+= natija
                print(f"{kg}kilo{klent} {natija} somga sotildi")
                print(f"omborda {klent}{store[klent]}kg qolti ")
                print("kirim va chiqim" ,notebook)
else: 
    print("kechirasiz bunday mahsulot ")

        
s = [1,2,3,4,57,8,2,""]
res =all(s)
res =any(s)
print(res)

import random
s = random.sample(range(150),20)
print(s)
def my_filter(eliment):
    return eliment

s = [1,None,"py",None,"php",78,[],True]
r = list(filter(my_filter,s))
print()



students = {
    "olim":{"surname":"islombekov",
            "aderes":"pahtabot",
            "davomat":{
                    "keldi":12,
                    "kemadi":3
        }
    },
    "abdulloh":{"surname":"salijonov",
            "aderes":"izboskan",
            "davomat":{
                    "keldi":13,
                    "kemadi":2
        }
    },
    "sardor":{"surname":"Isoqjonov",
            "aderes":"pahtabot",
            "davomat":{
                     "keldi":9,
                    "kemadi":6
        }
    },
    "olimjon":{"surname":"Maxkamov",
            "aderes":"Asaka",
            "davomat":{
                    "keldi":8,
                    "kemadi":7
        }
    }
}
bad = []

for i in students:
    if students[i]["davomat"]["keldi"]<10:
        s = {"name":i,"surname":students[i]["surname"]}
        bad.append(s)
print(bad)




a = 0 
s = 0
savol = [
    "1. osmon rangi qanaqa",
    "2. O'zbekiston poytahti",
    "3. python nechanchi yil chiqqan"
]
varyant = [
    ["kok","qizil","movoy"],
    ["Maskuva","Asaka","Tashkent","pikin"],
    ["1991","1985","1995","1975"]
]
javob = ["Moviy","Tashkent","1991"]
for i in savol:
    print(savol[s])
    f = input(varyant[s]).title()
    s+=1
    if f == javob[a]:
        a+=1
        print("javob tog'ri")
    else:
        print("hato")

