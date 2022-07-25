def main(x,y):
    """bu funciya faqat turu qaytaradi
    hardoyim 2 argumaet qabulqiladi"""
    return list(range(x,y+1))if x<y else []
a = 10
b = 84
d = main(a,b)
print(d)
import random
print(random.randint.__doc__)
print(main.__doc__)


def my_func(z,y="ok",x=False):
    print(z)
    print(y)
    print(x)

my_func(44)

def my_fun(*args,**kwargs):
    print(args)
    print(kwargs)
my_fun(a=55,f=55)

def raqam(x,y):
    if x+1 > y:
        while True:
            print(x)
            x -=1
            if x==y-1:
                break
    else:
        print("x dan y kichik bolisi kerak")
raqam(25,20)
        
def main_2(x,*y):
    """bu funsiya list ichidagi int larni jamlaydi """
    y = list(y)
    for i in y:
        if type(i)!=int:
            continue
        elif type(i)==int: 
            x += i  
        else:
            return "y butun son bolsin"
    return x
s=main_2(55,55,40,"zor",88,55,"ok",7,30)
print(s)

def symbol_conter(strr):
    """ bu funsiya harifdan boshqasini sanaydi"""
    sanoq = 0 
    for i in strr:
        if i.isalpha():
            pass
        else:
            sanoq+=1
    return print(sanoq) 
a ="assalomu# alekum# $$$$ hammaga *** hayirlik tong"
symbol_conter(a)



def chek_login(*args,**kwargs):
    """bu funsiya  login va parol qabul qiladi"""
    for i in kwargs:
        if i == "login":
            login =kwargs[i]
        elif i == "parol":
            parol=kwargs[i]
        else:
            pass
    return print(f"login  {login}  parol  {parol}")
chek_login(login="lola",parol=12345)


4