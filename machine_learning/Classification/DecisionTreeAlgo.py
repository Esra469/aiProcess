# -*- coding: utf-8 -*-
"""
Decision Tree

"""
"""
Random forest->ensamle learning modeli->şunun gibi 10 tane decision tree olsun bu treeler birleşince ortaya bir 
algoritma çıkar buna da random forest denir(ensamle learning örneği)

data aynı şekilde train ve test olarak ayrılıyor train üsütnde deneme yapılıyor test üzeridnen veri gönderip doğruluğu analizleniyor

NOT->Normalizayon işlemi train_test_slip yaptıktan sonra yapılmalı yoksa doğruluk değerleri hatalı çıkar
"""

import pandas as pd
import numpy as np

data=pd.read_csv("data2.csv")

data.drop(["id","Unnamed: 32"],axis=1,inplace=True)#gereksiz columslerı silemeye yarıyor inplace=True -> değişikliiği yapıp veriye kaydetmeye yarıyor    

data.diagnosis=[1 if each=="M" else 0 for each in data.diagnosis]#data.diagnosis i 1 ve 0 olarak ayarlayacak
y=data.diagnosis.values
x_data=data.drop(["diagnosis"],axis=1)#diagnosis ait olan colums çıkarıldı x_data ya atıldı


#%% train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.15,random_state=42)

#%% Normalization
x=(x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data))
#%% Decision tree
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)

print("score ",dt.score(x_test,y_test)) #Burada score 1 buluyorsun tekrardan kontrol et

#%% random forest 
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=100,random_state=1)
rf.fit(x_train,y_train)
print("random forest algo result: ",rf.score(x_test,y_test))#score x_test ve y_test i karşılaştırarak bir doğruluk değeri yani accuracy değeri veriyor


"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Veri yükleme ve gereksiz sütunları kaldırma
data = pd.read_csv("data2.csv")
data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)

# Diagnosis'i 1 ve 0 olarak dönüştürme
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis=1)

# Train-test split (önce ayırma yapıyoruz)
x_train, x_test, y_train, y_test = train_test_split(x_data, y, test_size=0.15, random_state=42)

# Normalizasyonu her set için ayrı ayrı yapıyoruz
x_train = (x_train - np.min(x_train)) / (np.max(x_train) - np.min(x_train))
x_test = (x_test - np.min(x_test)) / (np.max(x_test) - np.min(x_test))

# Decision Tree Model
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
print("Decision Tree score:", dt.score(x_test, y_test))

# Random Forest Model
rf = RandomForestClassifier(n_estimators=100, random_state=1)
rf.fit(x_train, y_train)
print("Random Forest score:", rf.score(x_test, y_test))


"""








