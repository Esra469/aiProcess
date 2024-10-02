# -*- coding: utf-8 -*-
"""
PCA =principle component analysis
PCA nerelerde kullanılır
1)feature extraction
2)feature dimension
3)stock market prediction
4)gene data analysis

Biz daha çok feature dimension ile ilgileneceğiz ->Feature sayısını azaltmak
example) 10 boyutlu data PCA kullanarak 2 boyuta dönüştürüyoruz ve görselleştirme yapıyoruz 

higher dimension=>lower dimension
!!!  olabildiğince varyans büyük olmalı(bunun anlamı data kaybı olmaması aslında)

x ve y ekseni olan bir grafik üzerinden gidelim bu 2 boyutlu bir data demektir bunu tek boyutluya çekmek istersek:
2 boyutlu datamı PCA kullanarak 1 boyutluya düşürmek varyans(variance) maximum olacak

"""
from sklearn.datasets import load_iris#sklearn aynı zamanda kendi içinde dataset de barındırıyor
import pandas as pd

#%% 
iris=load_iris()

#iris içerisindeki değerleri atıyoruz
data=iris.data
feature_names=iris.feature_names
y=iris.target

df=pd.DataFrame(data,columns=feature_names)
df["sınıf"]=y

x=data
#%% PCA
from sklearn.decomposition import PCA
pca=PCA(n_components=2,whiten=True)#whitten=normalize n_components->kaç componente ayrılacağı belirlenir
pca.fit(x)#bu şekilde 4 boyutudan 2 boyutluya inen matematiksel modeli yaptık transform ile de dönüştüreceğiz

x_pca=pca.transform(x)

#yeni elde ettiğimiz data eski datanın ne kadarını temsil edebiliyor
print("variance ratio: ",pca.explained_variance_ratio_)#hangisinin principle hangisinin second olduğunu belirtir
print("sum: ",sum(pca.explained_variance_ratio_))

#%% 2D

#x_pca.shape -> (150, 2) 150 sample var zatn bildiğimiz çiçek bilgisi 2 boyuta indirgedik bu yüzden (150,2) yazıyor
df["p1"]=x_pca[:,0]
df["p2"]=x_pca[:,1]

color=["red","green","blue"]

import matplotlib.pyplot as plt
for each in range(3):
    plt.scatter(df.p1[df.sınıf==each], df.p2[df.sınıf==each], color=color[each],label=iris.target_names[each])
plt.legend()
plt.xlabel("p1")
plt.ylabel("p2")
plt.show()












