
info.keys() # dict turida kalitini topadi
info.values() # dict turida qiymatini topadi
r ["java"] #get key error qaytish mumkun
r ["java"] = 5 # update kalit bolsa
r ["java"] = 2 # create kalit mavjut bolmasa

w = 0
m = "java c# java pythaon go java pythao rubi"
r = {"java":3,"c#":1,}
s ={}
for i in m.split():
    s = m.count("java")
print(s)

for i in m.split():
    if s > w:
        w = s[i]
print(w)

d = dict(a=15,name="sardor",aderes="andijon")
# # print(d)
# if "surname"in d:
#     print(d ["surname"])

s = d.get("surname","kalit yoq")
s = d.setdefault("surname","familya yoq")
s = d.update({"age":21})
print(d)
f = d.copy()
d.clear()
d.pop("a","kalit topilmadi") 
print(d)
s =d.popitem()
print(f)




students = {
    "olim":{"surname":"islombekov",
            "aderes":"pahtabot",
            "age":20,
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



for i in students:
    if "age" not in students[i]:
        f = int(input(f"{i}yoshini kiritin"))
        students[i].update({"age":f})               
print(students)


store = {
    "olma":{"narh":10000,"left":81},
    "anor":{"narh":15000,"left":50},
    "banan":{"narh":17000,"left":48},
    "limon":{"narh":25000,"left":29},
    "mandarin":{"narh":38000,"left":45},
    "nok":{"narh":25000,"left":30},
    "uzum":{"narh":25000,"left":50},
    "kivi":{"narh":25000,"left":10}
}

today ={
    "olma":{"sold":50},
    "anor":{"sold":25},
    "banan":{"sold":45},
    "limon":{"sold":5},
    "mandarin":{"sold":40},
    "nok":{"sold":20},
    "uzum":{"sold":35},
    "kivi":{"sold":4},
}


sitatistic ={} 

for i in store:
    s = store[i]["left"]-today[i]["sold"]
    a = store[i]["narh"]*s
    sitatistic.update({i:{"narh":store[i]["narh"],"kg":s,"summa":a}})
print(sitatistic)



