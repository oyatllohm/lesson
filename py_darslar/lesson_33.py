
d=[4,5,1,7,12,2,8,3,6,9,10]
# n = len(d)
# print(n)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if d[j] > d[j+1]:
#             d [j] ,d [j+1] = d[j+1],d[j]
# print(d)


from ast import arg
from datetime import date
from ntpath import join
from pyclbr import Function
from xml.dom import ValidationErr

paspurt_stoll ={"AB1234567":
                            {"name":"shokkirjon","surname":"rahimov","birth":date(1985,7,22)},  
                "AB1234585":                        
                            {"name":"asror","surname":"obidov","birth":date(2008,6,10)},
                "AB1234568":
                            {"name":"sanjar","surname":"yaqubov","birth":date(1990,1,15)}
}
import re 


class Bank:

    @classmethod
    def check(cls,pasport_serya,phone,banc_accaunt):
        if re.match(r"[A-Z][A-Z]\d\d\d\d\d\d\d$",pasport_serya) == None:
            raise ValidationErr("paspurt serya hato")
        if not re.match(r"\+998(?:99|88|90|93)\d\d\d\d\d\d\d$", phone):
            raise ValidationErr("nomer hato")
        if not re.match(r"\d\d\d\d\d\d\d\d\d\d$",banc_accaunt):
            raise ValidationErr("bank akkaint hato")
       
    @staticmethod 
    def print_data(x):
        print(x)


    def __init__(self,pasport_serya,banc_accaunt,phone,balans=0):
        Bank.check(pasport_serya,phone,banc_accaunt)
        if pasport_serya in paspurt_stoll:
            self.name = paspurt_stoll[pasport_serya]["name"]
            self.surname = paspurt_stoll[pasport_serya]["surname"]
            self.brith = paspurt_stoll[pasport_serya]["birth"]
            self.banc_accaunt =banc_accaunt
            self.phone =phone
            self.balans = balans
        else:
            raise ValidationErr("pasputr serya topilmadi")

    def info (self):
        return self.name , self.surname ,self.banc_accaunt, self.balans 

# Bank.print_data(15)

bank = Bank("AB1234568","1234567899","+998999002533")



# from typing_extensions import Self


class Baank :
    def __init__(self,name, bank_accaunt,balans):
        self.name = name
        self.bank_accaunt = bank_accaunt
        self.balans = balans

    
    def deposit(self,deposit):
        self.balans += deposit
    
    def withdrow(self,withdrow):
        if withdrow <= self.balans:
            self.balans -= withdrow
        else:
            raise ValidationErr("balansizda mablag' yetarlik emas")

    @classmethod
    def otkazma_nazorat(cls,*args ):
        pass
        for i in args:
           print(i)
           
        # if i == :
        #     print("otkazma amalga oshdi")
        # else:
        #     raise ValidationErr("mablaglar ten boloshi kerak")
                
            
    
    def transfer(self,pul,klentt):
        Baank.otkazma_nazorat(pul)
        if self.balans >= pul:
            self.balans-= pul
        else:
            raise ValidationErr("hisobizda mablag yetarlik emas")


    def otkazma(self,pul):
        self.balans += pul   
        Baank.otkazma_nazorat(pul)
    
     

    def info(self):
        return self.balans
    
    
    
kilent = Baank("oyatillo","12345",10)
kilent2 = Baank("ahmadillo","12456",0)
# kilent.deposit(40)
# kilent.withdrow(5)

# print(kilent.balans)
# print(kilent2.balans)
kilent.transfer(4,kilent2.otkazma(5))
print(kilent.balans)
print(kilent2.balans)
