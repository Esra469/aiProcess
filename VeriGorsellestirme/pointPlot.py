# -*- coding: utf-8 -*-
"""
keep going
"""
#point plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

import warnings
warnings.filterwarnings('ignore')

percentagle_people=pd.read_csv("PercentagePeopleBelowPovertyLevel.csv", encoding='ISO-8859-1')

percent_over_25_completed_highschool=pd.read_csv("PercentOver25CompletedHighSchool.csv",encoding='ISO-8859-1')

#peope
area_list=list(percentagle_people['Geographic Area'].unique())
area_poverty_ratio=[]
for i in area_list:
    x=percentagle_people[percentagle_people['Geographic Area']==i]
    area_poverty_rate=sum(x.poverty_rate)/len(x)#önceklikle eyaletlerin ortalaması alındı
    area_poverty_ratio.append(area_poverty_rate)#oluşturduğumuz diziye eklendi
data=pd.DataFrame({'area_list':area_list,'area_poverty_ratio':area_poverty_ratio})
new_index=(data['area_poverty_ratio'].sort_values(ascending=False)).index.values#dizideki degerler alınıd sort edildi ->ascending=False->azalan degere gore
sorted_data=data.reindex(new_index )

#graduate
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















