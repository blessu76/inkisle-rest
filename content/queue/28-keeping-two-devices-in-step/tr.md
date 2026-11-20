---
title: İki cihazı uyumlu tutmak: iCloud eşitlemesini ortak bir uygulama kitine taşımak
description: Inkisle'ın ilerlemesi, mürekkebi ve ayarları iCloud üzerinden cihazlar arasında zaten eşleştiriliyordu. 16 Kasım'da bu köprüyü ortak bir uygulama kitine taşıdık. Kayıtlı verileri nasıl bozulmadan tuttuk, hiç küçülmeyen birleştirme kuralları, satın alma işaretinin nasıl ele alındığı ve gerçek cihazlarda henüz kontrol etmediklerimiz.
slug: keeping-two-devices-in-step
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, iCloud, cihazlar arası eşitleme, kayıt verisi, birleştirme, mobil oyun
image_alt: İnce bir iplikle birbirine bağlanmış, farklı boyutlarda iki ekran; iki haritadaki adalar aynı renklerle boyanmış.
---

iOS için geliştirdiğimiz ada fethi strateji oyunu Inkisle'da ilerleme, mürekkep ve temel ayarlar (dil ve takma ad), aynı Apple Kimliği'ne sahip cihazlar arasında oyuncunun kendi iCloud anahtar-değer depolaması üzerinden eşleştirilir. Bu eşitleme zaten vardı. 16 Kasım'da yaptığımız şey onu kurmak değil, kendi yazdığımız bir köprüyü ortak bir uygulama kitine taşımaktı ve en büyük endişe kayıtlı tek bir değeri bile kaybetmemekti. Gerçek bir iPhone ile iPad arasında gidiş-dönüşü henüz kontrol etmedik. Oyun geliştirme aşamasında ve yayımlanmadı.

## Neyi taşıdık

O günkü sorumlunun talimatı, Apple cihazları arasında oyun verisi eşitlemesinin zorunlu olması ve ortak uygulama kitine girmesiydi. iCloud anahtar-değer yetkisinin zaten açık olduğunu, uygulamanın içinde de kendi Swift köprümüzün ve depolama sarmalayıcımızın çalıştığını gördük. Bu yüzden:

| Parça | Ne değişti |
|---|---|
| Köprü | Kendi Swift köprümüzü ve sarmalayıcıyı sildik, kitin platform depolamasına geçtik: iOS'ta iCloud, başka yerlerde yalnızca yerel |
| Anahtarlar ve kodlama | Depolama anahtarlarını, dize kodlamasını ve depolama tanımlayıcısını olduğu gibi bıraktık |
| Okumadan önce | iOS'ta, okumadan hemen önce eşitlemeyi bir kez uyandırmak (başarısız olursa eşitleme devam eder) |
| Proje ayarları | iCloud yeteneğini proje dosyasına da ekledik |

## Veri kaybetmemek

Anahtarlar ve biçimler aynı kaldığı için yeni derleme eskisinin yazdığını okur, eski derleme de yenisinin yazdığını okur. Her iki yönü de testlerle sabitledik: eski biçimli bir parçayı yeni kodla okumak, yeni bir parçayı eski kodla okumak ve eski bir ayar parçasını okumak. Yalnızca kod silindi; kayıtlı değerlere dokunulmadı.

## Birleştirme asla küçülmez

İki cihazın ilerlemesi farklı olduğunda uygulamanın kendi birleştirmesini korduk. Kitin de bir birleştiricisi var, ama onu kullanmadık. Uygulamanın birleştirmesi zaten yalnızca büyüyor ve aynı anahtarları ve biçimi korumak, ona dokunmadan bırakınca daha güvenliydi.

- Aşama başına yıldızlar ve en iyi rekorlar büyük olan değeri alır.
- İlerleme, daha ileri giden cihazı alır; mürekkep ve ayarlar yalnızca birleşir, asla küçülmez.
- Buluttaki değer en son gönderdiğimizden farklıysa, aynı anahtarın üzerine yazmış eski bir derlemeden toparlanmak için yeniden göndeririz.

## Satın alma işaretine ne oldu

Önceki bir yazıda kilit açmanın başka bir cihaza geçmediği söylenmişti. Bu çalışma bunu değiştirdi. Eşitleme parçası artık Tüm Denizlerin Kilidini Aç'ın satın alındığına dair bir işaret taşıyor ve onu okuyan başka bir cihaz da açılıyor. İşaret **yalnızca büyür.** Onu içermeyen bir parça işareti geri almaz; biz yeniden göndeririz.

Bu, sorumlunun "zorunlu eşitleme" talimatını izleyen bir tasarım değişikliği ve tek bir sınırı var: işaret bir kez eşitlendiğinde, iade onu diğer cihazlarda geri çekmez. İadelerin nasıl ele alınacağı bir politika kararı olarak bırakıldı. Satın alma akışının kendisi de henüz gerçek bir cihazda çalıştırılmadı.

## Boyut ve testler

iCloud anahtar-değer depolamasının toplam bir sınırı var (1 MB). 240 aşamanın tamamı bitirilmiş bir kaydın eşitleme parçası yaklaşık 6,3 KB'tır ve bir test onu 16 KB'ın altında tutar. 14 yeni test; değişmeyen anahtarları ve kodlamayı, iki cihazın birleştirilmesini, satın alma işaretinin yayılıp asla geri çekilmemesini, çevrimdışıyken veya oturum açılmamışken yerel kalmayı ve tekrar çevrimiçi olduktan sonra birleştirmeyi kapsar. Dört bulut test dosyasında toplam 77 test geçti.

## Neleri kontrol etmedik

- **Bir iPhone ile iPad arasında gerçek bir eşitleme kontrol edilmedi.** Yalnızca gerçek cihazlarda veya TestFlight'ta görülebilir.
- Silmeler diğer cihazlara geçmez, çünkü bu eşitleme yalnızca birleştirir.
- Android için geçerli değil. Veriler cihazda kalır.
- Başka bir cihazdaki eski bir derleme aynı anahtarın üzerine yazarsa satın alma işareti kısa süre kaybolabilir ve yeni derleme onu yeniden gönderir.
- Gizlilik politikası artık bu eşitlemeyi anlatıyor: oyun verileri oyuncunun kendi iCloud'unda tutulur, sunucularımızda değil, ve cihaz ayarlarından kapatılabilir.

## SSS

### Inkisle ilerlemesi bir sunucuda mı saklanıyor?

Hayır. Aynı Apple Kimliği'ne sahip cihazlar arasında oyuncunun kendi iCloud anahtar-değer depolaması üzerinden eşleştirilir ve sunucularımıza gönderilmez.

### Eşitleme kapatılabilir mi?

Evet. iOS ayarlarında bu uygulamanın iCloud'unu kapatmak eşitlemeyi durdurur ve veriyi yalnızca cihazda bırakır.

### Android'de eşitleniyor mu?

Hayır. Android'de veriler cihazda kalır.
