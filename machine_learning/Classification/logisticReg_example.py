
"""
Logistic regression

https://www.kaggle.com/code/kanncaa1/deep-learning-tutorial-for-beginners

"""
#Logistic regression->en küçük neural network
#computation graph->matematiksel ifadeleri görselleştirmek için
"""
parametre=weight and bias
Bir görsellde her bir resim için piksel tarar her bir pikseli weights ile çarpar bunun sonucu sum bulunur ve  bias eklenir
daha sonra z değeri bulunur ve bu Sigmoid functiona eklenir  burdadan predict yani y_head değerlier bulunur output is probability 
deger çıkar bir trash belirlenmiştir bunda göre y_head deeğerine bakılır ve sonuç doğruluguna bakılır. Tüm resimler için yine sondan gidilere
bu sefer de fonksionun türevi alına alına gider bu şekilde tüm resim analizlenmiş olur


initializing parametres->Belli değerler seçilir bu değerleri kontorl et

Forward Propagation->loss function->-(1-y)log(1-y')-ylogy'->Bir deger verilir bu degerin doğrulugu degerlendirilir verilen resim ve çıktı aynı ise loss değeri 0 çıkar 
                                              farklı ise 1 çıkar
cost Function->hata maliyeti ->loss sonucu çıkan 0 ve 1 değerleri toplamı çok büyük olursa-> 
amaç cost functionun buyuk bir deger çıkmaması ->cost degeri çok çıkması halinde weight ve bias değerleri güncellenmeli
Sigmoid Function->Loss(error) function->Cost Function

Optimization Algorithm with Gradient Descent
Backward propagation->Biz weigth değeri bulunur fonksşyonua göre ve buluduğumzu degeri cost a yaklantırmak için uğraşırız bu uğraşı da fonksiyon üzerinde bulunan
 weight değerlerini türevini alarak yaparız. ->Bu şekilde weigth değerlerimizi güncelliyoruz->cost functionu weight a göre türevini alıyoruz eğim=slop
 o anki weight a göre slop bulunudu bulunan slop weight dan çıkarldı weigth güncellendi güncel weight ile yeni slop bulundu
 w:=w-a*(türev cost(w,b)) a=learning rate->öğrenme hızı->hyperparameter->öne seceksin sonra deneyeceksin
 

"""
#Timör dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("data.csv")
data.info()
data.drop(["Unnamed: 32","id"],axis=1,inplace=True)#isimsiz ve işimzie yaramayan sutunu sildik bu axis=1 dedik o sutuna ait olan tüm satırları da sildi inplace=True diyerek dediğimiz işlemleir yaptı ve data ya kayıt etti demek
data.diagnosis=[1 if each=="M" else 0 for each in data.diagnosis]#iyi huylu timörleri 1 kötü huylu timörler 0 yap

y=data.diagnosis.values#numpy array oldu
x_data=data.drop(["diagnosis"],axis=1)

#Normalization->0 ve 1 arasıda scale etmek
x=(x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data))#.values#Bu şekilde normalizasyon yapmış oldu->Tüm değerleri 1 ve 0 a döndürüldü
#

#%% Dataset train and Test split
#Train test split
from sklearn.model_selection import train_test_split
#x_train ve y_train logistic regression için ayrıldı x_test ve y_test ile de bunlar üsütnde deneme yapılacak
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)#test_size=verilen deger yüzde kaça kaç bölündüğnü gösterir

x_train=x_train.T
x_test=x_test.T
y_train=y_train.T
y_test=y_test.T

print("x_train:",x_train.shape)
print("x_test:",x_test.shape)
print("y_train:",y_train.shape)
print("y_test:",y_test.shape)

#%%Parameter initialize and sigmoid Function
def initialze_weights_and_bias(dimension):
    w=np.full((dimension,1),0.01)#dimensionu 1 lerden oluşan bir weight matrixi yap demek 0.01 atıyoruz 0 atamayız çünkü her değeri 0 ile çarpıp 0 dönmesine neden olacak
    b=0.0 #bias değeri
    return w,b
w,b=initialze_weights_and_bias(30)

"""
sigmoid Funciton -> F(x)=1/(1+e^-(x)) ->x olarak z yi yazıyoruz bu sefer
"""
def sigmoid(z):
    y_head=1/(1+np.exp(-z))
    return y_head

#sigmoid(0) ->gelen değeri görüyoruz 
#yukarıda weightlerimizi initialize ettik

#implementing Forward and Backward
def forward_backward_propagation(w,b,x_train,y_train):
    #forward propagation
    z=np.dot(w.T,x_train)+b
    y_head=sigmoid(z)
    loss=-y_train*np.log(y_head)-(1-y_train)*np.log(1-y_head)
    cost=(np.sum(loss))/x_train.shape[1]#bir değeri sample ile bölmek değeri normalleştirmek demektir x_train.shape[1] is for scaling
    #backward propagation
    derivation_weight=(np.dot(x_train,((y_head-y_train).T)))/x_train.shape[1]#x_train.shape[1] is for scaling
    derivation_bias=np.sum(y_head-y_train)/x_train.shape[1] #x_train.shape[1] is for scaling
    gradients={"derivative_weight":derivation_weight,"derivative_bias ":derivation_bias}#Burası dictioanry ->parametreleri depolamak için kullanılıyor
    return cost,gradients
"""
2 matis çarpıldığında 1. matrisin columu ve 2. matrisin row u birbirine eşit olmalı bundan dolayı genelede ilk matrisin Transpozu alınır(T) 
"""

#implementing update Parameters
#ileri ve geri gitmek bir iterasyon demektir bu zamanda w ve b update ediliyor
def update(w,b,x_train,y_train,learning_rate,number_of_iteration):#number_of_iterator döngünün n ekadar forward ve backward propoagto yaptğışı blirtiyor
    cost_list=[]
    cost_list2=[]
    index=[]
    
    #updating(learning) parameters is number_of_iteration times
    for i in range(number_of_iteration):
        cost,gradients=forward_backward_propagation(w, b, x_train, y_train)
        cost_list.append(cost)
        #lets update
        w=w-learning_rate*gradients["derivative_weight"]#weigth eşittir öğrnme hızı-learing weght a göre türevi demek aslında bu
        b=b-learning_rate*gradients["derivative_bias"]#bias için de aynı
        if i % 10==0:
            cost_list2.append(cost)#her 10 adımda bir cost_list2 ye o costlar atılıyor
            index.append(i)
            print("Cost after iteration %i: %f"%(i,cost))
    
    #we update(learning ) parameteres weight and bias
    parameteres={"weight":w,"bias":b}#w ve b paramterleri paramters de depoluyruz bu br dict
    plt.plot(index,cost_list2)
    plt.xticks(index,rotation='vertical')
    plt.xlabel("Number of iteration")
    plt.ylabel("Cost")
    plt.show()
    return parameteres,gradients,cost_list

#implemeting prediction
def predict(w,b,x_test):
    #x_test is a input for forward propagation
    z=sigmoid(np.dot(w.T,x_test)+b)#np.dot bildiğimiz matris çarpımı gibi işloyr +b de bias değeri ekliyor
    y_prediction=np.zeros(1,x_test.shape[1])#0 lardan oluşan bir prediction oluşturuduk daha sonra bunu dolduracağız aşağıdaki if koşulunda
    #if z is bigger than 0.5, our prediction is sign one (y_head=1),
    #if z is smaller than 0.5, our prediction is sign zero (y_head=0),
    for i in range(z.shape[1]):
        if z[0,i]<=0.5:
            y_prediction[0,i]=0
        else:
            y_prediction[0,i]=1
    return y_prediction

#implementing Logistic regression
def logistic_regression(x_train,y_train,x_test,y_test,learning_rate,num_iteration):
    #initialize
    dimension=x_train.shape[0]
    w,b=initialze_weights_and_bias(dimension)
    #do not change learning rate
    parameters,gradients,cost_list=update(w,b,x_train,y_train,learning_rate,num_iteration)
    y_prediction_test=predict(parameters["weight"], parameters["bias"], x_test)
    y_prediction_train=predict(parameters["weight"],parameters["bias"],x_train)
    
    #print train/test Errors
    print("train accuracy: {] %".format(100-np.mean(np.abs(y_prediction_train-y_train))*100))
    print("test accuracy: {} %".format(100-np.mean(np.abs(y_prediction_test-y_test))*100))
    
logistic_regression(x_train, y_train, x_test, y_test, learning_rate=1, num_iteration=100)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train.T,y_train.T)
print("test accuracy {}".format(lr.score(x_test.T,y_test.T)))











