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


#import data
df=pd.read_csv("linear_regresion_dataset.csv",sep=";")#; ile 2 kısıma ayırdık
#df=pd.DataFrame(data,columns=['deneyim','maas'])
plt.scatter(df.deneyim,df.maas)
plt.xlabel("deneyim")
plt.ylabel("maas")
plt.show()

#%% linear regession

#sklearn library
from sklearn.linear_model import LinearRegression
linear_reg=LinearRegression()
#noktalar oluşturuldu
#x=df.deneyim#şu an type olarak pandas alıyor bir kolaylık olsun diye numpy e dönüştürmeliyz ->df.deneyim.values ile numpy olur
#x=df.deneyim.values#ama sklearn bu şekilde algılamıyor bunu (14,) olarak algılar 14,1 olarak ayarlamk lazım bunun için reshape yapıyoruz
x=df.deneyim.values.reshape(-1,1)
y=df.maas.values.reshape(-1,1)

linear_reg.fit(x,y)#mavi noktalar fit edildi

#%%prediction
b0=linear_reg.predict(0)
print("b0:",b0)

b0_=linear_reg.intercept_
print("b0_:",b0_)#y eksenini  kesitiği nokta

b1=linear_reg.coef_
print("b1:",b1)#eğim slope

#yukarıda verdiğimiz formulleri istendiğinde bu şeklde pythondan bulabiliriz














