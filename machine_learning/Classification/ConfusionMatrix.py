# -*- coding: utf-8 -*-
"""
Confusion matrix 
"""

import pandas as pd
import numpy as np

data=pd.read_csv("data2.csv")

data.drop(["id","Unnamed: 32"],axis=1,inplace=True)#gereksiz columslerı silemeye yarıyor inplace=True -> değişikliiği yapıp veriye kaydetmeye yarıyor    

data.diagnosis=[1 if each=="M" else 0 for each in data.diagnosis]#data.diagnosis i 1 ve 0 olarak ayarlayacak
y=data.diagnosis.values
x_data=data.drop(["diagnosis"],axis=1)#diagnosis ait olan colums çıkarıldı x_data ya atıldı


#%% Normalization
x=(x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data))
#%% train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15,random_state=42)


from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=100,random_state=1)
rf.fit(x_train,y_train)
print("random forest algo result: ",rf.score(x_test,y_test))

y_pred=rf.predict(x_test)
y_true=y_test

#%% confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_true, y_pred)

#%% cm visualization

import seaborn as sns
import matplotlib.pyplot as plt 
f,ax=plt.subplots(figsize=(5,5))
sns.heatmap(cm,annot=True,linewidths=0.5,linecolor="red",fmt=".0f",ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()

"""
Hangi değer aslında doğru iken yanlış olarak tespit edildiği, hangi değer aslında yanlış iken doğru olarak tespit edildiği konusunda bize 
bir analize verir ve bu analizi görselleşitrebilme olanağı sağlar.

"""

















