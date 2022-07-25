# dict 
dict(non = 100,osh =15000)#  "kalit" : qiymat ,"kalit":15257  {} qavislarga yoziladi
a = {"non":100,"osh":15000}
info.keys() 0# dict turida kalitini topadi
info.values() # dict turida qiymatini topadi
r ["java"] #get key error qaytish mumkun
r ["java"] = 5 # update kalit bolsa
r ["java"] = 2 # create kalit mavjut bolmasa
d.copy() # copya olish
d.update({"age":21})# qiymat qoshish
d.setdefault("surname","familya yoq")# kalit yoq bolsa qiymat qoshadi
d.get("surname","kalit yoq") # bunday kalit yoq
d.clear()# hammasini udalit qiladi
d.pop("a","kalit topilmadi") # topsa uchiradi topalmasa aytadi
s =d.popitem()# ohiridan ochiradi va qiymatini ozgaruchida saqlaydi
.items()#log'atga qiymat qoshadi manosi buyimla


info = {}
name = "oyatulloh"
surname = "karimberdiev"
age = 33
if name or surname or age:
    info["isim"] = name
    info["fam"] = surname
    info["age"] = age
print(info.keys())
