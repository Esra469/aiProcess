
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



