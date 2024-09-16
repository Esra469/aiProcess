# -*- coding: utf-8 -*-
"""
Linear regression
@author: ASUS
"""
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("linear_regresion_dataset.csv",sep=";")#; ile 2 kısıma ayırdık
#df=pd.DataFrame(data,columns=['deneyim','maas'])
plt.scatter(df.deneyim,df.maas)
plt.xlabel("deneyim")
plt.ylabel("maas")
plt.show()
#line fit ya da linear regression
#nasıl ilerlediğini göz önğnde bulundurarak ona göre bir doğru çizimi
"""
şu şekilde ilerler
y=b0+b1*x
b0=constant(bias)->doğrunun x eksinde kestiği noktaya denk gelir
b1=coeff->çizilen doğrunun eğimidir
maas=b0+b1*deneyim
"""

#linear regession 2
"""
y=b0+b1*x

#y_head->predict edilen deger oluyor doğru üzerinde 
residual=y-y_head->y nokta değeri y_head doğru üzerinde bir değer
noktaların yani y nin line nin altında veya üstünde olma durumuna göre negatif veya pozitif çıkabilriyor
bu şekilde olmaması için residual ın karesi alınıyır negatiflerden kurturuluyor

mean squared error->MSE=sum(residual^2)/n    n=sample(nokta )sayısı
amaç->min(MSE)
"""
