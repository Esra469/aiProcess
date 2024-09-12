# -*- coding: utf-8 -*-
"""
Linear regesyon
@author: ASUS
"""
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("linear_regresion_dataset.csv")
df=pd.DataFrame(data,columns=['deneyim','maas'])
plt.scatter(df.deneyim,df.maas)
plt.show()
