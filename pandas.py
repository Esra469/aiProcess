# -*- coding: utf-8 -*-
"""
Pandas
"""
#pandas hizli ve etkili dataframe
#dosya arasinda geçiş kolaydır
#pandas missing data için işi kolaylaştırıyor
#reshape yapıp datayı daha etkili ibr şekilde kullanabilirz
#slicing indexing kolay
#time series data anlizinde çok etkili
#hiz açısından optimize edilmş bir library

import pandas as pd
dictionary={"Name":["Ali","mehmet","Esra","esma","yusuf"],
            "AGE":[10,24,18,34,32],
            "Maas":[100,200,300,400,500]}
dataFrame1=pd.DataFrame(dictionary) #bize DataFrame oluşturmamızı sağlar

head=dataFrame1.head() #baştan 5 tane satırı bize ver demek
tail=dataFrame1.tail() #sondan 5 tane satırı bize verir
print("---------------------------------------------------------------------------")
#%% pandas basic method
print(dataFrame1.columns) #kolonarı bize verir ,filtreleme yapmak için işimize yarayacak

print(dataFrame1.info()) #bize oluşturduğumuz dataframeden belli başlı infolar verir
print(dataFrame1.dytpe)#her bir column için tür verir
print(dataFrame1.descrie())#numeric feature=columns (age,maas)  analizyebileceği verileri tarar bu yüzden bizde burada maas ve age alacak

print("---------------------------------------------------------------------------")
#%% indexing and slicing
print(dataFrame1["Name"])
print(dataFrame1.AGE)

dataFrame1["yeni feature"]=[-1,-2,-3,-4,-5]#ismi boşluk atarak yazmak mantıklı olur
print(dataFrame1.loc[:,"AGE"])#Tüm satırlar ve istediğim sütün
#pandas da 0:3e demek 3 ü de dahil olarak alır
print(dataFrame1.loc[:3,"AGE":"Name"])
print(dataFrame1.loc[::-1,:])#daha önce yazdığımız dataFrameyi ters döndürür
print(dataFrame1.loc[:,:"Name"])#tüm sütünlardan ilk satır isimleri verir,obje alabiliyor

print("---------------------------------------------------------------------------")
#%% filtering
#sql gibi veriyi direkt almak gibi çalışıyor /aslında true false gibi
filtre1=dataFrame1.Maas>200
filtrelenmis_data=dataFrame1[filtre1]

filtre2=dataFrame1.AGE<20
dataFrame1[filtre1,filtre2]#2 filtreyi birleştirmeye yarıyor

print("---------------------------------------------------------------------------")
#%% list comprehension
import numpy as np
ortalama_maas=dataFrame1.Maas.mean()
#ortalama_maas_np=np.mean(dataFrame1.Maas)

dataFrame1["maas_seviyesi"]=["dusuk" if ortalama_maas>each else "yuksek" for each in dataFrame1.Maas]

# for each in dataFrame1.Maas:
    # if(ortalama_maas>each):
    #     print("dusuk")
    # else:
    #     print("yuksek")
    
dataFrame1.columns=[each.lower() for each in dataFrame1.columns]#dataframe isimlerinin hepsinin harflerini küçültür

print("---------------------------------------------------------------------------")
#%% drop and concatenatting

dataFrame1.drop(["yeni feature"],axis=1,inplace=True)#yeni featurenin sutununu alır atar
#dataFrame1=dataFrame1.drop=(["yeni feature"],axis=1)->yukarıdaki ile aynı işlev
        
data1=dataFrame1.head()
data2=dataFrame1.tail()
#vertical ->yukarıdan ağı birleştirme
data_concat=pd.concat([data1,data2],axis=0)

#horizonal
maas=dataFrame1.maas
age=dataFrame1.age
data_h_concat=pd.concat([maas,age],axis=1)

print("---------------------------------------------------------------------------")
#%% Transforming data
dataFrame1["list_comp"]=[each*2 for each in dataFrame1.age]

#apply
def multiply(age):
    return age*2

dataFrame1["apply_method"]=dataFrame1.age.apply(multiply)  

print("---------------------------------------------------------------------------")  
#%%
    
















