

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
    
    def transfer(self,clent,summa):
        if summa > self.balans:
            raise ValidationErr("hato")
        else:
            self.balans-= summa
            clent.balans += summa

# Bank.print_data(15)




klent1  = Bank("AB1234568","1234567899","+998999002533")
klent2  = Bank("AB1234567","1234567899","+998999002533")



from turtle import width


class Rect :
    __slots__ = ["width","higet","__dict__","background"]
    def __new__(cls,*args,**kwargs):
        if not kwargs:
            raise ValueError("boyi va enini  korsatilmagan")
        width = kwargs.get("width")
        higet = kwargs.get("higet")  
        if type (width) in (int ,float) and type (higet) in (int ,float):
            if width > 0 and higet > 0 and width != higet:
                return super().__new__(cls)
            else:
                raise ValueError("uzuni va eni con bolishi kerak")
        

    def  __init__(self,width,higet):
        self.width = width
        self.higet = higet

    def surfase(self):
        return self.width * self.higet

    # @property
    # def higet(self):
    #     return self.__dict__["higet"]

    # @higet.setter
    # def higet(self,nev_higet):
    #     if type(nev_higet) in (int, float) :
    #         if nev_higet > 0 and nev_higet != self.width:
    #             self.__dict__["higet"] = nev_higet
    #     else:
    #         raise ValueError("invalit qiymat")

    # @higet.deleter
    # def higet(self):
    #     raise PermissionError("ochirishga ruhsat yoq")
    # higet = property (get_higet ,set_higet,del_higet)


    def __setattr__(self, attirName , attirValyu) :
        if attirName == "background":
            if isinstance(attirValyu , str):
                object.__setattr__(self,attirName,attirValyu)
            else:
                raise ValueError("background faqat str bolishi kerak")
        object.__setattr__(self,attirName,attirValyu)
        pass
   
        
r = Rect(width=10,higet=4)
# r.set_higet(50)
# r.higet="15"
# r.width = 15

r.background = ""
print(r.background)
# print(r.__dict__)
# s = r.surfase()
# print(s)




class Round:
    def roundi(self,summa):
        nollar = "" 
        sstr = str(summa)
        if len (sstr) == 5 :
            almashuchi_qiymat = int(sstr[2:])
            if almashuchi_qiymat >= 500 :
                nollar += "000"
                bosh_qiymat = str(sstr[:2])
                summa = bosh_qiymat + nollar
                summa = int (summa )+ 1000
            else:
                nollar += "000"
                bosh_qiymat = str(sstr[:2])
                summa = bosh_qiymat + nollar
                summa = int(summa)
        else:
            raise ValueError( "biz faqat 5 taliik sonlarni yahlitlaymiz")
        return summa



            
            
            

d = Round()
g  = Round()
k = g.roundi(99894)
print(k)
s = d.roundi(12435)
print(s)
f = d.roundi(72279)
print(f)
