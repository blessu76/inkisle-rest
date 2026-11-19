---
title: İki ücretsiz deniz ve tek bir kilit açma: ödemeyi nasıl sadeleştirdik
description: Inkisle, 1. ve 2. denizleri ücretsiz tutuyor ve geri kalanını tek bir satın almayla açıyor: Tüm Denizlerin Kilidini Aç. Tüketilen mürekkebin nasıl ayarlandığını, kilidin kodda nasıl hesaplandığını, geri yükleme ve iadelerde çizdiğimiz sınırları ve henüz test etmediklerimizi anlatıyoruz.
slug: two-free-seas-and-one-unlock
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, uygulama içi satın alma, tüketilmeyen, ücretsiz denizler, satın almaları geri yükle, mobil oyun
image_alt: İki açık ada, arkasında kilit simgeli bir ada sırası ve bu sıranın üzerine yatay duran bir anahtar.
published: 2026-11-19T19:17+09:00
---

iOS için geliştirdiğimiz ada fethi strateji oyunu Inkisle, artık 1. ve 2. denizleri ücretsiz tutuyor ve 3. ila 30. denizleri (28 deniz) tek bir satın almayla açıyor: Tüm Denizlerin Kilidini Aç. Tüketilen mürekkep satış ayarlarında yer alıyor, ancak yayımlanmadı ve gerçek cihazda test edilmedi. Altı bahşiş ürünü olduğu gibi kalıyor. Mağaza ürünleri kayıt aşamasında, ancak inceleme için gönderilmedi ve gerçek cihazda test edilmedi; bu yüzden satın alma henüz doğrulanmış değil. Oyun geliştirme aşamasında ve henüz yayımlanmadı. Bu yazı fiyat ya da tarih belirtmiyor.

## Neler değişti

İlk tasarımda her aşama ücretsizdi ve zorluğu düşüren mürekkep küçük tüketilen ürünler olarak satılıyordu. 15 Kasım'da sorumlu kişi bunu değiştirdi. **1. ve 2. denizler ücretsiz, Tüm Denizlerin Kilidini Aç ise tek seferlik tüketilmeyen bir satın almadır.** Tüketilen mürekkep (5'li ve 15'li paketler) satış ayarlarında yer alıyor, ancak yayımlanmadı ve gerçek cihazda test edilmedi. Mürekkep yıldızlarla da kazanılıyor: her 5 yıldız için 1, bir boss'u yenmek için 2. Daha önce satın alınan mürekkep de çalışmaya devam ediyor.

## Kilit hesaplanıyor

Kilitli deniz sayısı koda elle yazılmıyor. Toplam deniz sayısından ücretsiz deniz sayısı çıkarılarak bulunuyor. Bugün bu 30 − 2 = 28 ediyor ve deniz eklendiğinde satın alma sayfasındaki "N denizi açar" metni de buna göre güncelleniyor. Hazırladığımız satış metni, yeni denizlerin de dahil olduğunu vaat ediyor.

- Haritada 3. denizden itibaren olan aşamalarda kırmızı bir kilit var ve birine dokunulunca aşama yerine mağaza açılıyor.
- Satın alma ya da geri yükleme hepsini açıyor.
- Bir zafer sonrasında bir sonraki aşama kilitli bir denizdeyse oyun haritaya dönüyor.

## Ürün yokken uygulama çalışmalı

Mağazada henüz ürün yoksa ya da fiyat sorgusu başarısız olursa yalnızca satın alma düğmesi devre dışı kalıyor ve "yakında" notu görünüyor. Uygulama çökmüyor. Fiyat, sayfa her açıldığında yeniden sorgulandığı için ürün oluşturulduğunda kod değiştirilmeden çalışır. Şu an tam olarak bu aşamadayız. Ürün kurulumu mağaza tarafında engelli olduğu için gerçek satın alma akışını hiç çalıştırmadık.

## Bilerek çizdiğimiz sınırlar

| Durum | Davranış |
|---|---|
| 2. denizi zaten geçmiş bir oyuncu | Kilitli. Kayıtlar ve yıldızlar kalır, satın alma ya da geri yükleme onları yeniden açar |
| Başka bir cihaz | İlerleme iCloud üzerinden gelir, ancak kilit açılmaz. Orada "Satın almaları geri yükle" dokunun |
| İadeler | Erişimi geri almıyoruz |
| TestFlight "hepsini aç" | İlerleme kilidini kaldırır ama ödeme kilidini kaldırmaz, böylece satın alma akışı sandbox'ta test edilebilir |

İadeden sonra erişimi geri almamak hem bir tercih hem de bir sınırlama. Flutter'ın `in_app_purchase` paketinin iadeyi bildiren bir durumu yok ve bu ölçekte makbuzları bir sunucuda doğrulamamaya karar verdik. Bu değerlendirme bir tahmin **[doğrulanmadı]**.

## Kontrol etmediklerimiz

- Gerçek bir cihazda satın alma ya da geri yükleme yapmadık **[doğrulanmadı]**. Şimdiye kadar widget testleri (kilit, mağaza, satın alma, kilit açma) ve StoreKit yapılandırmasının bir kontrolü var.
- 375px ve 320px görünümleri bir simülatörle değil, widget testleriyle kapsandı **[doğrulanmadı]**.
- Android aynı kod yolunu kullanıyor, ama kayıtlı ürün olmadığı için orada ödemeyi test edemedik **[doğrulanmadı]**.
- Korece ve İngilizce dışındaki 11 dildeki satın alma metinleri makine çevirisi **[doğrulanmadı]**.

## Sık sorulan sorular

### Inkisle'ın ne kadarı ücretsiz?

1. ve 2. denizler. Tüm Denizlerin Kilidini Aç satın alındığında diğer 28 deniz birlikte açılır. Oyun henüz yayımlanmadı.

### Kaç kez satın almam gerekiyor?

Bir kez. Tüketilmeyen bir satın alma; yeni denizlerin de dahil olması için tasarlandı.

### Bahşişler oyunu etkiliyor mu?

Hayır. Altı bahşiş ürünü oyunda hiçbir avantaj sağlamıyor ve olduğu gibi kalıyor.
