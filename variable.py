"""
Python basic kodlar
"""
#variable 
#function
#object

#%% #->Kodu parça parça bölmek için kullanılır
var1=10 #integer
var2=15
gun="carsamba"#string
var3=10.0 #double

print("---------------------------------------------------------------------------")
#%%

#String
s="Bugun gunlerden cuma"
variable_type=type(s)

#String ifadeler yanyana yazılarak topkanmış gibi olur "100"+"200" =>100200 gibi sonuç verecektir.
var1="Ankara"
var2="Balikesir"
var3=var1+var2

uzunluk=len(var3)

print("---------------------------------------------------------------------------")
#%% numbers

integer_number=-40
#double-float ->ondalikli sayilar
float_number=-30.9

print("---------------------------------------------------------------------------")

#%% built-in function
#round ->sayiyi yukari yuvarlama
float1=12.3
#float(12)
#int(float1)
#round(float1)


print("---------------------------------------------------------------------------")
#%% user defined function

var1=10
var2=100
output=(((var1+var2)*50)/100.0)*var1/var2

#kolay yoldan işlem yapmak için function tanımlıyoruz
def toplam(var1,var2):
    """
    burada 2 değer alinacak ve işlem yapilacak
    parametreler var1 ve var2
    
    return toplam değerleri döndürecek
    
    """
    return var1+var2

sonuc=toplam(3,4)

print("---------------------------------------------------------------------------")
#%% default and flexiable function

#çemberCevreUzunlugu=2pir
#default parametreler ortaya yazilmaz
def cember_cevre(r,pi=3.14):
    """
    Cember cevre hesapla
    input(paramter): r ,pi
    output=cember cevresi
    """
    output=2*pi*r
    return output

#flexible
#Bu şekilde bir tanimlama istediğimiz değerde parametre girmemiz yardimci olur

def hesapla(boy,kilo,*args):
    print(args)
    output=(boy+kilo)*args[0]
    return output

#def hesapla(boy,kilo,yas):
#    output=(boy+kilo)*yas
#    return output
print("---------------------------------------------------------------------------")
#%% Soru1
def x(y):
    y=y+[2]
    print(y)   
c=[1,2,3]
x(c)

print("---------------------------------------------------------------------------")
#%% Soru2
def s(x, y = 2):
    c = 2
    for i in range(y):
        c = c + x
    return c
s(2)

print("---------------------------------------------------------------------------")
#%%lambda function
def hesapla2(x):
    output=x*x
    return output
sonuc=hesapla(3)

sonuc2=lambda x:x*x
print(sonuc2(3))
print("---------------------------------------------------------------------------")

#%% list

liste= [1,2,3,4,5,6]
type(liste)
    
liste_str=["ptesi","sali","cars"]
type(liste_str)

value=liste[1]
valu2=liste_str[2]
value3=liste[-1]#sondan indexi almak için kullanilir
value4=liste[0:3] #0 1 2 al 3. indexi alma demek

dir(liste)#Bu bize listede bulunan kullanilabilen fonksiyonlari veriyor

#örnek kullanim
help(list.append)#appendin nasıl kullanildigini gosterir
stirng_int_list=[1,2,3,"a","b"]
print("---------------------------------------------------------------------------")
#%% tuple

t=(1,2,3,4,5,6)

dir(t)#bu sekilde fonksiyonlari gorebiliriz
t.count(3)#kaç tane 3 oldugunu dondurur
t.index(3)#3 bulundugu yeri verir
print("---------------------------------------------------------------------------")
#%% Dictionary
#local database gibi
dictionary={"ali":32,"veli":40,"ayse":18}
#ali,veli,ayse=key
#32 40 18 =values
dictionary.key() #bize keyleri verir .values de değerleri verir

print("---------------------------------------------------------------------------")
#%%
#if-else statement
var1=40
var2=50

if(var1>var2):
    print("var1 büyüktür var2")
elif(var1==var2):
    print("var1 ve var2 eşittir")
else:
    print("var1 küçüktür var2")


#bir örnek
liste=[1,2,3,4,5]
value=2
if value in liste:
    print("evet {} değer listenin içinde".format(value))
else:
    print("hayır değil");
    
print("---------------------------------------------------------------------------")
#%% for loop
for each in range(1,11):
    print(each)
for each in "ankara ist".split():
    print(each)
liste=[1,45,32,4,6,7,22]

summation=sum(liste)

count=0
for each in liste:
    count=count+each
    print(count)
    
print("---------------------------------------------------------------------------")
#%% while loop
i=0
while(i<4):
    print(i)
    i=i+1
sinir=len(liste)
each=0
count=0
while(each<sinir):
    count=count+liste[each]
    each=each+1
print("---------------------------------------------------------------------------")
        




    















