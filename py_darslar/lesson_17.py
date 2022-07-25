l = ["ol",'li',"ul","ul","h1"]

d = l[1:3].copy()
l.clear()
print(l)
print(d)

a = 777
l.append(a)
l.extend(["i","p","pre"])
l.insert(0,"table")
s = l.index("ul")
a = l.count("ul")
b = l.remove("ul")
print(b)
print(l)



print(l)
l.pop(1)

a = list(range(100,200))
b = [ i for i in range(100,201) if i % 2 == 0 ]

a = []
for i in range(100,201):
    if i%2 == 0 :
        a.append(i)
print(a)


list1 = [1,5,9,88,55,66,2,77,59]
list2 = [11,55,99,88,59,66,55,77,55,1]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)

list3.sort()
list3.sort(reverse=False)
print(list3)

a = ["non", "olma" ,"anjir"]
a.sort(reverse=False)
print(a)

a  = -1
f = [10,-1,15,8,-9,15,-7]
for i in f:
    a+=1
    if i < 0:
        f.pop(a)
        f.insert(a,0)
print(f)

a = 10 
if a > 0 a +=1 else a -=5

print(a)