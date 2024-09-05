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


