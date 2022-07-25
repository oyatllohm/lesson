# print(5852)
# x = input("isim")
# print(x)

# age = 33
# aderes = "uzumzor 188"
# print(aderes, "yoshingiz",age,"da") 


# x = 15 ;y = 25;z = 50
# print( x, y, z)

# import keyword
# print(keyword.kwlist)

# name = "oyatulloh"
# age = 33
# print(name,age)

# h = "hello world" # str
# a = 888           # int 
# s = 45.5          # float
# d = True, False,None # boolean
# x = 15 
# print( x + False )
# a = type ()
# print(a)

# print( d )
# reak = 15
# print(reak)

d = {}
def tur(tur):
    for i in range(len(tur)):
        if type(i )== int:
            d.update ({"int" :i})
        elif type( i) == str :
            d.update({"str":i})
        elif type( i) == list :
            d.update({"list":i})
        elif type( i) == dict :
            d.update({"dikt":i})
        elif type( i) == float :
           d.update({"float":i})
    
tur("salom")
print(d)