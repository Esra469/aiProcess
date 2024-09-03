
"""
Numpy
"""
#Numpy
#importing
import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9]) #1*9 luk bir vektör
print(array.shape) #boyutunu belirtir

a=array.reshape(3,5) #matris oluşturur yeniden boyutlandırır
print("shape: ",a.shape)
print("dimension: ",a.ndim)
print("data type: ",a.dtype.name)
print("size: ",a.size)

print("type: ",type(a))

array1=np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]])

zeros=np.zeros((3,4))

zeros[0,0]=5
print(zeros)

np.ones((3,4))
np.empty((2,3))

a=np.arange(10,50,5) #10 dan başlayarak 50 ye kadar 5 er 5 er say
print(a)
a=np.linspace(10, 50,20) #10 dan başlayarak 50 ye kadar 20 sayı yaz
print(a)
print("---------------------------------------------------------------------------")
#%% numpy basic operations

a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a)) #her değer için sin değeri alir

print(a<2) #a değerleirnş gezip 2 den küçk olma durmunu true false sayar

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])

# element wise prodcut
print(a*b)

#matrix prodcut
a.dot(b.T) #çarpım yapmak  için b nin transpozunu azlıyoruz (matris çarpımında kural boyutarın aynı olması)

print(np.exp(a))

a=np.random.random((5,5))

print(a.sum())#random matristeki random değerleri toplar
print(a.max())#max değeri bulur
print(a.min())

print(a.sum(axis=0))#satır değerdeki verileri toplar
print(a.sum(axis=1))#sütün değerdeki verileri toplar

print(np.sqrt(a))#a nın karekökü
print(np.square(a))#a nın karesini alır

print("---------------------------------------------------------------------------")
#%% indexing and slicing

array=np.arrray([1,2,3,4,5,6,7]) #vektor dimension =1
print(array[0])
print(array[0:4])

reverse_array=array[::-1]
print(reverse_array)

array1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])
print(array1[:,1])

print(array1[1,1:4])

print(array1[-1,:])
print(array1[:,-1])
print("---------------------------------------------------------------------------")
#%% shape manipulation
array=np.array([[1,2,3],[4,5,6],[7,8,9]])

#flatten
a=array.ravel() #matrisi düzletşritiyor

array2=a.reshape(3,3) #yeniden boyutlandırır ama kalıcı olması için atama lazım onun için array.resize daha uygun
arrayT=array2.T #transpoz alır

print(arrayT.shape)

print("---------------------------------------------------------------------------")
#%% stacking array
array1=np.array([[1,2],[3,4]])
array2=np.array([[-1,-2],[-3,-4]])

#array([[1,2],[3,4]])
#veritical
# array([[1,2],
#       [3,4]])
# array([[-1,-2],
#        [-3,-4]])
array3=np.vstack((array1,array2)) # dikey birleştirilmş arraylar


#horizontal
# array([[1,2],[-1,-2],
#        [3,4],[-3,-4]])

array4=np.hstack(array1,array2) #birleştirilmiş arraylar

print("---------------------------------------------------------------------------")
#%% convert and copy array

liste=[1,2,3,4]
array=np.array(liste) #listede arraye geçmiş olduk

liste2=list(array)#arraydan liste geçme
print("---------------------------------------------------------------------------")
#%%

