class Klavyatura :
    def __new__(cls,*args ,**kwargs):
        if not kwargs.get("kabel"):
            raise ValueError ("kabel korsatilishi shart")
        return object.__new__(cls)

    def __init__(self,kilaviyatura,kabel):
        self.kilaviyatura =kilaviyatura
        self.kabel = kabel
    # def __str__(self):  # __str__ abektni pirint qiberadi
    #     return self.kilaviyatura 
        
    def info (self):
        return self.kilaviyatura ,self.kabel
      
     
infoo = Klavyatura(kilaviyatura="105 knopka")  
print(infoo)

print(isinstance("kf",int))



class Filewirete:
    file_conter = 0 
    def __init__(self,filname):
        self.filname = filname

    # def __setattr__(self, __name: str, __value: str) -> None:
    #     print(__name)
    #     print(__value)


    def yozish(self,data):
        f = open(f"{self.filname}","w" )
        f.write(data)
        f.close()

    def oqimoq(self):
        f = open(f"{self.filname}","r" )
        return f.read()

    def qoshmoq(self,data):
        f = open(f"{self.filname}","a")
        f.write(data)
        f.close()

g = Filewirete("vazifa.txt")
# print(g.oqimoq())
# a = g.oqimoq()
# print(a)


class Abanent:
    """bu class  abanentlarni qabul qiladi 
        va telfon qiladi 
        va malumotlarini beradi 

            call : tel qilish 
            info : malumotlarini olish

        """
    def __init__(self,name,tel_number,balans):
        self.name = name
        self.tel_number = tel_number
        self.balans = balans


    def call(self):
        return print(f"chaqirilmoqda \n {self.tel_number}")

    def info(self):
        return self.name, self.tel_number, self.balans


tel = Abanent("oytilla","99 900 25 33","10.20 $")
tel_2 = Abanent("ahmadulloi\n","90 060 10 44\n", "3.45 $")

print(tel.info())
tel_2.call()




# def sort (sarala):
#     sanoq = 1 
#     tartib = []
#     while  True: 
#         for i in sarala:
#             if i == sanoq :
#                 tartib.append(i)
#                 sanoq+=1 
#         if sanoq-1 == max(sarala):
#             break
#     return tartib          

# listt = [4,5,1,7,12,2,8,3,6,9,10]


# s = sort(listt)
# print(s)


