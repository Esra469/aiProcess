# -*- coding: utf-8 -*-
"""
Decision Tree
"""
#Burada regression nasıl yapılır algoritmayı nasıl kullanacağız
"""
CART: Classification and Regression Tree
information entropy e göre datayı split ediyoruz ->split etmek grafik olarak verilen bir data şeklini bölmek demektir

Belli bir grafiki information entropy ile split edip burada yes ve no  şeklinde bir tree oluşturuyoruz. tree nin üst 
bölmeleri koşul yapısı ille bağlı bir bakıma x1 x2 ve y gibi değerlere ayırıyoruz
x1 ve x2 featuresi y yi veriyor
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("",sep=";",header=None)
x=df.iloc[:,0].values.reshape(-1,1)
y=df.iloc[:,1].values.reshape(-1,1)

#%%decision tree regression
#2 Boyutlu dataset kullanarak tasarladık
from sklearn.tree import DecisionTreeRegressor
tree_reg=DecisionTreeRegressor() #random sate=0
tree_reg.fit(x,y)#ağaç modelini oluşturduk demek
tree_reg.predict(6)#6 için olan bir sonuç verecek data ya göre konrol edebilirz ne kadar doğru diye

x_=np.arange(min(x),max(x),0.01).reshape(-1,1)#Bu şekilde mix x den max x e kadar 0.01 artacak şekilde artacak 
y_head=tree_reg.predict(x)

#visualize
plt.scatter(x, y,color="red")
plt.plot(x,y_head,color="green")
plt.xlabel("tribun level")
plt.ylabel("ucret")
plt.show()



#%% Random Forest (ağaçların toplamı)
"""
ensemle  learning üyesi
ensemle learning

data->{n sayısa sample}-sub_data->tree1,tree2....->average->result



"""

data=pd.read_csv("random_forest_regression_dataset.csv",sep=";",header=None)#header none yaptık 1 ve 100 başlarda gözükmesin diye

x=data.iloc[:,0].values.reshape(-1,1)#Burada x eksenini seçtik iloc ile tüm satırları seçtik tüm satırlardan 1. sütünü aldık ve numpy için valeus e döndürdük
y=data.iloc[:,1].values.reshape(-1,1)

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators=100,random_state=42)#100 tane ağaç kullanılacak şekilde ayarlandı n_estimators ile random_state->bir daha run edildiğinde eskisi ile aynı sonucu verecek şekilde ayarlıyor
rf.fit(x,y)#x ve y ye göre bir line yani fit değeri aldık
rf.predict([[7.5]])#7.5 seviyesinde fiyatın ne seviyesinde olduunu göreceğiz

x_=np.arange(min(x),max(x),0.01).reshape(-1,1)#Burada x değerlerini aldım
y_head=rf.predict(x_)#aladığım x değerlerini y_head e atadım predict ettim

#visualize
plt.scatter(x, y,color="red")
plt.plot(x_,y_head,color="green")
plt.xlabel("tribun level")
plt.ylabel("ucret")
plt.show()



#%% Evaluation regression model ->çıkan sonuçların doğruluğu test edilir

























