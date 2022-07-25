
def check_numbers(x,y):
    if x.strip().isdigit() and y.strip().isdigit():
        print(int(x)+int(y))
    else:
        print("hato lik bor x va y son bolishi kerak ")

d ="15"
a = "45"
check_numbers(a,d)


def main():
    # print("main func")
    1+1
    return True
result=main()

print(result)



s = "salom".count("a")
print(s)



def check_numbers(a,b,c):
    print(a,b,c)
    return 55 

x ="15"
y = "45"
c = 155
check_numbers(x,y,c)

import random
def generator_random_list(limit):
    return list(random.sample(range(0,100),limit))
     
s=generator_random_list(50)
print(s)


 

def generator_random_list(limit):
    l = []
    while True:
        if len(l)==limit:
            break 
        r = random.randint(0,100)
        if r not in l:
            l.append(r)
    return l 
s=generator_random_list(50)
print(s)


def jamlash(a,b,c):
    if type(a) == list and type(b)== list and type(c)==list:
        return a + b + c
    else:
        return "a b c list bolishi keraks"

list_1 = ["ok","py","non"]
list_2 = [ 15,55,66,66,]
list_3 = [[5],["python"],[88]]

s = jamlash(list_1,list_2,list_3)
print(s)


def month_name(maonth_number):
    moth = {1:"yanvar",2:"febral",3:"mart",4:"apral",
    5:"may",6:"iyyun",7:"iyyul",8:"avgust",
    9:"sentiyabir",10:"aktiyabir",11:"noyabir",12:"dekabir"}
    print(moth[maonth_number])
   
month_name(1)



"""  """
def students_append(talaba_dict,limit):
    s={}
    malumot = ["isim","familya","age"]
    if limit >0:
        last_id = list(talaba_dict.keys())[-1].split("#")[-1]
        last_id = int(last_id)
        for i in range(limit):
            talaba_dict[f"student#{last_id}"]={}
            talaba_dict[f"student#{last_id}"]["ism"]=input("isim")
            talaba_dict[f"student#{last_id}"]["familya"]=input("familya")
            talaba_dict[f"student#{last_id}"]["age"]=input("age")
            last_id+=1
    return talaba_dict       
       
student ={
       "talaba#55": {"name":"oyatulloh","surname":"karimberdiev","age":33
       }}
a=students_append(student,2)
print(a)
print("salom dumyo")