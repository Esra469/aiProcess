# -*- coding: utf-8 -*-
"""
#Kaggle Titanic Project
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings("ignore")#bazı hataalr geliyor ama problem yok onları enale ediyoruz
plt.style.use("seaborn-whitegrid")#->Bu sayede istediğimiz türü seçip kullanabilrz
plt.style.available#->Mümkün olan tüm style leri gösterir

train_df=pd.read_csv("train.csv")
test_df=pd.read_csv("test.csv")
test_PassengerId=test_df["PassengerId"]
train_df.columns
train_df.describe()

#variable description <a id="1"></a><b> ->bu şekşlde bir kullanım notebook da link şeklinde yönlendirme sağlayack
#dataset içerisindeki featureleri değerlendirme feartue den işe yarardığı

#univariate variable analysis
    #categorical variable analysis
    #birden fazla kategoriden oluşan featurelerdir->survived (0,1) gender(M,F) Embarked,Ticket
    #  Numerical variable analysis
    # numerical olan ->fare age and passengered
    
#Categorical variable check
def bar_plot(variable):
    """
    input:variable ex:"Sex"
    output:bar plot & value count
    """
    #get feature
    var=train_df[variable]
    #count number of categorical variable(value/sample)
    varValue=var.value_counts()#istenen sutunda kaç tane kategori var
    #visualize
    plt.figure(figsize=(9,3))
    plt.bar(varValue.index, varValue)#x,y kordinatı olarak ayrılır gradikte x istenen kategori türü y de de her bir kategori değeriden kaç tane olduğu 
    plt.xticks(varValue.index, varValue.index.values)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()
    print("{}:\n {}".format(variable,varValue))

category1=["Survived","Sex","Pclass","Embarked","SibSp","Parch"]#birden fazla değeri olan featureler
for c in category1:
    bar_plot(c)

category2=["Cabin","Name","Ticket"]
for c in category2:
    print("{} \n".format(train_df[c].value_count()))
    

#Numerical variable->Histogram plot ettiriliyor
#histogram->herhangi bir toplamdaki özelliğin dağılımı
def plot_hist(variable):
    plt.figure(figsize=(9,3))
    plt.hist(train_df[variable],bins=800)#Pbu olmazsa ayrı ayrı şeritler halinde gözükmez(bins)
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{} distribution with hist".format(variable))
    plt.show()

numericVar=["Fare","Age","PassengerId"]
for n in numericVar:
    plot_hist(n)
    
    
    
#Basic data analysis ->linke bağlamak için -> <a id="2"></a><b>
#Bazı featruelerin hangiinin hayata kalma ile ilgisi var(ilişki var mı)
#pclass-Survived
#Sex-Survived
#SibSp-Survived
#Parch-Survived

#pclass-Survived
train_df[["Pclass","Survived"]].groupby(["Pclass"],as_index=False).mean()#grupby da gruplandırdıktan sonra neye göre gruplanacağı da belirtlmeli(mean)
#belli bir duruma göre sıralatalım
train_df[["Pclass","Survived"]].groupby(["Pclass"],as_index=False).mean().sort_values(by="Survived",ascending=False)#ascending =false ->azalan bir durumda

#Sex-Survived
train_df[["Sex","Survived"]].groupby(["Sex"],as_index=False).mean().sort_values(by="Survived",ascending=False) 


#outlier detection (maaş -işci ilişkisi (elimizdeki verileir bozan şey outlier))
#1st quertian(Q1)/3rd quertian(Q3)=2nd quertian=median=Q2  IQR=Q3-Q1  IQR.1.5=outlier
#Q1-(IQR.1.5)=bir deger   Q3+(IQR.1.5)=bir deger ->bu degerleri diziye koy dışarıda kalan degerler outlier olur ->bu durum bir istatistik olay olduğunda çıkarılmsı gereken değer o degerdir demek

def detection_outliers(df,features):
    outlier_indices=[]
    for c in features:
        #1st quartile
        Q1=np.percentile(df[c],25)
        #3rd quartile
        Q3=np.percentile(df[c],75)
        #IQR
        IQR=Q3-Q1
        #Outlier step
        outlier_step=IQR*1.5
        #detect outlier and their indeces
        outlier_list_col=df[(df[c]<Q1-outlier_step) | (df[c]>Q3-outlier_step)].index
        #store indeces
        outlier_indices.extend(outlier_list_col)
    outlier_indices=Counter(outlier_indices)#kaç tane outlier olduğunu hesaplar
    multiple_outliers=list(i for i,v in outlier_indices.items() if v>2)
    
    return multiple_outliers

train_df.loc[detection_outliers(train_df,["Age","SibSp","Parch","Fare"])]

#drop outlier
train_df = train_df.drop(detection_outliers(train_df,["Age","SibSp","Parch","Fare"]),axis = 0).reset_index(drop = True)


#missing value (boş degerlerden kurtulma)
    #Find missing value
    #Fill missing value
train_df_len=len(train_df)
train_df=pd.concat([train_df,test_df],axis=0).reset_index(drop=True)#temizleme için test ve train birleştirldi


train_df.columns[train_df.isnull().any()]#train dataFrame içerisinde missing value var mı diye baktık
train_df.isnull().sum()#->boş olan frameleri al ve topla

#fill missing value(value ler doldurulacak)
#embarked has 2 missing value
#Fare has only 1
train_df[train_df["Embarked"].isnull()]#bir şeyler ile karşılaştırıp embarked doldurulacak
train_df.boxplot(column="Fare",by="Embarked")
plt.show()

train_df["Embarked"]=train_df["Embarked"].fillna("C")
train_df[train_df["Embarked"].isnull()]#->Yukarıdakini doldurduktan sonra artık boş değer gelmeyecek

#Fare
train_df[train_df["Fare"].isnull()]
train_df["Fare"]= train_df["Fare"].fillna(np.mean(train_df[train_df["Pclass"]==3]["Fare"]))
#Boş deger kalmadı






        

    
    
    
    
    
    
    
    
    
    


