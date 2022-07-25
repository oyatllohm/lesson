
import keyword # aperatorlar
print(keyword.kwlist)

import string # str raqamlarini chaqirish 
string.ascii_lowercase #kichkina harif
string.ascii_uppercase #katta harif
string.ascii_letters # jamlammasi

import random # tasodifi topish 
random.random() # kasir
random.randint(1,10)#  butun 
random.shuffle(d)# list ichidagi qiymatlarni aralashtiradi
random.randrange(1,100,10) #butun 3 chisi joy tashaah
random.choice() # list ichidan tasodif matinni yo raqamni  tanlab  oladi 
random.sample(list,5) # list ichidan tasodif raqamlarni yo sozlarni oladi qiymati ham bor misol 5

import hashlib  # parol himoyalashda ishlanadi
 md5 = hashlib.md5()  # bir ozgaruchida saqlaymiz
 md5.update(pasword) # parolni qavus ichiga solamiz
 print(md5.hexdigest()) # ozgaruchibilan birga chop qilamiz


import math # matimatik funksia
p = math.ceil(s)  # raqamni tepaga qarab yahlitlaydi
p = math.floor(a) # raqmni paska qarab yahlitlaydi 
p = math.sqrt(s) # darajani teskarisiga ohshash 
print((x).is_integer()) # filoatda fols qaytaradi butun sonmas deganday


import locale
locale.setlocale(locale.LC_ALL,"uz_UZ.utf-8")
#  uz bekchaga tarjima qiladi calendar va date dagi sozlarni

import re 
r = re.match(r"[A-Z][A-Z]\d\d\d\d\d\d\d","AB1234568")
# r = re.match(r"\+998(?:99|88|90|93)\d\d\d\d\d\d\d", "+998999002533")
# # print(r)
