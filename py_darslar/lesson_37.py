# def strr(s):
#     d = 0
#     f = []
#     for i in s:
#         d += 1
#         if d % 3 == 0 :
#             f.append(i)
#     print(f)

# # g = "zxcvbnmlfkrtyttygth"
# # strr(g)

# def tur(tur):
#     d = {}
#     for i in tur:
#         if type(i )== int:
#             d.update ({"int" :i})
#         elif type( i) == str :
#             d.update({"str":i})
#         elif type( i) == list :
#             d.update({"list":i})
#         elif type( i) == dict :
#             d.update({"dikt":i})
#         elif type( i) == float :
#            d.update({"float":i})
#     print(d)
        
        



# d = ["assalom",15,"ok",22,[1,2,6],{"s":15},1.5,5.5]

# tur(d)

class integer:
    @classmethod
    def verifay_coord(cls,valyu):
        if isinstance(valyu,int):
            return True
        raise ValueError("hato")

    def __set_name__(self,owner,name):
       
        self.name = "__"+name
    
    def __get__ (self,instanse,owner):
        return instanse.__dict__[self.name]

    def __set__(self,instanse,valyu):
        instanse.__dict__[self.name] = valyu

class Point3D:

    x = integer()
    y = integer()
    z = integer()
    def __init__(self,x:int,y,z) :
        # Point3D.verifay_coord(x)
        # Point3D.verifay_coord(y)
        # Point3D.verifay_coord(z)
        self.x = x
        self.y = y
        self.z = z

p = Point3D(5,8,9)

# print(p.z)

    # @property
    # def x (self):
    #     return self.__x

    # @x.setter
    # def x (self,nev):
    #     Point3D.verifay_coord(nev)
    #     self.__x  = nev
    
    # @property
    # def y (self):
    #     return self.__y
    # @y.setter
    # def y (self,nev):
    #     Point3D.verifay_coord(nev)
    #     self.__y  = nev

    # @property
    # def z (self):
    #     return self.__z
    # @z.setter
    # def z (self,nev):
    #     Point3D.verifay_coord(nev)
    #     self.__z  = nev
    
    


# print(p._Point3D__z)

# print(p.z)

     