# -*- coding: utf-8 -*-
"""
SVM Support vector machine

"""
"""



"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("data2.csv")
df.drop(["id","Unnamed: 32"],axis=1,inplace=True)

#Malignant=M kötu huylu timör
#Benign=B iyi huylu timör

M=df[df.diagnosis=="M"]
B=df[df.diagnosis=="B"]

#Scatter plot
plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kotu",alpha=0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="iyi",alpha=0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

"""
Burada object değerleri algorimada kullanabilememiz için sayısal değerlere dönüştürmek zorundayız bunun için normal ve hasta değerleri
0 ve 1 e sayısal olacak şekilde atama yapıyoruz 
"""
df.diagnosis=[1 if each =="M" else 0 for  each in df.diagnosis]
y=df.diagnosis.values
x_data=df.drop(["diagnosis"],axis=1)

#Normalization
x=(x_data-np.min(x_data))/np.max(x_data-np.min(x_data))

#train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

#%% SVM 
from sklearn.svm import SVC
svm=SVC(random_state=1)
svm.fit(x_train,y_train)

#%% test
print("print accuracy of svm algorithm: ",svm.score(x_test,y_test))


















