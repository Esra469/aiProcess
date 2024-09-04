# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:27:08 2024

@author: ASUS
"""
#Diagnosa data for cleaning
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("pokemon.csv")
print(data['Type 1'].value_counts(dropna=False))#tiplere göre kaç tane pokemon oldugunu yazar
data.describe()

#%% visual exploraty data analysis
#Box plot->
data.boxplot(column='Attack',by='Legendary')
plt.show()

# Tidy data(melting)
data_new=data.head()
#lets melt ->datada yeni feature çıkarmak
#melt edilecek frame, melt edilecek sutun yeni variable ve  value değerleri için atanacak değerler
melted=pd.melt(frame=data_new,id_vars='Name',value_vars=['Attack','Defense'])

#Pivoting Data ->Reverse of melting
melted.pivot(index='Name',columns='variable',values='value')

# Concatenating data
data1=data.head()
data2=data.tail()
conc_data_row=pd.concat([data1,data2],axis=0,ignore_index=True)#data1 ve data2 dikey concat et
conc_data_row

# horizona concat->yatay birleştirme yapar
data1=data['Attack'].head()
data2=data['Defense'].head()
conc_data_col=pd.concat([data1,data2],axis=1)#add dataframe in column
conc_data_col

#data.dtypes-> columların türlerini verir

# data type
data['Type 1']=data['Type 1'].astype('category')
data['Speed']=data['Speed'].astype('float')#convert ettik gibi oldu prprocess
data.dtypes

# missing data
#bir datada daha önce tanımlanmayan değeri olmayana şeyler
data["Type 2"].value_counts(dropna=False)#type 2 nin her değerden kaçar tane oldugunu göster dropna=false->nan degerleri de göster

data1=data
data1['Type 2'].dropna(inplace=True)#nan onları drop et ama alma

assert 1==1 #dediğimizde hata vermiyorsa yaptığımız işlemler doprudr demek
assert data['Type 2'].notnull().all() #return nothing because we drop nan values

data['Type 2'].fillna('Empty',inplace=True)
assert data['Type 2'].notnull().all() #return nothing because we drop nan values







 



