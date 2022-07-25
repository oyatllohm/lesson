
name = "oyatulloh"
date = "2021-12-31"

sms = f"""hurmatli {name} dasturdan fOYDlanish muddati {date} sanada tugaydi """#.format( ism=name,sana=date)
print(sms)

x = input("sozni kiritin s harifidan boshlansin")


if x [0]=="s"or x[0]== "S":
    print("qabul")

x.strip()

x ="2021-21-21".split("-")
year= None
month= None
day = None
print(x)

file_name = input("fayil nomi va formatini kiritin").split(".")
if len(file_name)<2:
    print("hato")
else:
    if file_name[-1] =="jpg" or file_name[-1] == "png" or file_name[-1] == "jpeg":
        print(file_name)
    else:
        print("hato faqat rasim joylang")


coment = input("koment kititin")

c = coment.strip()

check = c.startswith("<sikiript>")
print(check)
 
massage = "dkfoieoibheoi https://t.dollar.uz hzehnedthdte "
s = massage.split()
for i in s:
    if i.startswith("https"):
        m = i.split("//")
        print(m[1])



