# -*- coding: utf-8 -*-
"""
Pandas Foundation
"""
#single column=series
#NaN=not a number
#dataframe.values=numpy

import pandas as pd
import matplotlib.pyplot as plt
country=["Spain","France"]
population=["11","12"]
list_label=["country","population"]
list_col=[country,population]
zipped=list(zip(list_label,list_col))
data_dict=dict(zipped)#zip i dictionary e donusturduk
df=pd.DataFrame(data_dict)#csv forması açamk ile aynı sayılır, dosya açıyoruz
df
#boradcasting=yeni bir column eklemek ve değerler girmek
df["capital"]=["madrid","paris"]
df["income"]=0 #yeni bir column ekledik ve 0 atadık hepsini

#visual exploratory data analysis->plot,subplot,histogram
data=pd.read_csv("pokemon.csv")
data1=data.loc[:,["Attack","Defense","Speed"]]#attack defense ve speed aynı garfik üzerinde plot çizildi
data1.plot()
#ayrımak için subplot
data1.plot(subplots=True)
#scatter
data1.plot(kind='scatter',x='Attack',y='Defense')
#histogram->frekans ölçer
data1.plot(kind='hist',y='Defense',bins=50,range=(0,250),normed=True)#normed->frekansları normalize eder

fig,axes=plt.subplots(nrows=2,cols=1)
data1.plot(kind='hist',y="Defense",bins=50,range=(0,250),normed=True,ax=True)
data1.plot(kind='hist',y="Defense",bins=50,range=(0,250),normed=True,ax=True,cumulative=True)#cumulative->en baştan itibaren veri toplayarak gider
plt.savefig('graph.png')
plt

#indexing pandas time
# 0 1 2 3 4 şekilde devam eden datalar için özelleşmil pandas yapıları var
#datatime dönüştürme
time_list=["1992-03-08","1992-04-12"]
print(type(time_list[1]))
datatime_object=pd.to_datetime(time_list)
print(datatime_object)

import warnings
warnings.filterwarnings("ignore")
data2=data.head()
data_list=["1992-01-02","1992-01-02","1992-02-10","1992-03-05","1992-03-10"]
datatime_object=pd.to_datetime(data_list)
data2["date"]=datatime_object
data2=data2.set_index("date")
data2
#artık zamana bağlı bir datamız var

print(data2.loc['1992-01-02'])#loc datanın içindeki bellir bir indexi çekmeye yarımcı olur

#resampling pandas time
data2.resample("A").mean()#yıllara göre ayrım
data2.resample("M").mean()#aylara göre ayrım
#interpolate->lineler ile araları doldurmak
data2.resample("M").first().interpolate("linear")
#mesela 3 ve 4 arasında boluk varsa 3 ve 4 arasını aralıklara böler orayı da linear şekilde doldurur
data2.resample("M").mean().interpolate("linear")

 








