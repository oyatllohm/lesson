
# def d (a):
#     r = ""
#     for i in a :
#         if i.isdigit() and i != "0":
#             r +=i
#             if len(r)==4:
#                 break
#     return int (r)if len(r)== 4 else False

       



# s = "asa0s8s7g1kk02vv3zv"
# print(d(s))
from time import *
import datetime
t = time() - 24 * (60 * 60)
s = time()
res = datetime.date.fromtimestamp(s)
# print(res)


import datetime

from time import time
# print(dir(datetime))
date = datetime.date(2022,1,4)
date2 = datetime.date(2022,1,7)
timedelta = datetime.timedelta(seconds=1)

res = date +  timedelta
res2 = date -  timedelta
print(date)
print((timedelta))
print(res2)
