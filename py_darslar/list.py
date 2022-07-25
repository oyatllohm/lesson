
.extend(d[2:4])# lisdan listga kopya oladi indexdan indexgacha yo qiymat qoshadi [ozgaruchi ,"str"]
.append() # lisga qiymat qoshish list .append() qavisni ichiga kiritilyatgan ozgaruchi nomi qoshish
.remove("faqat bitta")# lisdan qiymat ochiradi manosi olib tashlash qiymatni kiritamiz
.pop()# list ichdan index boyicha ochiradi bolmasan ohiridan ochiradi
[1:3].copy()# listdan copya oladi index boyicha yo hammasi
.clear()#list ichidagi malumotlarni ochiradi
.insert(0,"qiymat yo ozgaruchan ") #list ichiga index boyicha qiymat qoshadi 
.index("qiymatni indexini topadi")
.count("qiymat nechtaligini sanaydi")
.sort() # list ichidagi raqamlarni ketma ket qiladi  yo alfabit boyicha tahlaydi
.cort(reverse=False)#teskari tahlaydi  
a = list(range(100,200)) # listga raqam qoshish
all("list nomi") # list ichidagi barcha malumot bor bolsa Turu qaytaradi bolmasam Folse
any("list nomi")# lis ichida 1 malumot bolsa Turu bolmasa Folse
b = [ i for i in range(100,201) if i % 2 == 0 ] #for ni 1 qatorda yozish 
result = "ok" if y > 10 else "error";print(result) # if bir qatorda yozilishi

[1:8] [1] [2:] [-1]   [-2:] #index ga murojat qilish
