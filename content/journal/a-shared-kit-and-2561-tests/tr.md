---
title: Ortak bir kiti yükseltirken neyi koruyoruz: 2.561 testlik bir kapı
description: Inkisle, uygulamalarımızın kullandığı ortak kiti her yükselttiğinde biçim, analiz ve tam test kapısından geçmek zorunda. Bir kit özelliğinin tamamını neden değiştirmedik, zaman testleri yük altında nasıl dalgalandı, son yükseltmede hangi dosyalar değişti ve neleri kontrol etmedik.
slug: a-shared-kit-and-2561-tests
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, ortak kit, testler, Game Center, yükseltme, mobil oyun
image_alt: Aynı biçimdeki birkaç küçük blok tek bir çerçevenin içinde duruyor ve üzerlerinden tek bir yeşil nokta geçiyor.
published: 2026-11-24T12:45+09:00
---

iOS için geliştirdiğimiz ada fethi strateji oyunu Inkisle, birkaç uygulamamızın dayandığı ortak bir kit kullanıyor. Kitin sürümünü her yükselttiğimizde, commit öncesinde tek bir kapı biçimi, statik analizi ve tüm test paketini çalıştırıyor. 19 Kasım'da kiti 0.15.2'den 0.15.3'e taşıdık: kapı 2.561 testi geçti (8 atlandı) ve yalnızca iki dosya değişti, `pubspec.yaml` ve `pubspec.lock`. Bu yazı o sayının nasıl korunduğunu ve yolda nelerin dalgalandığını anlatıyor. Oyun geliştirme aşamasında ve yayımlanmadı.

## Kapının üç adımı var

Tek bir betik bunları commit öncesinde sırayla çalıştırır: kod biçimi değişmemeli, statik analiz 0 sorun bildirmeli ve tüm testler geçmeli. Biri başarısız olursa commit yapmayız. Başka biri "geçti" dediğinde, commit etmeden önce bunu kendimiz yeniden çalıştırırız.

## 14 Kasım: kit özelliğinin tamamını değiştirmedik

Kiti 0.12.0'dan 0.13.0'a taşımak, takma adı ve Game Center lider tablosunu kitin üstlenmesini mümkün kıldı. Sorumlunun talimatı, her oyunun oyuncuya ilk açılışta takma ad belirletmesi ve Game Center lider tablosunda görünmesiydi. Kitin oyuncu özelliğinin **tamamını devralmadık.** Kendi sürümümüzün daha iyi olduğunu düşünmek için dört nedenimiz vardı:

1. Takma ad, iCloud üzerinden cihazlar arasında eşitlenen ayar kaydının içinde duruyor. Onu kitin depolamasına taşımak bu eşitlemeyi bozardı.
2. Zaten 16 dilde bir takma ad sayfamız ve dil ile ekran boyutu kombinasyonları için dondurulmuş testlerimiz var.
3. Lider tabloları 24 dinamik tablo ve değerleri eşitlenen ilerleme kaydından türetiliyor. Taşımak, en iyi skoru saklayan iki yer bırakırdı.
4. Android'deki Play Games'in kullandığı kütüphaneye hâlâ ihtiyacı var.

Yani yalnızca iOS Game Center bağlantısı kite taşındı; tablo kimlikleri, kayıtlı takma adlar ve en iyi skorlar değişmeden devam etti. Geç oturum açmanın ardından birikmiş verinin yeniden gönderilmesi ve takma adın Game Center adıyla önceden doldurulması aynı anda eklendi. 10 test ekledik ve kapı ardından 1.990 testi geçti (7 atlandı).

## Zaman testleri dalgalandı

Bu kapıda iki kez, zamanı ölçen bir test yük altında dalgalandı. 800 yol çizen bir kare bütçesi testi, testler paralel çalışırken bir kez başarısız oldu ve iCloud çalışması sırasında bir performans bütçesi testi bir kez başarısız oldu. İkisi de tek başına çalıştırıldığında ya da tam paket yeniden çalıştırıldığında geçti. Bunu bizim değişikliğimiz olarak değil, yük olarak okuyoruz; ancak nedeni izlemedik. Bütçeleri gevşetmedik.

## 19 Kasım: iki dosya değişti

0.15.3 sürümü herkese açık API'yi olduğu gibi bırakıyor; iCloud eşitlemesindeki bir yeniden saymayı yıkımdan sonra durduruyor ve belge ekliyor. Uygulamada ne kod ne de test değiştirdik. Uygulamanın kullandığı boyut sınırı (512 KB) bilinçli bir tercih, bu yüzden onu korumayı seçtik. Değişen dosyalar `pubspec.yaml` ve `pubspec.lock` idi ve kapı ilk çalıştırmada geçti; bu kez zaman dalgalanması yoktu. Test sayısı 14 Kasım'daki 1.990'dan 2.561'e çıktı.

## Neleri kontrol etmedik

- **Game Center oturum açma, skor gönderme, lider tablosu ekranı ve bir iCloud gidiş dönüşü gerçek bir cihazda kontrol edilmedi.** TestFlight'ta bakacağız.
- 375px ve 320px görünümleri doğrudan görülmedi, 320×568'de widget testleriyle kapsandı.
- Yük altında dalgalanan testlerin kök nedenini bulamadık.
- Buradaki sayılar o günkü kapı sonuçlarıdır ve test sayısı daha sonra değişecek.

## Sık sorulan sorular

### Ortak kit nedir?

Birkaç uygulamamızın birlikte kullandığı bir kod paketi. Inkisle onun takma ad, Game Center ve iCloud eşitleme bölümlerini kullanıyor.

### Kiti yükseltirken neyi kontrol ediyorsunuz?

Tek bir betik, biçimin değişmediğini, statik analizin 0 sorun bildirdiğini ve tüm testlerin geçtiğini kontrol eder. Biri başarısız olursa commit yapmayız.

### Oyun yayımlandı mı?

Hayır. Hâlâ geliştirme aşamasında ve yayımlanmadı.
