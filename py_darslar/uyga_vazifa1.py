

True, False,None # boolean turiga man sub
is # hisoblanadi
not   #emas
in # ichida 
and # va 
or # yoki

type()# turini aniqlaydi
str() #"mati" qoshtirnoq yo bir tirnoqqa yoziladi
int() # butun  raqam 
float ()# kasir sonlar 
bool() # mantiq 
list()# list  [] qavislar ichida yziladi va vergul qoyib yana boshqa malumot yozilado
tuple() # listga ohshash () qavislarga yoziladi
dict(a = 15,f ="salom")#  "kalit" : qiymat ,"kalit":15257  {} qavislarga yoziladi

if : #  shart aperatiri
    pass
elif :
    pass
else:
    pass

# matimatik amallar

x+2
x-2
x*2
x/2
x**2
x//2
x%2

ord("k") #harif yo belgini raqamini aniqlaydi
chr(58) # raqamni harifini aniqlaydi
for # sikil 
while # bu ham sikil

continue # for while  aylammasida sakratadi
break # tohtadi

print(round(3.5)) # yahlitlaydi 
print(pow(10,2)) # daraja

try:      # hatolarni oldini oladi manosi harakat qilib korin
    pass  #   manosi otish 
except:   # bundan mustasno
    pass  # otish


def deco(fun): # funsiyaga funsiy
    def wrap(x,y):
        if type(x)==int and type(y)==int:
            return fun(x,y)
        else:
            return "x y butun bolishi kerak"
    return wrap
    raise # hato qaytaradi
@deco # yangi funsiyaga birlashtiramiz va @ tekshiruchi funsiyani nomi yoziladi
def funsiya_ochish(): 
return #funsiyada parametirga qiymat qaytaradi  
print(main.__doc__)# funsiya nomi va kalit soz fun.__doc__ funsiyani vazifasini aytadi
s = lambda x,y :x+y# bir qator funsiya 

d = max(list1) # listti icidan kattasini raqamni topadi
d = min(list1) # list  ichidan kichigini raqamni topadi 
d = sum(list1) # listti hamma raqamlardi jamlaydi
d = divmod(15,2) # raqamni boladi va qoldigini aniqlaydi

name = f"malumot {ozgaruchi} yama malumot " # ikkihil malumot turini qoshish
name ="malumot %s yama malumot %s "%(a ,b) # ikkihil malumot turini qoshish
palindrom = z[::-1] # teskari sozda ishlatiladi

n = int(input("son kiritin"))
for son in range(2,n+1):
    if son %2 == 0:
        t += son# faqat juft bolsa qoshadi
        
        #piplar
# pip install requests
# pip install pytelegrambotapi
#pip freeze