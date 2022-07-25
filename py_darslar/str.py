# str metodlar
len() # str hairiflarni sanaydi
"assalom".count("s") # str belgilandan harifni sanaydi 
"assalom".replace("s","$") #str  harifni almashtiradi
"satir".startswith("https")# shart qoyiladi bilan boshlansa shuni topadi  
"satir".rstrip("*") # chapdan onga belgi yo bos joylarni tozalaydi raqam yo harif chiqquncha
"satir".lstrip(" ") # ongdan chapga belgi yo bos joylarni tozalaydi raqam yo harif chiqquncha
"satir".strip(" ") # satirdan boshi va ohiridagi bos joylarni yo belgini tozalaydi  
"satir".split(".") # satirda belgilangan joylarni ajratib list tutiga aylantiradi yo bosh joydan
s = x.splitlines()# satirda pastagi qatorlardan ajratib listga aylantiradi
"satir".join() #lisdan satirga kopya oladi qavis ichiga list nomi yoziladi
.find() #satir ichidan belgini topish va index raqamini  aytadi
g.capitalize()# bosidagi harifni 1 marta katta qiladi
.title()# har bir sozni boshini katta qiladi
.upper()# hamma harifni kattaytiradi
.lower()#hamma harifmi kichaytiradi


# tekshirih metodlari
s = "555".isdigit()#raqam ligini anig'lash
s = "salom".islower()# satirni kichik harif ligini tekshiradi
s = "GJJHG".isupper()# satirni katta harif ligini tekshiradi
s='qweiri'.isalpha() # satirni faqat harif logini tekshiradi
s='dfld64#kv5'.isalnum() # satirni raqam va hariflogini tekshiradi

