class Round:
    def round(self,summa):
        
        s = str(summa)
        d = {5:2,6:3,7:4,8:5}
        _index = d.get(len(s))
        print(_index)
        if _index is None:
            raise  ValueError("hato")
        if int (s[_index:]) >= 500:
            res = f"{int(s[:_index]) +1}000"
        else:
            res = f"{int(s[:_index]) }000"
        return res
            
d = Round()
s=d.round(55556)
print(s)

# r = Round ()
# d = r.round(15678)

from turtle import width

class Geom :
     
    def check(self,velue):
        if type(velue )in (int,float):
            if velue > 0:
                return True
        return False
    def  __init__(self,width,higet):
        if  self.check(width) and self.check(higet):
            self.width = width
            self.higet = higet
        else:
            raise ValueError("notogri qiymat berilgan")

    
    def surfase(self):
        return self.width * self.higet


    def set_head(self,higet):
        if self.check(higet):
            self.higet = higet
        else:
            raise ValueError("notogri qiymat")

    def set_head(self,width):
        if self.check(width):
            self.width = width
        else:
            raise ValueError("notogri qiymat")




# class Rekt(Geom):    
    
#     def __str__(self) -> str:

#         return  f"tort burchak boyi{self.width} eni {self.higet}"
    
# r = Rekt(15,55)
# # print(r)

# class Square(Geom):
   
#     def __str__(self) -> str:

#         return  f"kvadrat boyi{self.width} eni {self.higet}"





# # d = issubclass(Rekt ,object)
# # print(d)

# class Gm :

#     def kuzov(self):
#        print("zanglamas kuzov")
#     def maginittolasi(self):
#         return None
#     def rul (self):
#         print("rul bor")


# class Car(Gm):
#     def avto():
#         return print("aftamabil")

# s = Car ()
# a = s.kuzov()


# d = Car ()
# s  = d.rul()
import random

class Gun :
    def __init__(self,name, weige ,tupe_of_bullet,uron):
        # self.name = name  
        # self.weige = weige
        # self.tupe_of_bullet = tupe_of_bullet
        # self.uron = uron 
        pass
        
    def aftamat():
        aftamat = random.choice(['M16',"AK47",'AGU',"VAL","AK74"])
        kachistiva= random.choice([5,6,7,8])
        # p_name = random.choice(["uzun","chachma","sipiral"])
        patron = 30
        return "AFTAMAT",aftamat ,kachistiva ,  patron 

    def topponcha():
        topponcha = random.choice(["PM","P99","Glock","USP"])
        kachistiva= random.choice([1,2,3,4])
        # p_name = random.choice(["uzun","chachma","sipiral"])
        patron = 12
        return   "TOPPONCHA" ,  topponcha , kachistiva  ,patron
        
class Personaj :
    @staticmethod
    def chek_life(life):
        if isinstance(life,int):
            if life > 75:
                return True
        raise ValueError("life 75 katta son bolishi !! ")

    def __init__(self,name,positsion,life ):
        self.name = name
        self.positsion = positsion
        self.life = life
        self.defence =  False
        self.gun = random.choice([Gun.aftamat(),Gun.topponcha()]) 

# d = {1:25,2:50,3:75,4:100,5:125,6:150,7:175,8:200,9:225,10:250,11:275}
    # _index = d.get(x)
  # return son[_index-25:_index]
  