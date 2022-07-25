



import datetime
from distutils.log import fatal
class Car:
    model = "malibu"
    color = "qora"
    pozitsion = 4
    year = 2020
    price = 0 
    def __init__(self,pozutsiya,color,model):
        self.color =color
        self.pozitsion = pozutsiya
        self.model = model
        self.year = datetime.datetime.now().year

    def information (self):
        return self.model ,self.color ,self.pozitsion, self.year , self.price
        # print("b?u Car class metodi")

    def set_color(self,color_name):
        self.color = color_name

malibu_2 = Car(pozutsiya=2,color="black",model="malibu")
Nexia = Car(pozutsiya=2,color="oq",model="Nexia")
malibu_2.set_color("white")

# print(malibu_2.model,malibu_2.color,malibu_2.pozitsion)

# print(malibu_2.color)


# Spark = Car()
# Nexia.color = "oq"
# print(Nexia.__dict__)


# print(Nexia.model)
# print(Spark.model)


# print(Car.year)
# print(Car.info())
# car = Car() 

# class Home :
#     hana =  None
#     sotik = None
#     raqam = None
#     manzil = None
#     narh = None

# uy = Home()

# uy.hana=5
# uy.manzil="sahar"
# uy.raqam=55
# uy.sotik=5
# uy.narh = f"{40000}$"

# uy_2=Home()
# uy_2.hana = 6
# uy_2.manzil="tuman"
# uy_2.raqam= None
# uy_2.sotik = 12
# uy_2.narh = f"{30000}$"


# print(uy.__dict__)
# print(uy_2.__dict__)





class Lotin_kiril_transle:
    def latin(word):
        latin_dict = {
        'a': 'а',
        'b': 'б',
        'c': 'с',
        'd': 'д',
        'e': 'э',
        'f': 'ф',
        'g': 'г',
        'h': 'х',
        'i': 'и',
        'j': 'ж',
        'k': 'к',
        'l': 'л',
        'm': 'м',
        'n': 'н',
        'o': 'о',
        'p': 'п',
        'q': 'к',
        'r': 'р',
        's': 'с',
        't': 'т',
        'u': 'у',
        'v': 'в',
        'w': 'ш',
        'x': 'х',
        'y': 'й',
        'z': 'з',
        'ng': 'нг',
        'ch': 'ч',
        'sh': 'ш',
        "'": "ъ",
         ' ': ' '}
        transle = ""          
        for i in word:
            if word.find(i)== word.find("s") and word.find(i)+1== word.find("h"):
                transle += latin_dict["sh"]
            elif word.find(i)== word.find("h") and word.find(i)-1== word.find("s"):
                continue
            elif word.find(i)== word.find("c") and word.find(i)+1== word.find("h"):
                transle += latin_dict["ch"]
            elif word.find(i)== word.find("h") and word.find(i)-1== word.find("c"):
                continue           
            else:
                transle += latin_dict[i]
        return transle

days = Lotin_kiril_transle.latin("chorshanba")
# print(days)

# taom = Lotin_kiril_transle.latin("shashlik")
# print(taom)


from lesson_32 import Filewirete 

fayil = Filewirete("vazifa.txt") 

fayil.qoshmoq("non\n")
# print(fayil.oqimoq())