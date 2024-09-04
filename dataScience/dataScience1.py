
"""
Data Science
"""

import numpy as np
import pandas as pd
import seaborn as sns #visualization tool
import matplotlib.pyplot as plt

# from subprocess import check_output
# print(check_output(["ls", "../input")]).decode("utf8")

#çalıştığımız dataseti aldık ve inceledik
data=pd.read_csv("pokemon.csv")
data.info()


#correlation map
#2 tane feature arasında correation oranı 1 ise bunlar doğru orantılıdır demek->2 durumun birbiri ile alakası
#mesela evin oda sayısı artarsa fiyatı da artar bu değer 1 döner
#correlation map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()
#annot true->sayıların gözükmesi linewidths->aradaki line kalınlığı fmt->virgülden sonra 1 deger

data.head(10)#ilk 10 pokemon degerini verir
data.columns
#%% pokemonda lineplot eklemek
data.Speed.plot(kind='line',color='g',label='Speed',linewidth=1,alpha=0.5,grid=True,linestyle=':')
data.Defense.plot(color='r',label='Defense',linewidth=1,alpha=0.5,grid=True,linestyle='-')
plt.legend(loc='upper right')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Line plot')
plt.show()

#%% scatter plot
data.plot(kind='scatter',x='Attack',y='Defense',alpha=0.5,color='red')
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Attack defense scatter plot")
#%% Histogram
#kaç tane pokemonun hangi hızda oldugu analizi
data.Speed.plot(kind='hist',bins=50,figsize=(10,10))
plt.show()

plt.clf()#->yapılan grafiği siler
#%% Dictionary ->dic faster than lists
dictionary={'spain':'madrid','usa':'vegas'}
print(dictionary.key())
print(dictionary.values())

dictionary['spain']="barcelona" #spain i barcelona olarak update edecek
dictionary['france']="paris" #yeni bir entry eklemek için kullanılır
del dictionary['spain']#spaini siler
print('france' in dictionary) #true false döndürür

dictionary.clear() #temziler boş dic döndürür
#del dictionary ->direkt siler 

#%% pokemon datasetinde pandas kullanımı
# 1-filtering pandas data frame
x=data['Defense']>200#data içerisindeki defense degeri 200den yükske olan degerler
data[x]

#2-filtering pandas with logical_and
data[np.logical_and(data['Defense']>200,data['Attack']>100)] #her iki koşulu da sağlayan degerler
#şu şkeilde de belirtilebilri
data[(data['Defense']>200) &(data['Attack']>100)]

#%% while and for
lis=[1,2,3,4]
for i in lis:
    print('i is ',i)
print('')

#enumerate index ve value degerleri
for index,value in enumerate(lis):
    print(index,":",value)
print('')

#for dictionary
dictionary={'spain':'madrid','france':'paris'}
for key,value in dictionary.items():
    print(key,":",value)
print('')

#for pandas we can achive index and value
for index,value in data[['Attack']][0:1].iterrows():
    print(index," :",value)

    
     




















