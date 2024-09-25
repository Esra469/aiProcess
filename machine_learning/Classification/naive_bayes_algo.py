# -*- coding: utf-8 -*-
"""
Naive Bayes algorithm

"""
"""

deneyim ve maasa gore bir tablo düşün bu tabloda mavi ve kırmızı noktalar fizik ve math öğretmenliğini gösteriyor olsun herhangi
bir noktanın fizik mi yoksa math hocası mı olduğunu belirlemek için kullanılır bu algoritma

P(Math|X)=(P(X|Math)*P(Math))/P(X)
P(Math|X)->probablity of math teach olma x e göre
P(X|Math)->likelihood()->daire içerisindeki o yüzdeliği
P(Math)->tüm değerlerdeki yüzdeliği->prior probability
P(X)->marginal likelihood

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("data2.csv")

data.drop(["id","Unnamed: 32"],axis=1,inplace=True)
# malignant= M kötü huylu timör
# benign= B iyi huylu timör

M=data[data.diagnosis=="M"]
B=data[data.diagnosis=="B"]

#scatter plot
plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kotu",alpha=0.3)
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="iyi",alpha=0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()


data.diagnosis=[1 if each =="M" else 0 for each in data.diagnosis]
y=data.diagnosis.values
x_data=data.drop(["diagnosis"],axis=1)


#Normalization
x=(x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data))

# train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

#Naive bayes
from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(x_train,y_train)

print("print accuracy of naive bayes algo",nb.score(x_test,y_test))





















