# FIREWALL-USING-IMAGE-PROCESSING-FACE-RECOGNITION-AND-LIVENESS-FACTOR-ALGORITHMS
Goruntu ısleme , yuz tanıma ve canlılık faktoru algorıtmaları kullanarak guvenlık duvarı yazılım projesıdır.  

Görüntü işleme ve Yüz tanıma algoritmaları kullanarak güvenlik sistemi tasarımında günümüzde 
telefon, tablet, güvenlik kameraları mantığı kullanılarak ve güncellenerek oluşturulan bir projedir. 
Bu proje tanımlanan -izin verilen- kişilerin girişine izin verilecek şekilde yapılacaktır. Proje 
sonucunda oldukça avantajlı bir giriş sistemine sahip olunacaktır. Hiçbir şekilde birine ihtiyaç 
olmadan, anahtar vb. şeyler olmadan giriş sağlanarak olası şanssızlıklar giderilecektir. Bununla 
beraber sadece şanssızlık değil güvenlik açısından da herhangi bir hata veya tehdit ortadan 
kaldırılmak istenmiştir. Proje geliştirilerek toplu yaşam alanlarında aranan kişileri de tespit 
edebilecek alt yapıya sahiptir. 

It is a project created by using and updating the logic of phone, tablet, security cameras in the 
design of security system using image processing and face recognition algorithms. This project 
will be done in a way that the defined -allowed- persons will be allowed to enter. As a result of 
the project, it will be possible to have a very advantageous nir entry system. Possible misfortunes 
will be eliminated by providing access without the need for anyone, keys etc. However, not only 
bad luck, but also in terms of security, any mistake or threat was wanted to be eliminated. 

Numpy = np 
Opencv = cv2 
Face-Recognition = fc 

Günümüz teknolojisinde elektronik aletlerde ve cihazlarda örneğin telefon, tablet, bilgisayarve bu 
tarz teknolojik cihazlarda sıkça kullanılmakta olan yüz tanıma sistemleri mevcut olup bu sistemler 
şifreleme amaçlı kullanılmaktadır. Örneğin telefonumuzu açabilmek için yüzünü tanıttığımız 
kişilerin erişimi olabilmektedir. Bunlarla beraber herhangi bir dosyamızı açabilmek için yüz 
tanıma sistemi ile şifreleme yapabilmekteyiz. Bu uygulama ve şifreleme sistemi güvenliğimiz ve 
gizliliğimiz için oldukça önemlidir. Yüz tanıma sisteminden kısaca bahsedecek olursak görüntü 
işleme algoritmaları kullanarak yapılan bir güvenlik sistemidir. Özellikle benim projemde 
kullanacağım ve genel olarak da tercih edilen bir yazılım dili olan Python kullanılmaktadır. 
Python'da görüntü işleme kütüphaneleri kullanılarak program yazılmaktadır. Peki bu görüntü 
işleme ne demektir? 
Görüntü işleme fotoğraf veya fotoğraflardan, video ve video kesitlerinden alınan datanın 
kullanılıp tanımlanmak istenen nesne veya kişinin doğruluğunu tespit eden yazılımdır. Görüntü 
işleme yazılımını projemde yüz tanıma işlemi için kullandım. Genel anlamda kısa bir giriş 
yapacak olursak, önceden tanıtılmış kişi yüzünü data olarak belirleyip daha sonrasında kamerada 
görünen kişi ile uyumunu ölçerek yüz tanıma işlemini gerçekleştiren programı yazdım. Bu 
programda görüntü işleme ve yüz tanıma algoritmaları mevcuttur. Yazılım ve programlama 
işlemini gerçekleştirdikten sonra bu programı somutlaştırarak evlerde veya kalabalık alanlarda 
bulunan girişlere uygulanıp otomatik olarak giriş sağlamak planlanmıştır. Bu sayede örneğin 8 
aranan kişi veya suçlular otomatik olarak tespit edilecektir. Bu işlem sonrasında hayatımız daha 
güvenli ve daha sistematik bir hal alacaktır. 

Güvenlik duvarı nasıl kurulacak?  

Kurulacak olan güvenlik sistemi için öncelikle en uygun yazılım dili seçilmelidir. Bu yazılım dili 
ise Python olarak seçilmiştir. Python; programa dili veri bilimi, makine öğrenimi, sistem 
otomasyonu, web ve API geliştirme ve daha fazla işlem için temel yazılım dilidir. Python, dil 
bakımından oldukça sade olup yapılabilecek uygulama ve yazılacak programlar konusunda 
oldukça geniş kapsamlı bir dildir. Python; nesne yönelimli, yorumlamalı, birimsel ve etkileşim 
bakımından yüksek seviyeli bir programlama dili olup bu sayede ise çok geniş kapsamlı ve 
birbirinden farklı projelerde kullanılan bir dildir. Peki Python'da bu yüz tanıma ve güvenlik 
sistemi nasıl kurulacak? Öncelikle seçtiğimiz yazılım dilinde geniş çaplı bir araştırma yaptım. Bu 
araştırmalar sonucu Python'da kullanılacak olan kütüphaneleri, modülleri ve modelleri tespit 
ettim. Bu kütüphanelerden bahsedelim. Öncelikle görüntü işleme programının vazgeçilmez ve en 
temel parçası olan OpenCv geliyor. OpenCv kütüphanesi; (Open Source Computer Vision), açık 
kaynak kodlu görüntü işleme kütüphanesidir. 1999 yılında İntel tarafından geliştirilmiştir. 
OpenCv kütüphanesi içerisinde görüntü işleme ve makine öğrenmesine yönelik 2500'den fazla 
algoritma mevcuttur. Bu algoritmalar sayesinde yüz tanıma, nesneler ayırt ederek seçme, canlı 
hareketlerini tespit edebilme, nesne sınıflandırma, plaka tanımlama, optik karakter tanımlama gibi 
işlemler rahatlıkla gerçekleştirilebilir. 

OpenCVy’nin kütüphanesinin yanında kullanılan kütüphanelerin başında Face_Recognition 
kütüphanesi gelmektedir. Peki bu kütüphane ne işe yarar ve nasıl çalışır? Python'dan veya komut 
satırından yüzleri tanıma ve değiştirme ile Dünyanın en basit yüz tanıma kütüphanesidir. Dlib'in 
son teknoloji ürünü yüzü kullanılarak üretilmiş olup tanıma Derin öğrenme ile oluşturulmuştur. 
Model, üzerinde% 99.38'lik bir doğruluğa sahiptir. Hata payı anlaşılacağı üzere çok azdır. Bu da 
güvenlik duvarı için vazgeçilmez bir etkendir. Dlib ve CMake kütüphaneleri ise face_recognition 
kütüphanesinin kullanılması ve kurulması açısından temel oluşturacak kütüphane ve eklentilerdir. 
Bu kütüphaneler C++ tabanlıdır. Face-Recognition kütüphanesinin temel anlamda çalışma 
mantığı Görsel-1’de verilmiştir. İlk olarak, görüntüde kullanıcının yüzünü bulma işlemi ve bir 
sınırlayıcı kutuyla sınırlandırma işlemi gerçekleştirilecektir. Sonrasında, tanıma görevi için 
kullanılabilecek yüzün özellikleri ayıklama işlemi sağlanacaktır. Bu işleme eğitme işlemi de 
denebilir. Son olarak da saklanan yüzlerin görsel özelliklerini temsil eden bir vektör veri tabanı 
ile bir yüz eşleştirme yapılacaktır. Data olarak alınan fotoğraflar çok boyutlu dizi ve matris olarak 
irdelenecektir. Bu işlem ise Python yazılım dilinin vazgeçilmezi olan NumPy kütüphanesi 
yardımı ile yapılacaktır. NumPy kütüphanesinden bahsedelim. NumPy,  Python programlama dili 
için büyük diziler ve matrisleri destekleyen ve bu diziler üzerinde işlem yapacak olan üst düzey 
matematiksel işlevler ekleyen bir kütüphanedir. Diğer bir kütüphanemiz Os kütüphanesidir. Bu 
kütüphane Python programlama dili ile hazır bir şekilde gelen, dosya ve dizinlerde kolay bir 
şekilde işlemler yapabilmemizi sağlayan bir kütüphanedir. Kütüphanelerimizin tanıtılma işlemini 
gerçekleştirdik. Şimdi ise yazacağımız programın kısaca ve gene lolarak mantığından ve 
algoritmasından bahsedelim. Daha sonra da programımıza geçelim. Öncelikle tanımlama ve tespit 
işleminden önce neye göre tanımlama işlemi yapacağını belirlememiz gerekiyor. Bu işlem de 
programımıza önceden yüklenecek veya program dahilinde alınacak datalardan oluşmaktadır. Bu 
datalar bahsedildiği gibi program harici dosyaya yüklenecek fotoğraf veya fotoğraflar ile 
sağlanabilir. Aynı zamanda ise program dahilinde çekilecek olan fotoğraflar ile sağlanabilir. Bu 
dataları çeşitli yöntemler ile aldıktan sonra dataları tanımlama ve işleme üzerinde çalışma 
işlemleri için hazır hale getirilecektir. Bu data işlemi bilgisayarın çalışma mantığına uygun şekle 
getirmek için yapılacaktır. İlk adım olarak datalarımızı çeşitli yöntemler ile elde ettik. Ardından 
da bu dataları üzerinde işlem yapılır hale getirdik. Bu işlemler örnek yazılım ve kodlar ile detaylı 
bir şekilde anlatılacaktır. Son adım olarak da harici veya dahili kamera yardımıyla video kamera 
açılarak tanımlama işlemi gerçekleştirilecektir. Bu işlem esnasında öncelikle yapılan işlem açılan 
kamerada yüz var mı onu incelemektir. Yüz olmazsa eğer herhangi bir karşılaştırma ve datalardan 
yararlanarak tanımlama işlemi yapılamayacağı için program yalnızca kamera görevi 
üstlenecektir. Eğer ki açılan video kamerada yüz var ise datalarla işlem yapma kısmına geçecektir. 
Bu işlem de yukarda bahsedildiği üzere kütüphaneler ve harici yazılım dosyası ile sağlanacaktır. 
Bu dosya hazır bir kütüphane gibi programa eklenmelidir. Dosya sayesinde kamera ekranında 
yüzü tespit edebilmekteyiz. Bu dosya, "haarcascade_frontalface_default" dosyası olup hazır 
olarak elde edilebilir bir dosyadır. Bu dosya yardımı ile video kamera ekranında yüz var ise 
tanımlama işlemine geçilecek şekilde algoritma yazılacaktır. Ekranda yüzün varlığını tespit 
ettiğimiz takdirde tanımlama aşamasına geçebilmekteyiz. Yüz tanıma -yüz tanımlama işlemi- 
yukarıda açıklandığı gibi öncelikle açılan harici veya dahili kamerada yüz olup olmadığını tespit 
ederek başlıyordu. Ardından kamerada görünen alanda yüz var ise artık önceden elde edilmiş 
veya yüklenmiş data veya veri tabanı ile eşleştirme, benzetme ve karşılaştırma işlemi olarak 
adlandırılabilir. Bu işlem de datada ve veri tabanında bulunan fotoğrafları matris ve dizi olarak 
dönüştürme işlemini yapmıştık. Bu işlem fotoğrafları sayısal veya matematiksel olarak belirtme 
işlemi olarak da tanımlanabilir. Bu işlem sonucunda verilerimiz işlenmeye hazır hale gelmiştir. 
Bu verileri kullanarak gerçek zamanlı açılan kamerada bulunan yüzleri karşılaştırma işlemi 
sağlanabilmektedir. Bu karşılaştırma işlemi nasıl gerçekleşiyor? Datalarımızı matris haline 
getirmiştik, bu işlem ile fotoğrafların kesitlerinde bulunan matematiksel ifadeler kullanılır. 
Dataların matrisleri ile kamerada açılan fotoğrafın matris şeklini kesit kesit inceleyerek, benzetme 
ve karşılaştırma işlemleri sonucunda benzerlik veya farklılık fonksiyonları doğrultusunda 
kamerada açılan yüzü tanımlama işlemini gerçekleştiriyor. Detaylı anlatım kodlar ile beraber 
bahsedilecektir. Temel anlamda programın aşamalarından ve genel mantığından bahsettiğimize göre program 
detaylarına, programlama işlemlerine ve test aşamalrına geçebiliriz. 

Program ve Test Aşamaları: 

Geçen dönem gerçekleştirdiğim projenin devamı olarak bu dönem aynı projem üzerinden 
geliştirme işlemi ve bu işlem sonucunda da projemi somutlaştıracağım. Öncelikle geçen dönem 
yaptığımız gelişmeleri hatırlayalım ve özetleyelim. Projemizin son hali şu şekildeydi: 
Geliştirdiğim algoritma ve yüz tanıma programında datası verilen kişilerin yani tanıtılan kişilerin 
tanınması gerçekleştirilmek isteniyordu. Ancak yazdığım algoritmada hata payı, hassasiyet 
problemi ve canlılık faktörü sorunu bulunmaktaydı. Bunlardan bahsedelim. Yazdığımız algoritma 
öncelikle kişilerin fotoğrafını çekerek data -veri- elde edip bunları da matris formu haline 
getirerek cihazımızın fotoğraflar üzerinde işlem yapılabilmesini sağlamaktaydı. Bunu da sayısal 
formda yapıyordu. Yazılan algoritmada 3 aşama bulunmaktaydı. Bu aşamalar; Kişinin fotoğrafını 
çekmekle başlıyordu. Bu sayede yazılımımız kendi verisini oluşturacak yüzler elde ediyordu. 
Ardından ise bu fotoğraf ve yüzleri sayısal matrislere çevirerek algoritmamızın kullanacağı data 
elde ediyordu. Son aşama ise anlık açılan kamerada görünen yüzleri ve kişileri doğru bir şekilde 
tanımaya çalışmaktaydı. Son aşamada geliştirdiğimiz algoritmanın eksikliğini açıkça 
görebiliyorduk. Bu eksiklikler elde edilen verilerde oluşan hatalardan kaynaklanıyordu. Bunun 
sonucunda da kişileri yanlış tanıyabiliyor örneğin a kişisine b, b kişisine a diyebiliyordu. Bununla 
beraber tanıttığımız kişiye “Unknown” bilinmiyor diyebiliyor veya tanıtma işlemi yapmadığımız 
kişiyi ise datası alınan herhangi birine benzetip, adlandırıyordu. Elbette bu tarz hatalar olacaktır. 
Anca hata payının en aza indirilmesi gerekmektedir. Sonuç olarak projem bir güvenlik sisteminin 
temelini oluşturacaktı. Bu tarz hataların fazla olması istenmeyen bir durum oluşturuyordu. 
Bununla beraber en önemli hata kamerada görülen kişinin canlı -reel- kişi olup olmadığı fark 
etmeksizin tanıma işleminin gerçekleşmesiydi. Burada yapılması gereken geliştirme kameraya 
fotoğraf gösterildiği zaman kameradaki görüntünün cansız olduğunu anlayabilmesi idi. Ben de 
gereken geliştirme işlemlerine başladım. Bu geliştirme işlemlerinin temeli öncelikle hata payının 
en aza indirilmesiydi. Araştırmalarım sonucunda yazdığım programda fark ettim ki geliştirilen 
algoritmanın hatalı olduğunu fark ettim. Bu hatanın doğrultusunda ise algoritmamı geliştirmek 
veya algoritma mantığımı değiştirmek için çalışmalara başladım. Deneme aşamalarından 
bahsedelim. 

1. Deneme: Hazır algoritmanın geliştirilmesi
 
Hazırda bulunan algoritmamı tamamen değiştirmeden, gereken geliştirmeleri düzeltmek ve daha 
sağlıklı (hata payının daha az) olması için çalışmalara başladım. Bu çalışmalarda elde ettiğim 
sonuçlar çok fazla ilerleme kaydettirmedi bana. Örneğin 100 kişide denenen program önceden 50 
kişiyi doğru bir şekilde tanıyordu. Geliştirme sonucunda bu oran pek fazla artmadı %60-65'lere 
kadar anca çıkabildi. Bunun sonucunda tekrardan geliştirme işlemlerine başladım.

2.Deneme: Hazır algoritmanın geliştirilmesi 

Hazır halde bulunan algoritma üzerinde geliştirme işlemlerine devam ettim. Bu işlem bu sefer 
“conf” benzerlik oranını değiştirmek üzerine oldu. Ancak bu sefer de doğru tanıma sayısı artmak 
yerinde düştü. Örneğin bir yüzün algoritmada bulunan dataya benzeyip tanımlanması için veri ve 
yüzün benzerlik oranının 0,6 veya 0,5 olması gerekmektedir. Bu sayısal verinin mantığını 
araştırarak şu bilgileri elde ettim: Yazdığım algoritma kişileri datalar ile eşleştirip tanıması için 
ilk başta 0,6 benzerlik oranını kullanıyordu. Bunu yazdığım algoritma ile 0,5 seviyesine indirdim. 
Bu sefer de datası olmayan kişileri de alınan kişilere daha fazla eşleştirme yaptı. Ve sonuç olarak 
ise bilinmeyen kişileri herhangi bir tanımlama sonucunda yanlış tanıdı. Yani sorunun benzerlik 
oranı algoritmasının sayısal mantığında olmadığını da böylece test etmiş oldum. 

3.Deneme: Hazır algoritmanın geliştirilmesi 

Elimde olan algoritmanın sayısal mantığı yerine koşul ifadesini değiştirmek istedim. Bunun 
anlamını şu şekilde ifade edelim; Algoritmanın sayısal mantığını tekrardan 0,6 oranına çevirdim. 
Ardından ise bu mantığın kullanımını değiştirmek istedim. Yani, sayısal mantığın yanında 
algoritmadaki kullanımı da değiştirilebilmekteydi. Örneğin sayısal mantık açısından 0,6 oranını 
sağlamasının yanında algoritmadaki kod birliği sayesinde fotoğraf ve datanın benzerliğini de 
tanımlayabiliyoruz. Daha önceki algoritmada 0,6 oranı şartının yanında, yazılımda da 70 
benzerlik ifadesi yer almaktaydı. Bu oranın fazla olduğunu düşünerek %60 ve %50 oranına kadar 
düşürdüm. Ama bunun sonucunda da istediğim hassasiyeti-hata payını- elde edemedim. Bu sefer 
de datası olan kişileri yanlış tanımaya veya tanımamaya başladı. Bu 3 deneme aşamasından sonra 
da anladım ki geliştirmiş olduğum algoritmanın temelinde mantık hatası vardı. Bunun sonucunda 
da algoritmamı baştan yazıp değiştirme işlemlerine başladım. Hazır algoritmanın verdiği mantık 
hatası aşağıdaki fotoğrafta verilmiştir.Burada algoritmanın hem sağdaki (Kadir) hem de soldaki
(Ahmet) kişiyi tanımasına rağmen veri oluşturma aşamasında bulunan fotoğraf çekme işlemlerindeki
sorunlardan dolayı, kadir kişisi uzaklaştığında tanınmıyor olarak adlandırılıyor.
Bunun nedeni ise Ahmet kişisi adına, veri alma aşamasının kameraya uzak bir şekilde olması ve 
bununla birlikte sağda bulunan kişinin (kadir) kameraya yakın bir şekilde veri alma aşamasının 
gerçekleşmesi yüzündendir. Kadir kişisi ayağa kalktığı (uzaklaştığı) zaman algoritma aslında
verisi bulunan kişiyi tanımıyor. Bu da algoritmamızın hatalı olduğunu göstermektedir.
Burada ise AHMET adlı kişi yaklaşınca (oturunca) KADİR adlı kişi uzakta kalmaya devam edince
her iki kişiyi de hatalı bir şekilde tanıyor. AHMET'e KADİR, KADİR'e BİLİNMEYEN kişi diyor.
Buradaki hatalar şu sebeplerden kaynaklanıyor; Öncelikle cihazımızın (bilgisayar veya telefon) 
kamerasındaki hassasiyetten kaynaklanıyor olabilir. Bu hatayı gidermek için daha kaliteli
çekim yapan kameralar kullanılabilir. Fotoğrafın çekildiği açı hata payı için oldukça önemli olup
bu hatayı ortadan kaldırmak için ise değişik açılardan fotoğrafların çekilmesi gerekmektedir.
Fotoğrafların çekildiği mesafe(uzaklık) veriler için önemli olup açı ile aynı mantık ile
farklı mesafelerden veri almak gerekmektedir. Bunlarla beraber genel olarak ortamdaki ışık,
yoğunluk vb etkenler de etkilidir. Bunu ortadan kaldırmak için ideal mesafe, ışık, uzaklık belirlenmeli
ve bunlar göz önünde bulundurularak veri alınıp veri tabanı haline getirilmesi gerekir. 
Bu bilgiler göz önüne alınarak hata payının en aza indirgenmesi oldukça muhtemeldir.

4.Deneme: Algoritmanın değiştirilmesi 

Daha önceden yazdığım algoritmayı baştan değiştirip yazmak için çalışmalara başladım. 
Öncelikle kullandığım kütüphaneleri değiştirmek için araştırmalara başladım. Bunun değişimin 
sonunda da anladım ki; Yazdığım algoritma sonucunda oluşturduğum programın fotoğraflarını 
kendi çekmesi ve veri haline(data) çevirme işlemleri esnasında fotoğraf kalitesini bozarak hata 
payının artmasına neden olmaktaydı. Elbette programımızın kendi verisini kendi elde etmesi 
verim açısından daha iyiydi ancak bunun sonucunda hassasiyetinin bozulması projemizin asıl 
amacından uzaklaşmasına sebebiyet veriyordu. Bunun sebepleri ise cihazımızın kamera kalitesi, 
çekim aşamalarındaki hatalar, ortam şartlarının optimum olmaması gibi ortam ve cihaz 
hatalarıdır. Bu hataların yanında da algoritmamızın zaten hatalı olarak elde ettiği fotoğrafları 
matris formuna (sayısal) çevirme aşamasında da ister istemez bozulmaları hesaba katarsak 
algoritmamızın hata payının bu derece yüksek olması kaçınılmaz olmaktaydı. Bu sebebiyetten 
algoritmamdan fotoğrafları kendinin çekme aşamasını çıkardım. Daha önceden çekilen 
fotoğrafların kullanılmasının daha verimli olacağını düşündüm. Bu sayede yazılan program değil 
de manuel olarak fotoğraf çekme işlemi olacaktı. Bu sayede optimum şartların daha kolay elde 
edilmesini sağladım. Algoritmadan çıkardığım fotoğraf çekme aşamasını yeni yazdığım 
algoritmada da değiştirmem gerekiyordu. Bu yüzden algoritmaya, manuel olarak fotoğraf 
eklenme işlemini tanıttım. Bundan sonra dosya yolu belirtilen dosya içine eklediğimiz fotoğraflar 
kullanılacaktı. Ve algoritmayı geliştirmeye devam ettim. Ama bu aşamadan önce verim açısından 
deneme yaptım. Deneme sonucunda hata payının azaldığını ancak istediğim seviyeye 
gelmediğini fark ettim. 

5.Deneme: Değiştirilen algoritmanın geliştirilmesi 

Güncellemiş olduğum algoritmadaki hatalara veya eksikliklere odaklanarak başladım. Bunun 
sonucunda kullandığım kütüphanelerin de eksik kaldığını fark ettim. Kullandığım kütüphaneler 
yerine daha geniş kapsamlı ve daha hassas kütüphanelerle değiştirdim. Python yazılım dili bu 
konuda kullanıcılarına çok fazla seçenek sunarak yazacağımız algoritmada kullanılacak 
kütüphane kapasitesinin verimini de göstermiş oldu. Yeni algoritmamıza “face-recognition" 
kütüphanesini ekledim. Bu kütüphane: Face-Recognition: Python’dan ve komut satırından 
yüzleri tanıma ve değiştirme ile çok basit yüz tanıma kütüphanesidir. Bu kütüphane model 
%93,38’lik bir doğruluğa sahiptir. Bu kütüphane yüz tanıma sisteminde kullanılan en yaygın 
kütüphanedir. Bu kütüphane doğrultusunda da hassasiyet ve hata payında ciddi anlamda 
gelişmeler oldu. Facer-ecognition kütüphanesi hassasiyeti artırıp, hata payının azalmasında 
temel anlamda rol oynamış oluyor. Bu kütüphaneyi algoritmamıza import ettikten sonra 
çalıştırmaya çalışınca birden fazla hata aldığımı gördüm. Bu hataları araştırıp, gidermeye çalıştım. 
Bu hataları araştırınca da hataların face-recognition kütüphanesinin kurulum aşaması için Dlib 
ve CMake kütüphanelerinin kurulması gerektiğini gördüm. Bunun sonucunda bu kütüphaneleri 
import edip yüklemeye çalıştım. Çok geniş kapsamlı ve boyut olarak da büyük kütüphaneler 
olduğu için normal kütüphanelere göre biraz daha detaylı kuruluma sahipti. Uzun uğraşlar 
sonucunda bu kütüphaneleri kurdum ve import ettim. Ardından da face-recognition 
kütüphanesini çalıştırdım. Yukarıda giriş kısmında Dlib ve CMake kütüphanelerinden kısaca 
bahsetmiştik. Şimdi ise daha detaylı bir şekilde bahsedelim. Dlib ve CMake kütüphaneleri bir 
arada kullanılıp, C++ yazılım dilinde karmaşık yazılımlar oluşturmak için kullanılan 
kütüphanelerdir(araçlardır). Bu araçların kullanılması için ise Visual Studio programı üzerinden 
C++ dilini de yüklemek gerekiyordu. İşin detay ve zor olan kısmı buydu. Bu aşamayı da gereken 
araçları ve uygulamaları yükleyip bilgisayarın ortam değişkenlerinde bulunan path’e ekleyerek 
sonlandırdım. Ve algoritmamı geliştirmeye devam ettim. Bu algoritma türünde iki farklı yöntem 
vardı. Öncelikle ana algoritmaya ek olarak kullanılan simple-facerec algoritmasının da kullanıldığı 
programı yazdım. Bu algoritmalar sonucunda hata payı ve hassasiyet denemeleri yaptım. Bu 
aşamada hata payının daha az olduğunu gördüm. Ancak bu hata payı gereken güvenliği 
sağlamamaktaydı. Bunun sebebini de ek olan algoritma olduğunu gözlemledim. İki algoritma 
bağının gereken hassasiyeti bozduğunu ve verimi düşürdüğünü gözlemledim. Bununla beraber 
geliştirdiğim algoritmadaki bir başka sorun da şu idi: Aile üyelerinden benzerliği fazla olan kişileri 
karıştırabiliyordu. Bu da yazdığımız algoritmanın güvenlik sistemi için açığı olduğu anlamına 
geliyordu. Bunun üzerinde de çalışarak gereken geliştirmeleri yaptım. Bu geliştirme aşaması ise 
şu şekilde ilerledi: Öncelikle hatanın neden kaynaklandığını buldum. Aile üyelerindeki (baba
oğul, anne-kız, kardeş-kardeş) yüz benzerliğinden kaynaklanıyordu. Bunu da sayısal anlamda 
ispat olarak, kullanılan algoritmalarda iki farklı sayısal mantık kullandığından bahsetmiştim. Bu 
sayısal mantığın 0,6 olması durumunda aile üyelerinin benzerliğinden kaynaklanan sorundan 
dolayı ara ara baba-oğul karıştırması yapabiliyordu. Bu hata payını da ortadan kaldırmak için 
geliştirme işlemlerine başladım.

6.Deneme: Değiştirilen algoritmanın geliştirilmesi 

Daha önceden kullandığım, geliştirdiğim algoritmalarının eksikliklerini göz önüne aldığımda 
yapılan hataları tekrarlamayarak yeniden algoritmayı yazmaya başladım. Bu algoritma temel 
anlamda fotoğrafları manuel olarak yüklenmesini ve ardından fotoğrafları data-veri- haline matris 
işlemleri ile sağlayarak kullanmaktadır. Yazılan algoritmada face-recognition, dlib, cmake, 
opencv, os, numpy kütüphaneleri kullanılmıştır. Algoritma geliştirme işlemlerinin sonlandırılası 
sonucunda deneme aşamalarına geçtim. Bu deneme aşamaları sonucunda kullandığım ve 
geliştirdiğim farklı algoritmalardan en verimlisi, en az hata payına sahip olan ideal algoritmayı 
yazmış oldum. Bununla birlikte aile üyelerindeki benzerlikten kaynaklanan hata payını da 
düzeltmiş oldum. Bunu da algoritmanın sayısal mantığını 0,6 yerine 0,5 ile değiştirerek sağlamış 
oldum. Bu algoritma sayesinde kişileri hatasız bir şekilde, mesafe fark etmeksizin doğru bir 
şekilde tanıyordu. 
Görsel 1’de gösterildiği üzerine kişileri doğru bir şekilde tanıyabiliyordu. Bunun yanında görsel 
1’de gösterilen kişilerin bir önceki adımda aile üyelerinin benzerliğinden kaynaklanan hatada 
örnek gösterilen kişilerdir. Bu aşamada da görüyoruz ki, algoritma aile üyeleri de dahil olmak 
üzre tanıma işlemini olabildiğince az hata payı ile yapabilmektedir. 

7.Deneme: Algoritmada hatanın giderilmesi 

Algoritmadaki tanıma hassasiyeti sorunsuz bir şekilde çalışıyordu ancak ekstra olarak bir hata 
daha fark edilmiştir. Bu hata da açılan anlık kamerada görünen fotoğraf şeklindeki kişileri de 
algoritmanın tanıması ve adlandırmasıdır. Bu çok büyük bir güvenlik eksiğidir. Sonuç olarak 
algoritmamız güvenlik sebebiyle kullanılacağı için girişe izni olamayan kişilerin girişe izni olan 
kişilerin fotoğraflarını kullanarak giriş işlemini başarılı bir şekilde yapabilmesi bizim algoritma 
için güvenlik eksiği olduğunu gösterir.
Bu güvenlik açığının giderilmesi için farklı yöntemler geliştirilebilir. Örneğin Göz kırpma 
işlemi, gülümsemek, yüzünüzü sağa-sola çevirmek, aktivasyon kontrolü vb. Kişiden istenen 
anlık hareketler ile canlılık faktörü etkinleştirilmiş olur. Bu yöntemlere ek olarak açılan anlık 
kameradaki derinlik faktörünün ölçülmesi ile olabilir. Peki bu yöntemlerden hangisi en verimli 
yöntem olacaktır, deneyerek görelim. 

8.Deneme: Canlılık faktörünün etkinleştirilme işlemleri  

İlk işlem, aktivasyon kontrolü oldu. Aktivasyon kontrolü, kullanıldığı yere göre değişik 
anlamlara gelebilir. Benim kullandığım alanda kamera karşısındaki hareketi ölçmemizi sağlar. 
Bu işlem sonucunda anlık olarak açılan kameramızda, herhangi bir hareket var mı, yok mu bunu 
kontrol etmemizi sağlayan kod dizinidir. Bunun sayesinde ekranda hareket yok ise kamera 
karşısında gösterilen yüzün canlı değil de cansız (fake) bir fotoğraf olduğunu fark edip, 
algoritmamızı da buna göre geliştirmemizi sağlamış oluruz. Temel anlamda arka planda açılan 
anlık kameradaki görüntüyü gri tona dönüştürerek hareketi ölçüyor. Bu ölçme işlemi sayısal 
anlamda değil, hareketin varlığı ya da yokluğu türünden bir ölçüm oluyor. Bu sayede de anlık 
açılan kamerada önce hareketi kontrol edip ardından da yüz tanıma algoritması devreye 
girmektedir. 
Programımız kameraya gösterilen ekranın canlı mı yoksa fake mi olduğunu ekrandaki canlılık 
faktörünü ölçerek belirlemeye çalışmaktadır. Ancak bu aşamada şöyle bir sorun oluşmakadır. 
Açılan anlık kameraya fotoğraf gösterdiğimiz zaman yer yer fotoğrafın hareketinden etkilenerek 
canlılık faktörünü etkinleştirmiş olabiliyoruz. Bu duruma ek olarak da bu denemede oluşan 
güvenlik açıklarından bir tanesi ise kameraya fotoğraf yerine video gösterdiğimiz zaman hareket 
az bile olsa o az hareket canlılık faktörünü etkinleştirmiş olabilmekte idi. Anlaşılacağ üzere bu 
aşamada ve yöntemde hassasiyet ve hata payı istediğimiz aşamada değildi.  

9.Deneme: Canlılık faktörünün etkinleştirilme işlemleri 

Bir sonraki adımda ise 3D Evrişimsel bir ağ kullanmayı denedim. Bu aşamada kullanılan 
yöntemden bahsedelim. Öncelikle bu kod dizinini githup sitesinden hazır halde buldum ve 
geliştirmeye çalıştım. Hazır halde alınan kodlarda sürüm, kullanım yöntemi, yıl, kütüphane 
hatalarının çok sık olmasından dolayı çok kullanılan bir yöntem değildir. Ancak benim yapmak 
istediğim şey, kullanılacak yöntemi hazır halde bularak geliştirip, güncel sürüme getirerek, 
hatalarını çözüp kullanmaktı. Bu geliştirme işlemi çok fazla zamanımı aldı. Çünkü kullanılan 
kütüphanelerin sürümleri eski olmakla beraber kullanılma yöntemi de değişmişti. Güncel hale 
getirdikten sonra kodu çalıştırdım.Temel anlamda çalışma mantığından bahsedelim. Bu kod 
dizini 3 farklı dosyadan oluşmaktadır. İlk olarak her zaman kullandığımız kişilerin verilerinin ve 
isimlerinin tanımlandığı kod dosyası vardı. Ardından 3D evrişimsel sinir ağının tanımlandığı 
kod dosyası mevcuttu. Bu kod dosyasında asıl işlem yapılmaktaydı. Peki nasıl? Sequential() 
fonksiyonu ve Keras kütüphanesi kullnalarak açılan anlık kameradaki görüntünün 3 boyutlu 
verisini kullanarak sayısal veriye çevirip 3 boyutlu ölçüm yapmaktaydı. Bu 3 boyutlu ölçümün 
2 boyuttan farkı ise 2 boyut kameraya fotoğraf gösterdiğimiz zaman bu ekranı düz (2 boyut) 
olarak algılarken 3 boyut ise daha detaylı inceleme ile kamera görüntüsünün 3 boyutlu olup 
olmadığını ölçme işlemidir. Eğer kamerada canlı kişi var ise bunu canlı 3 boyutlu alarak 
ortamdan kişiyi ayırt etmeye yarar ve bu sayede canlı olup olmadığını anlamış oluruz. Ancak 
yazılımda sadece 2 boyut kullandığımız zaman gösterilen canlı-cansız kişinin kamera 
görüntüsünden canlı veya cansız olup olmadığını anlayamaz. İlk başta hatasız bir şekilde çalıştı. 
Ekranda görülen kişinin adına “7” diyerek tanıtma işlemini sağladım. Telefondan fotoğraf 
gösterdiğim zaman canlılık hatası olarak çıktı verdi, anlı olarak kameraya göründüğü zaman ise 
tanıma işlemine başladı. Ve hatasız bir şekilde tanıdı. Çıktılar Yukarıdaki görsellerde 
verilmiştir. Ancak ortam özelliklerinden dolayı hata payı giderek artmaktaydı. Başarısız 
çıktıların görselleri aşağıda verilmiştir. 
Burada anlık kamerada görülen kişinin tanımlı ve canlı olduğu halde canlılık hatası vererek 
yazılımın ve algoritmanın eksik olduğunu gözlemliyoruz. Bunun sonucu ise algoritmada olan 
eksiklikler ve bununla beraber kamera hassasiyetiyle beraber ortamdaki özelliklerin optimum 
olmamasından kaynaklanmaktadır. Hata payının bu kadar bariz ve yüksek olması yazılım ve 
algoritmanın işlevsel olmadığını göstermektedir. Yazılım kısmında algoritmayı ne kadar 
geliştirirsek geliştirelim ortam özelliklerinden kaynaklanan hataların olmasından dolayı 
algoritma gene başarısız olacaktı.  

10.Deneme: Algoritma seçilmesi 

Algoritma araştırmalarına başladım ve bulduğum farklı algoritmaları kullanarak programımı 
çalıştırmaya çalıştım. Ancak bulduğum algoritmaların içerisinde bulunan bazı hazır kod 
dosyaları mevcuttu. Bu kod dosyaları nedir? Bu kod dosyaları algoritmanın eğitileceği 
yöntemleri belirleyen model dosyalarıdır. Bu model dosyaları hazır halde bulunur ve sonradan 
değiştirilemez. Yazdığım program da bu hazır halde bulunan model dosyalarını açmadı ve 
çalıştırmadı. Bu yüzden de bulduğum farklı algoritmaları kullanamadım. Sebebi ise dosyaların 
type’ı ile benim programımın type’ının uyumsuz olmasından kaynaklanıyordu. 

11.Deneme: İdeal algoritmanın seçilmesi 

Elde edilen başarısız algoritma denemeleri sonucunda öncelikle daha kesin bir algoritma 
yöntemi bulmam gerekiyordu. Bu algoritmaya da ortam şartları ve özellikleri etki etmemesi 
gerekiyordu. Araştırmalarım sonucunda ve mantık olarak düşündüğümüz zaman kameraya 
gösterilen fotoğraftaki kişi gözlerini hareket ettiremez veya kırpamaz idi. Bu düşüncenin 
sonucunda da yazacağım algoritmada öncelikle göz kırpma ve göz hareketlerini hissederek 
kameradaki kişinin canlı kişi olduğuna karar verip son adım olarak da tanıma işlemine geçmesi 
gerekiyordu. Tanıma işlemi kod dizini zaten sürekli kullandığım kodlardan oluşmaktaydı. Bu 
koda ek olarak da göz kırpma işlemini algılayan bir algoritma yazdım. Ve bu iki farklı kodu tek 
kod dizininde birleştirdim. Ancak bu sefer de iki farklı algoritma çakışarak algoritmaları 
yazdığım spyder uygulaması hata vererek donmaya başladı. Yani anlaşılacağı üzere birleştirilen 
kodlarda herhangi bir kod hatası olamamakla beraber mantık hatası yani kodların çakışmasından 
dolayı oluşan hatalar mevcuttu. Bunun üzerine kullanacağım algoritma yöntemini kesinleştirip 
kodu güncellemeye başladım. 

12.Deneme: İdeal algoritmanın güncellenmesi

En son ideal algoritmanın seçilmesi sonucunda aynı algoritma üzerinden geliştirme yapmaya 
karar verdim. Bu algoritmanın çalışma prensibi, öncelikle eye_status.py python dosyasının 
çalıştırılması sonucunda daha önceden hazır halde elde edilen göz işlevleri ile algoritmanın 
eğitilmesi sağlanır. Bu işlem değişik göz çeşitlerinin kapalı ve açık hallerinin görselleri ile 
yapılır. Kapalı ve açık gözlerin nasıl olduğunu belirleyerek algoritma bu şekilde eğitilir. Eğitilen 
algoritma ardından eklenen yazılımlar sayesinde açılan anlık kamerada yüzleri belirler, ardından 
gözleri belirler en son ise gözlerde hareket var mı onu inceler. Örneğin, ilk başta gözler kapalı 
olup ardından açılırsa veya ilk başta açık olup daha sonra kapanırsa gözlerin hareket ettiği 
kanısına varıp kameradaki görüntünün canlı bir kişiye bağlı olduğuna karar verir. Bu 
algoritmaya ek olarak da her adımda ortak olarak kullandığımız face_rec.py adlı dosyada yüz 
tanıma algoritması kullanılır. Bu iki dosya birbirleri ile etkileşerek gözlerde hareket olması 
koşulu ile yüz tanıma programı tamamlanmış olur. Bu algoritma dizininin avantajları; ortam 
şartlarına diğer adımlarda olduğu gibi keskin olarak bağlı olmaması ve canlılık faktörünün en 
net şekilde belirlenmesi ve kararlaştırılması ile hassasiyetinin en ideal olması ve hata payının en 
az olmasına neden olur. Ve böylece projemiz geliştirilmeye açık olmak kaydı ile tamamlanmış 
olur. 
Algoritma ve programın çıktısı sonucunda yukarda bulunan cansız fotoğraf adlı görselde 
görüldüğü üzere açılan anlık kameraya fotoğraf gösterdiğimiz zaman ne kadar süre 
gösterildiğinden bağımsız olarak gözler hareket etmediği için program çıktısı sonucu her zaman 
cansız kişi olacak ve tanıma işlemine başlamayacaktır. Ancak aşağıda bulunan canlı kişi adlı 
görselde görüldüğü üzere kameraya canlı kişi görünüp gözlerini hareket ettirince (göz kırpma) 
kamerada görülen kişinin canlı oluğuna karar verip tanıma algoritması devreye girer. Ve daha 
önceden tanıtılmış bir kişi kamera karşısında ise algoritma en verimli şekilde kişiyi tanır. Böylece 
projemizde en ideal şartlar ve hassasiyet sağlanmış olur.   

SONUÇ VE ÖNERİLER 

Kariyer Gelişimine Katkı ve Yaygın Etki 

Güvenlik sistemi hangi alanlarda ve nerelerde kullanılacak? 

Şahsa ait evler, toplu kullanım alanları, başta olmak üzere hapishanelerde, hastanelerde, alışveriş 
merkezlerinde, askeri alanlarda, devlet dairelerinde kullanılabilir. Buradan anlaşılacağı üzere 
herhangi bir kullanım kısıtlaması yoktur. İhtiyaç anında insanın olduğu her yerde kullanılabilir. 

Avantajları nelerdir? 

• Güvenlik sisteminin avantajları, insana gerek kalmadan geçiş işlemlerini 
gerçekleştirebilecektir. Olası bir hata anında geçiş işlemini durdurarak güvenliği 
sağlayacaktır. 
• Yoğunluğu ortadan kaldırabilecektir. 
• Herhangi bir uğraş olmadan (istenirse) aranan suçluları bulabilecektir. 

Oluşturduğum bu algoritma ve program sayesinde zamandan tasarruf etmek mümkündür. 
Projedeki amaç insanlığa hizmet etmek olup, insan hayatını daha pratik hale getirmektir. 
Gereken geliştirmeler sonucunda program ve algoritma uygun şekillerde gerekli bağlantılar ile 
gerek özel gerek ise toplu alanlarda kullanılabilir hale getirilebilirdir. Birkaç örnek verecek 
olursak; anahtarını evde unutan insanlar hiçbir zaman anahtara gerek duymadan kedi evine ya 
da programa tanıtılmış evlere girebilecektir. Bunun sayesinde hem anahtar kavramı ortadan 
kalkmış olacak hem de istenmeyen problemler ortadan kalkmış olacaktır. Program ve algoritma 
güvenlik sistemi amaçlı da kullanılabilecektir. Mesela toplu taşıma alanlarındaki kameralar, 
toplu alanlarda bulunan kameralar ve AVM giriş-çıkışlarındaki kameralara gereken 
geliştirmeler eklendiği ve algoritma geliştirildiği takdirde aranan kişileri, kaybolan çocukları, 
suçluları herhangi bir insan gücü olmadan tespit edebilecektir. 













