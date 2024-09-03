
"""
Matplotlib.pyplot 
"""

#matplotlib
#görsellestirme kutuphanesi
#line plot,scatter plot,bar plot,subplots,histogram

import pandas as pd
df=pd.read_csv("iris.csv")
print(df.columns)

print(df.Species.unique())#species içinde kaç çeşit tür var bulmak için
print(df.info)#içerisindeki kolum ve valuelerşn bilgilerini verir

print(df.describe())
setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]

print(setosa.describe)#yukarıda verilere göre setosaların  datalarını analizleyeceğiz
print(versicolor.describe)#yukarıdakine göre versicoolor un datalarını analizleyeceğiz

print("---------------------------------------------------------------------------")
#%% Line plot
import matplotlib.pyplot as plt
df1=df.drop(["Id"],axis=1)
# print(df1.plot())
# print(plt.show())#görselleştirme 

#setosaya ait grafik
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa-PetalLengthCm")#nasıl grafik oluşturacagız
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="blue",label="verginice")#nasıl grafik oluşturacagız
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()#label yazdırılması
plt.show()#show görsel için her zman gerekli

df1.plot(grid=True,alpha=0.5)#bu şekidle grafik üzerinde grid oluşturmasını sağlar,alpha grafiklerin saydamlaşmasını sağlar
plt.plot()
print("---------------------------------------------------------------------------")
#%% scatter plot
#daah açok 2 tane featureyi karşılaştırmak içn kullanılır

setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
verginica=df[df.Species=="Iris-virginica"]

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")#scatter dot oluştmrasını sağlar
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(verginica.PetalLengthCm,verginica.PetalWidthCm,color="purple",label="verginica")

plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

#%% Histogram

plt.hist(setosa.PetalLengthCm,bins=10) #bins verilern grafikte kalınlığı belirler
plt.xlabel("PetalLengthCm value")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

print("---------------------------------------------------------------------------")
#%% Bar plot
import numpy as np

#x ve ye eksenlerinde verilene göre bir grafik oluşturur
# x=np.array([1,2,3,4,5,6])
# y=x*2+5
# plt.bar(x,y)
# plt.title("bar plot")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

x=np.array([1,2,3,4,5,6])
a=["turkey","use","a","b","c","d"]
y=x*2+5
plt.bar(a,y)
plt.title("bar plot")
plt.xlable("x")
plt.ylable("y")
plt.show()
print("---------------------------------------------------------------------------")
#%% sub plot
df1.plot(grid=True,alpha=0.9,subplots=True)
plt.show()

setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
verginica=df[df.Species=="Iris-virginica"]

plt.Subplot(2, 1, 1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa")
plt.ylabel("setosa-PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")
plt.ylabel("versioncolor-petalLengthCm")

print("---------------------------------------------------------------------------")
#%%

