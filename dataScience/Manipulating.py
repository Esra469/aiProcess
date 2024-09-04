# -*- coding: utf-8 -*-
"""
Manipulating data frame 

"""
#indexing data
import pandas as pd
data=pd.read_csv("pokemon.csv")
data=data.set_index('#')
data.head()#yeni bir index atayıp 1 den başlattık gibi
data["HP"][1]#hp nin 1. elemanını alır
#using log accessor
data.log[1,["HP"]]

print(type(data["HP"]))#-> tek [] series
print(type(data[["HP"]]))#->data frame

data.loc[10:1:-1,"HP":"Defense"]#hp den defense kadar al 10 tane deger->reverse yapar
data.loc[1:10,"Speed":]#10 tane deger alır speeden sonuna kadar

#transforming data
def div(n):
    return n/2
data.HP.apply(div)#pokemonların yaşını alıp 2 ye böler
data.HP.apply(lambda n:n/2)

#index object and labeled
print(data.index.name)
data.index.name="index_name"#-> bu şekilde name ye atama yapıyoruz
data.head()

data.index=range(100,900,1)

#columns için
data=data.set_index(["Type 1","Type 2"])
data.head(10)
#önceden feature olan Type 1 ve Type 2 değerleri index oldu artık

#pivoting data frame
dic={"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":["10,45,26,12"],"age":[14,25,56,45]}
df=pd.DataFrame(dic)
df

#index adını treatment yaptık  yukarıdak itablonun daha minimalist ve toplanmış hali gibi
df.pivot(index="treatment",columns="gender",value="response")
#stacking and unstacking
#1. auter 2.inner
df1=data.set_index(["treatment","gender"])
df1
#kaggleden ders devamına bak














