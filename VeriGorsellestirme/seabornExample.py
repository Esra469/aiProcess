# -*- coding: utf-8 -*-
"""

"""

#seaborn example gallery bak 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

#içşnder yer alan dosyalrı manuel degerlendirmek gibi encoding='ISO-8859-1' eklendi
percentagle_people=pd.read_csv("PercentagePeopleBelowPovertyLevel.csv", encoding='ISO-8859-1')

percentagle_people.head()
percentagle_people.poverty_rate.replace(['-'],0.0,inplace=True)
percentagle_people.poverty_rate=percentagle_people.poverty_rate.astype(float)#poverty_rate object kalmasındansa float ayarladık

percentagle_people['Geographic Area'].unique()#bana benzersiz olan eyaletleri getir

#use barplot    
area_list=list(percentagle_people['Geographic Area'].unique())
area_poverty_ratio=[]
for i in area_list:
    x=percentagle_people[percentagle_people['Geographic Area']==i]
    area_poverty_rate=sum(x.poverty_rate)/len(x)#önceklikle eyaletlerin ortalaması alındı
    area_poverty_ratio.append(area_poverty_rate)#oluşturduğumuz diziye eklendi
data=pd.DataFrame({'area_list':area_list,'area_poverty_ratio':area_poverty_ratio})
new_index=(data['area_poverty_ratio'].sort_values(ascending=False)).index.values#dizideki degerler alınıd sort edildi ->ascending=False->azalan degere gore
sorted_data=data.reindex(new_index )#aldığımı yeni index haline getirdi

#visualization
plt.figure(figsize=(10,10))#yeni bir figür aç
sns.barplot(x=sorted_data['area_list'],y=sorted_data['area_poverty_ratio'])
plt.xticks(rotation=90)#yazılan isimlerin duruş açısı
plt.xlabel('States')
plt.ylabel('Poverty Rate')
plt.title("poverty rate given states")


#%% most common 15 name or surname of killed people
kill=pd.read_csv("PoliceKillingsUS.csv",encoding='ISO-8859-1')
seperate=kill.name[kill.name !='TK TK'].str.split()#adı tk tk olmayanları ayrı "Esra" "Çimen" gibi
a,b=zip(*seperate)#bunlar ziple ["Esra" "Çimen"] diye
name_list=a+b#burada da tuple içinde birleştirldi
name_count= Counter(name_list)#namelerin kaç tane oldugunu count ediyor
most_common_names=name_count.most_common(15)#en çok olanı hesapla
x,y=zip(*most_common_names)
x,y=list(x),list(y)

#visualization
plt.figure(figsize=(10,10))
sns.barplot(x=x,y=y,palette=sns.cubehelix_palette(len(x)))#len(x)->o uzunlk sayısı kadar farklı renk ama biirbiri ile uyumlu
plt.xlabel("Name or surname of killed people")
plt.ylabel("Frequency")
plt.title("Most common 15 name or surname of killed people")

#plot2
#high school graduate rate of the population that is older than 25 in states
percent_over_25_completed_highschool=pd.read_csv("PercentOver25CompletedHighSchool.csv",encoding='ISO-8859-1')
percent_over_25_completed_highschool.percent_completed_hs.replace(['-'],0.0,inplace=True)
percent_over_25_completed_highschool.percent_completed_hs=percent_over_25_completed_highschool.percent_completed_hs.astype(float)
area_list=list(percent_over_25_completed_highschool['Geographic Area'].unique())
area_highschool=[]
for i in area_list:
    x=percent_over_25_completed_highschool[percent_over_25_completed_highschool['Geographic Area']==i]
    area_highschool_rate=sum(x.percent_completed_hs)/len(x)
    area_highschool.append(area_highschool_rate)

#sorted
data=pd.DataFrame({'area_list':area_list,'area_hightschool_ratio':area_highschool})
new_index=(data['area_highschool_ratio'].sort_values(ascending=True)).index.values#artan sıralamaya gore yaptık
sorted_data2=data.reindex(new_index)
#visualize
plt.figure(figsize=(10,10))
ax=sns.barplot(x=sorted_data2['area_list'],y=sorted_data2['area_highschool_ratio'])
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel("high school graduate rate")
plt.title("percentagle of given state's")

#yatay barplot
#percentagle of state's population according to races that are black,white,native american,asian and hispanic
share_race_city=pd.read_csv("ShareRaceByCity.csv")
share_race_city.replace(['-'],0.0,inplace=True)#- degerini 0.0 ile yerini değştir
share_race_city.replace(['X'],0.0,inplace=True)
share_race_city.loc[:,["share_white","share_black","share_native_american","share_asian","share_hispanic"]]=share_race_city.loc[:,["share_white","share_black","share_native_american","share_asian","share_hispanic"]].astype(float)
area_list=list(share_race_city['Geographic area'].unique())
share_white=[]
share_black=[]
share_native_american=[]
share_asian=[]
share_hispanic=[]
for i in area_list:
    x=share_race_city[share_race_city['Geographic area']==i]
    share_white.append(sum(x.share_white)/len(x))
    share_black.append(sum(x.share_black)/len(x))
    share_native_american.append(sum(x.share_native_american)/len(x))
    share_asian.append(sum(x.share_asian)/len(x))
    share_hispanic.append(sum(x.share_hispanic)/len(x))
#visualization
f,ax=plt.subplots(figsize=(10,10))
sns.barplot(x=share_white,y=area_list,color="green",alpha=0.5,label="White")#label grafikteki etiketler olacak
sns.barplot(x=share_black,y=area_list,color="blue",alpha=0.7,label="African American")
sns.barplot(x=share_native_american ,y=area_list,color="pruple",alpha=0.6,label="Native american")
sns.barplot(x=share_asian ,y=area_list,color="pink",alpha=0.5,label="Asian")
sns.barplot(x=share_hispanic ,y=area_list,color="yellow",alpha=0.8,label="Hispanic")

ax.legend(loc='lower right',frameon=True)#legendlerin gorunurlugu // labelrin gorundugu yer lower right ->alt ve sağ köşeye al #frameon=False olsaydı o da saydam olacaktı
ax.set(xlabel='Percentangle of Races',ylabel="Sates",title="Percentangle of state's population According to races")




















