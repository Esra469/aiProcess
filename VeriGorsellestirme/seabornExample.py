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


#Normalizasyon
#higth school graduation rate vs Poverty rate of each state 
#2 datayı da 0 ve 1  ararsına çektik
sorted_data['area_poverty_ratio']=sorted_data['area_poverty_ratio']/max(sorted_data['area_poverty_ratio'])
sorted_data2['area_highschool_ratio']=sorted_data2['area_highschool_ratio']/max(sorted_data2['area_highschool_ratio'])
data=pd.concat([sorted_data,sorted_data2['area_highschool_ratio']],axis=1)
data.sort_values('area_poverty_ratio',inplace=True)

#visualize
f,ax1=plt.subplot(figsize=(10,10))
sns.pointplot(x='area_list',y='area_pover_ratio',data=data,color='lime',alpha=0.8)
sns.pointplot(x='area_list',y='area_highschool_ratio',data=data,color='red',alpha=0.8)
plt.text(40,0.6,'high school graduate ratio ',color='red',fontsize=17,style='italic')
plt.text(40,0.55,'poverty ratio',color='lime',fontsize=18,style='italic')
plt.xlabel('States',fontsize=15,color='blue')
plt.ylabel('Values',fontsize=15,color='blue')
plt.title('hight school graduate vs poverty rate',fountsize=20,color='blue')
plt.grid()

#joint plot
#pearsonr->2 tane koşul arasındaki korelasyonu gösterir 1 ise pozitif correlation -1 ise negatif correlation 0 ise correlation yok 
#visualization of high school garduation rate vs poverty rate of each state with different style of seaborn code
g=sns.jointplot(data.area_poverty_ratio,data.area_highschool_ratio,kind="kde",size=7)
plt.savefig('graph.png')#resimn kaggle de görünmesi için yazılabilr
plt.show()

g=sns.jointplot("area_poverty_ratio","area_highchool_ratio",data=data,size=5,color='r')#data=data demek yukarıdaki ile aynı işlevi sağlayacak demek aslında

#Race rates according in kill data(öldürülenlerin ırklara gore dagılımı)
kill.race.head(10) #
kill.race.value_counts()#hangi ırktan kaç tane olduğunu verir
kill.race.dropna(inplace=True)#ırk datasında boş deger varsa drop et yani datadan çıkar(ve bunu dataya kaydet)
labels=kill.race.value_counts().index
color=["grey","green","blue","pink","yellow","black"]#6 ırk çeşidi oldugu için 6 renk var
explode=[0,0,0,0,0,0]
sizes=kill.race.value_counts().values #ırkların degerlerinni aldı sizesere atadı#bu değerleirn hepsini bir diziye atadı->array([1201,  618,  423,   39,   31,   28], dtype=int64)
#visual
plt.figure(figsize=(7,7))
plt.pie(sizes,explode=explode,labels=labels,colors=color,autopct='%1.1f%%')#autopct ondaık yazdıktan sonradki virgülden sonraki deger
plt.title("killed people according to races ",color="blue",fontsize=15)

#Visualization of high school graduation rate vs poverty rate of each state with differenet style of seaborn code
#show the result of a linear regression within each dataset(lmplot a ait bir durum)
#LM plot
sns.lmplot(x="area_list",y="area_hightschool_ratio",data=data)
plt.show()

#Visualization of high school graduation rate vs poverty rate of each state with differenet style of seaborn code
#kde Plot
sns.kdeplot(data.area_poverty_ratio,data.area_highchool_ratio,shade=True,cut=5)#shade oluşan yuvarlakların dolulugu cut->oluşan gorselin buyuklugu
plt.show()

#Violin Plot
#show each dsitribution with both violins and points
#use cubehelix to get  a custom sequential palette
pal=sns.cubehelix_palette(2,rot=-.5,dark=.3)
sns.violinplot(data=data,palette=pal,inner="points")#gorsel ustundeki noktalar inner da gosterilir
plt.show()#buradaki gorselde şişman olan kısmın daha çok istenen veri odaklı oldugu anlasılır


#Visualization of high school graduation rate vs poverty rate of each state with differenet style of seaborn code
#heatmap
#correlation map
#corr corelation negatif olursa ters ilişki corelation pozitif olursa doğru bir ilişki durumu olur
f,ax=plt.subplot(figsize=(10,10))
sns.heatmap(data.corr(), annot=True,linewidths=.5,fmt='1.f',ax=ax)
plt.show()


#Box Plot
#manner of dead(olum sekli) 
#gender
#age
#plot the orbital period with horizonal boxes
sns.boxplot(x="gender",y="age",hue="manner_of_death",data=kill,palette="PRGn")#hue=manner_of_death içindeki classları ayrı uniqleri almak gibi
plt.title("manner of dead",color="blue")
plt.show()


#swarm plot(fazla datada sorun cıkarabilir)
#manner of dead(olum sekli)
#gender
#age
sns.swarmplot(x="gender",y="age",hue="manner_of_death",data=kill)
plt.show()

#pair plot
sns.pairplot(data)#histogram ve line şekilnde bir plot çizdiriyor
plt.show()

#Count plot
#manner of death
kill.manner_of_death.value_counts()#manner of death içinde hangi çeşitten kaç tane var bilgisi
sns.countplot(kill.gender)#kill içindeki genderleridne hangiisnden kaç tane oldugunu analizler
sns.countplot(kill.manner_of_death)
plt.title("gender",color="blue",fontsize=10)

#age of killed people
above25=["above25" if i>25 else 'below25' for i in killed]
df=pd.DataFrame({'age':above25})
sns.countplot(x=df.age)
plt.ylabel('number of killed people')
plt.title("age of killed people",color="blue",fontsize=15)























