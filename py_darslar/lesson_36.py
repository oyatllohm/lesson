
class Fileobjekt:

    def __init__(self,file) -> None:
        self.file =file
       
    def fayil_ochish(self,data):
        f = open(f"{self.file}","w")
        f.write(data)
        f.close()

    def fayil_oqimoq(self):
        f= open(f"{self.file}","r")
        
        return f.read()
    def fayil_davomiga_yozish(self,data):
        f = open(f"{self.file}","a")
        f.write(data)
        f.close()
class File(Fileobjekt):
    pass

f = File("vazifa.txt")
# s = f.fayil_ochish("vazifa.txt")
f.fayil_davomiga_yozish("\nsalom")
# d = f.fayil_oqimoq()
# print(d)


# import random
# from lesson_35 import Personaj 
# import time
# class War:

#     @staticmethod
#     def game_over(winner,loser):
#         info = f"""
#               oyin tugadi
#               Golib {winner.positsion} {winner.name} life {winner.life}

#               Maglub {loser.positsion} {loser.name} life {loser.life}
#         """
#         print(info)
    
#     def himoya(self):
#         self.defence = random.choice([True,False])

#     def attck(self,target,bullet_count):
       
#         target.himoya()
#         print (f"{self.name}    {target.name}   ga hujum qilmoqda")
#         time.sleep(.5)
#         print (f"otilgan oqlar soni\n{bullet_count}")
#         time.sleep(.5)
#         r = random.randint(0,bullet_count)
#         print(f"nishonga tekkan oqlar soni   {r}")
#         uron = 2 if target.defence else 3
    
#         if self.gun[2] >= 5: # jonga zarar
#             uron = 5 
#         else :
#             pass 
#         print(f"zarar   {uron * r }   ga Ten")
      
#         target .life -= uron * r
#         print(f" HARBIR OQNIN  JONGA BERGAN ZARARI    {uron}  TEN ")
#         if target.life <=0:
#             War.game_over(winner=self,loser = target)

#         if target.life <=0 : # qurolni ozlashtirish
#             self.gun += target.gun
#             target.gun = "bu qurolni ozlashtirib ketishdi"
#         else:
#             self.gun 
#             target.gun

# class Human(Personaj,War):
#     def __str__(self) -> str:
#         return f"human:name {self.name} positsion{self.positsion} life {self.life}"
    


# class Alian (Personaj,War) :
#     def __str__(self) -> str:
#         return f"alian:name {self.name} positsion{self.positsion} life {self.life}"
    


# def war (janchi,dushman):
#     while True:
#         if  janchi.life <= 0 or dushman.life <= 0 :
#             break
#         if janchi.life > 0 :
#             janchi.attck(dushman,bullet_count)
#         if dushman.life > 0 :
#             dushman.attck(janchi,bullet_count)




# human = Human ("jhon","kapral",100)
# alian = Alian("motaru","se205",100)
# adi = Human("zafar","kamandir",100)
# bullet_count = random.randint(5,15)



# war(human,alian)

# print("odam",human.gun)
# print("ozga sayyora",alian.gun)
