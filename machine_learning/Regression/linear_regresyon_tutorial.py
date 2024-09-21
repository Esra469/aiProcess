# -*- coding: utf-8 -*-
"""
Linear regression

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

#plot data
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

#:x.shape ->boyutu verir -> -1,1 mantığı 1 e böler -1,2 7,2 yazdırcak

linear_reg.fit(x,y)#mavi noktalar fit edildi

#%%prediction
b0=linear_reg.predict([[0]])
print("b0:",b0)

b0_=linear_reg.intercept_
print("b0_:",b0_)#y eksenini  kesitiği nokta

b1=linear_reg.coef_
print("b1:",b1)#eğim slope

print(linear_reg.predict([[11]]))#güncel predict bu şekilde oluşturuluyor

#yukarıda verdiğimiz formulleri istendiğinde bu şeklde pythondan bulabiliriz

#visualize line
array=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)#deneyim
plt.scatter(x,y)
plt.show()

y_head=linear_reg.predict(array)#maas predict degerleri
#line miz aşağıdaki sonucunda oluşturulacaktır
plt.plot(array,y_head,color="red")#x ekseni ve predict ettigimiz değerleri grafikte oluşturduk

linear_reg.predict([[10]])#ayrı ayrı istediğimiz şeyi predict edeblrz


#multiple linear regression->bir y eksenine birden fazla durumun etkilemesi
#simple linear reg->y=b0+b1*x
#multiple linear reg->b0+b1*x1+b2*x2 ->maas=b0+b1*deneyim+b2*yas
#maas= dependent variable
#deneyim,maas=independent variable
#b0 b1 b2=>amac=min(MSE)

df2=pd.read_csv("multiple_linear_regression.csv",sep=";")
x2=df2.iloc[:,[0,2]].values
y2=df.maas.values.reshape(-1,1)

multiple_linear_reg=LinearRegression()
multiple_linear_reg.fit(x2,y2)#bana bir tane x ve y kullanarak line fit edecek

print("b0:",multiple_linear_reg.intercept_)
print("b1,b2:",multiple_linear_reg.coef_)

#predict
multiple_linear_reg.predict(np.array([[10,35],[5,35]]))


#%% polynomial Linear regression

data=pd.read_csv("polynomial_regression.csv",sep=";")

x3=data.araba_max_hiz.values.reshape(-1,1)#sklearn learn kullanmak için values ve reshape yapıyorz numpy a dönüştürülüyor
y3=data.araba_fiyat.values.reshape(-1,1)

#visualize
plt.scatter(x3,y3)
plt.xlabel("araba_max_hiz")
plt.ylabel("araba_fiyat")
plt.show()

#linear regression->(y=b0+b1*x) and multiple linear regression->(y=b0+b1*x1+b2*x2)

#linear regrssion
lr=LinearRegression()
lr.fit(x3,y3)#olan samplelere en uygun line fit ediliyor

#predict
y_head=lr.predict(x3)

plt.plot(x3,y_head,color="red",label="linear")
plt.show()

lr.predict([[130]])#fit ettiğimiz degere gore hangi sonucu vereceğini buluyoruz

#bu çalışmada linear regressionun bizim işimize tam yaramadığını görüyoruz çünkü bizm problem linear değl polinomal artış gosteriyor

#%%polynomial Linear regression ->y=b0+b1*x+b2*x^2+...+bn*x^n

from sklearn.preprocessing import PolynomialFeatures
polynomial_regression=PolynomialFeatures(degree=2)#Burada degree artırdıkça polinom bir fonksiyon için doğruluk eğerisi de artacak 

x_polynomial=polynomial_regression.fit_transform(x3)#burada benim x imi karesel bir biçimde donuştur

#%% fit
linear_regression2=LinearRegression()
linear_regression2.fit(x_polynomial,y)

#visualize
linear_regression2.predict(x_polynomial)#x_polynamial kullanarak predict ediyoruz

plt.plot(x,y_head,color="green",label="poly")
plt.legend()
plt.show()



























