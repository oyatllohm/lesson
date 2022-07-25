
parol = "oshqovoq"
message = input("habar kiritin")

if len(message)>8:
    if message[:8] :
        pass

passport_seria ="AB1234567"

if len(passport_seria)==9:
    if passport_seria[0]in "AB1234567"and passport_seria[1]in"AB1234567":
        if passport_seria[2:].isdigit():
            print("qabul qilindi")
    else:
        print("bu serya notogri")
else:
    print("passport_seria hato kiritildi")



sms = input("soz kiritin #bolmasin ")

if "#" in sms :
    print("  sms qabul qilimmadi")
else:
    print(" sms qabul qilindi")


f = "dol#lar$u#sa$ru$$#$bl$"
a = 0
s = 0
for i in f:
    if i == "$": a+= 1
    if i == "#" :s+=1
print("satir ichida",a,"dona $ belgisi bor")
print("satir ichida",s,"dona # belgisi bor") 