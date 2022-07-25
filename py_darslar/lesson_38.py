


# class Db:
#     counter = 0
#     # def __new__(cls,self,*args,**kwargs):
#     #     if  Db.s > 0:
#     #         raise ValueError("Erro")
#     #     return object.__new__(cls)

#     def __init__(self,data_name,users,pasword) -> None:
#         self.data_name = data_name
#         self.user = users
#         self.pasword = pasword
#         Db.counter +=1 

#     # def __setattr__(self, __name: str, __value: Any) -> None:
#     def __add__(self,valyu):
#         result = Db.counter + valyu
#         return result  

#     def __sub__(self,valyu):
#         result = Db.counter - valyu
#         return result


#     def __mul__(self,valyu):
#         return Db.counter * valyu

#     def __truediiv__(self,valyu):
#         return Db.counter / valyu


#     def __len__(self):
#         return Db.counter

#     def __bool__(self):
#         return True if Db.counter > 0 else False


#     def __eq__(self, velyu: object) -> bool:
#         return True if Db.counter ==  velyu else False

#     def __it__(self, velyu: object) -> bool:
#         return True if Db.counter <  velyu else False

#     def __gt__(self, velyu: object) -> bool:
#         return True if Db.counter >  velyu else False

    

# db = Db("users", "xikmatillo","x12345_2022")
# db2 = Db("users", "sardor","x12345_2022")
# print(db.counter > 5 )
import requests
import eel
url = "https://cub.uz/uz/arkhiv-kursov-valyuta/json/"

def chek_valyu(metod):
    def wrapper(self,*args,**kwargs):
         if type(args[0]) in ( int,float):
            if args >= 1:
                return  metod (self.args,kwargs)
  

class Convetor:
    def  klometr_to_metit(self,kiloetr):
        return kiloetr * 1000
    
    def metir_tu_santimete(self,santimetr):
        return santimetr * 100


    @staticmethod
    def today_curs():
        res = requests.get(url).json()
        return  res[0]["Rate"] ,res[1] ["Rate"] 

    @chek_valyu
    def usd_tu_uzs(self,summa):
        cousers = Convetor.today_curs()
        return  summa * cousers [0]


    @chek_valyu
    def usz_tu_usd(self,summa): 
        cousers = Convetor.today_curs()
        return  summa // cousers [0]

    

    def metor_to_dyum(self,metor):
        return metor * 254

s = Convetor()
# a=s.metor_to_dyum(1.5)
# # print(a)

d= s.today_curs()
print(d)