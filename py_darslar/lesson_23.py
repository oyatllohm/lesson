from math import ceil
l = ["aklsjf","hg" , {} ,4565,"gjgj",55]

def my_filter(elemeent):
    if type(elemeent)==str:
        return elemeent
d = list(filter (my_filter(l)))


f = filter(my_filter,l)
print(d)
data = input("son yozin 1 yo 2 bolsin ")

def func_1():
        print("siz 1 yozdiz")
def func_2():
        print("siz 2 yozdiz")
def func_3():
        print("siz 3 yozdiz")
    

if data == "1":
    func_1()  
elif data == "2":
    func_2()
else:
    func_3()
  
fun = {"1":func_1,"2":func_2,"3":func_3}
if fun.get(data):
    fun[data]()

s = lambda x,y :x+y
print(s(15,89))
s = lambda x,y :type(x)==int and type(y)==int
print(s(15,1))


def deco(fun):
    def wrap(x,y):
        if type(x)==int and type(y)==int:
            return fun(x,y)
        else:
            return "x y butun bolishi kerak"
    return wrap
@deco
def main(x,y):
    return x + y
print(main(11,22))


@deco
def main2(x,y):
    return x - y
print(main2(11,22))
@deco
# def decoo(fun):
#     def wrap(a,*c,**s):
#         if requste["user"]["is_authentikator"]:
#             return fun(a,*b,**b)
#         else:
#             return "404.html"
#     return wrap


@deco
def home(requste,*args,**kwargs):
        return "index.html"
    
print (home("is_authentikator"))

        
def contak(requste,*args,**kwargs):
    if requste["user"]["is_authentikator"]:
        return "contak.html"
    else:
        return "404.html"
result ={

}
