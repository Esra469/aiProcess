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





