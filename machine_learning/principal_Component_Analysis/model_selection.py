# -*- coding: utf-8 -*-
"""
Model selection
 Parametreler:
     1)öğrenilen parametreler
     2)seçilen parametreler (hyperparameter)
         örn:KNN algoritması K değeri
      
     K FOLD CROSS VALIDATION :avoid overfitting  (train datasını ezberlemesini önlemek için yapıyoruz)
     Data train ve test diye ayrılır ama her zaman yaptığımız gibi trainler test ile bakılmaz önce tranler kendi arasında ayrılan validationlara göre 
     aynı işlem yapılır ve bunlardan accuracy1 accuracy2.. gibi değerler bunup daha sonra bunların ortalaması bulunuyor sonrasında test ile kontrol ediliyor
"""

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

#%% 
iris=load_iris()
x=iris.data
y=iris.target

#%%Normalization
x=(x-np.min(x))/(np.max(x)-np.min(x))

#%% train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

#%% KNN için model
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3) #k neighbors ,rastgele seçilebilr ya da grid şekilde bölünüp bulunabilir

#%% K fold CV k=10
from sklearn.model_selection import cross_val_score
accuracies=cross_val_score(estimator=knn, X=x_train,y=y_train,cv=10) #estimator=knn demek cross validation yaparken knn kullan demek oluyor

#Sonuç olarak train i 3 e böldü onları da kendi içinde 10 a böldü daha sonra 9 tanesini train 1 tanesini de validation olarak ayarlayıp accuracy değeri buldu
print("average accuracy: ",np.mean(accuracies))
print("average std: ",np.std(accuracies))

#%% 
knn.fit(x_train,y_train)
print("test accuracy: ",knn.score(x_test,y_test))

#%% grid search cross validation
from sklearn.model_selection import GridSearchCV

grid={"n_neighbors":np.arange(1,50 )}#n_neighbors 1 den 50 ye kadar değerler alacak
knn=KNeighborsClassifier()  
knn_cv=GridSearchCV(knn,grid,cv=10) #GridSearchCV ,hangi algortmayı kullanabileceğimz grid ve crossvalidation 10 olacak şeklde ayarladık
knn_cv.fit(x,y)

#%% print hyperparameter KNN algorithm K değeri

print("tuned hyperparameter K:",knn_cv.best_params_)#en iyi parametreyi seçiyoruz
print("tuned parametreye göre en iyi accuracy(best score) :",knn_cv.best_score_)#seçilen parametreye göre çıkan accuracyi belirliyorz

#%% Grid search CV with logistic regression

x=x[:100:]
y=y[:100]
from sklearn.linear_model import LogisticRegression
grid={"C":np.logspace(-3,3,7),"penalty":["l1","l2"]} #l1=lasso ve l2=ridge

logreg=LogisticRegression()
logreg_cv=GridSearchCV(logreg, grid,cv=10)
logreg_cv.fit(x,y)

print("tuned hyperparameters: (best parameters):",logreg_cv.best_params_)#hangi parametre daha iyi
print("accuracy: ",logreg_cv.best_score_)#Bu parametre ile alınan doğruluk değeri

#%% Model selection Homework
logreg2=LogisticRegression(C=1,penalty='l2')
logreg2.fit(x_train,y_train)
print("score: ",logreg2.score(x_test, y_test))














