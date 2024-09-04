# -*- coding: utf-8 -*-
"""


"""
import pandas as pd

def tuple_ex():
    t=(1,2,3)
    return t
a,b,c=tuple_ex()
print(a,b,c)

#built in scope: name in predefined built in scope module such as print ,len
import builtins#python tarafından sağlanan tüm scoplar variable ismi olarak yazılmaz
dir(builtins)

#%% nested function ->iç içe fonksiyonlar
def square():
    def add():
        x=2
        y=5
        z=x+y
        return z
    return add()**2
print(square())

#def f(a,b=2)-> b=2 is default argument
#def f(*args)->args can be one or more
#def f(**kwargs)->kwargs is a dictionary

def f(**kwargs):
    for key,value in kwargs.items():
        print(key," :",value)
f(country='spain',capital='madrid',population=1234)

#lambda function
square=lambda x:x**2
print(square(4))
tot=lambda x,y,z:x+y+z
print(tot(1,2,3))

#anonymus function
number_list=[1,2,3]
y=map(lambda x:x**2,number_list)#number_list içerisindeki değerlerin herbiirnin karesini alıyor
print(list(y))

#iterators

name="Esra"
it=iter(name)
print(next(it))#ilk harfi verir
print(*it)#ilk harften sonraki harfler

#zip example
list1=[1,2,3,4]
list2=[5,6,7,8]
z=zip(list1,list2)
print(z)
z_list=list(z)
print(z_list)
#sonuc->(1,5),(2,6),(3,7),(4,8)

un_zip=zip(*z_list)
un_list,un_list2=list(un_zip)
print(un_list)#(1,2,3,4)
print(un_list2)#(5,6,7,8)
print(type(un_list2))

#list comprehension
num1=[1,2,3]
num2=[i+1 for i in num1]
print(num2)
#num1 ->iterable
#i->iterator

#conditional on iterable
num1=[5,10,15]
num2=[i**2 if i==10 else i-5 if i<7 else i+5 for i in num1]
print(num2)

#%%  list comprehension with pokemon dataset
data=pd.read_csv("pokemon.csv")
threshold = sum(data.Speed)/len(data.Speed)
print(threshold)
data["speed_level"] = ["high" if i > threshold else "low" for i in data.Speed]
data.loc[:10,["speed_level","Speed"]]#buradan detayları alacağız









    
