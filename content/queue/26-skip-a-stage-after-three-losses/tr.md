---
title: Üç yenilgiden sonra bölümü atlamak: bedeli olan nazik bir teklif
description: Inkisle'da aynı bölümü üç kez kaybetmek, onu 3 Ink karşılığında atlama teklifini getirir. Teklifin ne zaman geldiği, hangi bölümlerin dışarıda kaldığı, atlanan bölümün deniz haritasında nasıl göründüğü ve nasıl kaydedildiği.
slug: skip-a-stage-after-three-losses
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, bölüm atlama, zorluk, oyun tasarımı, kayıtlı veri, mobil oyun
image_alt: Küçük bir mercan rengi bayrakla işaretlenmiş bir adanın bulunduğu deniz haritası ve o adanın yanından geçip bir sonraki adaya giden noktalı bir yol.
---

iOS için yaptığımız ada fethi strateji oyunu Inkisle'da aynı bölümü üç kez kaybetmek şu soruyu getirir: "Bu bölümü atlayıp daha sonra mı denemek istersin?" Atlamanın bedeli 3 Ink'tir. Atlanan bölüm deniz haritasında bir bayrak alır ve istediğin zaman oynanabilir. Oyun hâlâ geliştirme aşamasında ve yayımlanmadı; bu açılır pencereyi gerçek bir cihazda henüz görmedik.

## Neden atlama teklif ediyoruz

Bazı bölümler zorluk ayarından sonra bile zor kalıyor. Oyuncunun tek bir adada takılıp kalmasını istemedik. Teklif, oyuncuya oyunu bırakmak yerine ilerleyip sonra geri dönme imkânı veriyor.

## Ne zaman sorar

- Açılır pencere, aynı bölümün **üçüncü yenilgisinden** sonra, sonuç sayfası yerleştikten (1,1 saniye) sonra çıkar.
- Oyuncu hayır derse 4. ve 5. yenilgide sormaz. **6. ve 9.** yenilgide ve böyle devam ederek yeniden sorar. Her seferinde sormak ısrarcılık olurdu; yalnızca bir kez sormak ise hâlâ takılı kalan oyuncuyu kaçırırdı.
- Yenilgiler bölüm başına sayılır. Bölümü kazanmak sayacı 0'a döndürür. Zaten geçilmiş veya atlanmış bir bölümdeki yenilgiler sayılmaz.

## Bedeli nedir

Atlamanın bedeli **3 Ink**'tir; oyuncunun oyunda zaten kazandığı ya da satın aldığı aynı Ink. Yeni bir para birimi ya da ürün eklenmedi. Değer, kodda tek bir sabittir; açılır pencerenin metni, düğme ve mağazaya giden bağlantı hep ona uyar.

Önce 1 Ink olarak belirledik, sahibi 2 ila 3 isteyince 3'e çıkardık. Oyuncunun 3'ten az Ink'i varsa atlama düğmesi "Ink yok, mağazayı aç" olur ve mevcut mağaza sayfasını açar. 3 veya daha fazlası olduğunda atlama düğmesi geri gelir.

## Hangi bölümler dışarıda

- 1-1'den 1-4'e kadar olan bölümler; Ink'siz öğretici kısım. Orada atlamak kontrolleri hiç öğrenmemek demek olurdu.
- Oyunun ilk Ink'i hediye ettiği 1-5. bölüm.
- Son bölüm; çünkü açılacak bir sonraki bölüm yok.
- Patron bölümleri dahildir.

## Atlanan bölüm ne demek

- Bir sonraki bölüm açılır ve atlanan bölümün **0 yıldızı** olur. Atlamak geçmek değildir, bu yüzden yıldız satın alınamaz.
- Haritada düğüm mercan rengi bir bayrak alır. Ekran okuyucular "atlandı" ekler. Bölüm kartında şöyle yazar: "Bu bölüm atlandı. Hazır olduğunda yeniden dene."
- Daha sonra geçilirse bayrak kalkar ve yıldızlar normal şekilde kaydedilir.
- Bir deniz ancak bölümleri geçildiğinde tamamlanır; bayraklı bir bölümün de denizi tamamlamak için kazanılması gerekir.
- Son sahne yalnızca gerçek bir zaferle açılır; bu yüzden 10-8'i atlamak onu açmaz.

## Nasıl kaydedilir

Mevcut ilerleme kaydına iki isteğe bağlı anahtar eklenir: bölüm başına başarısızlık sayısı ve atlanan bölümlerin listesi. İkisi de boşsa anahtarlar yazılmaz; eski bir kayıt bayt bayt aynı kalır. Okurken bilinmeyen kimlikler ile negatif veya metin değerleri atılır ve zaten geçilmiş bir bölüm atlama işaretini kaybeder, çünkü geçmek önceliklidir.

iCloud birleştirmesinde daha büyük başarısızlık sayısı korunur, atlama listeleri birleştirilir ve başka bir cihazdaki geçiş önceliklidir. Aynı anlık görüntüyü yeniden birleştirmek hiçbir şeyi değiştirmez ve bir test bunu denetler.

## Neleri kontrol etmedik

- Açılır pencere ve bayrak gerçek bir cihazda veya simülatörde. 375 ve 320 px genişliğindeki widget testleri 16 dil sütununda taşma bulmadı, ancak ekran görüntülerine bakmadık.
- iCloud anlık görüntüsünün üzerine yazan eski bir uygulama sürümünün iki yeni anahtarı düşürüp düşürmediği. Düşürürse geçilen bölümler ve yıldızlar kalır, yalnızca atlama işaretlerinin kaybolacağını düşünüyoruz.
- Korece ve İngilizce dışındaki çeviriler ana dili konuşan biri tarafından gözden geçirilmedi.

## SSS

### Inkisle bölüm atlamayı ne zaman teklif eder?

Aynı bölümü üç kez kaybettikten sonra; denemeye devam edersen 6., 9. yenilgiden sonra ve böyle devam ederek yeniden. İlk bölümler, 1-5 hediye bölümü ve son bölüm dışarıda kalır.

### Atlamanın bedeli nedir, yıldız alınır mı?

3 Ink'tir. Atlanan bölüm 0 yıldız verir. Daha sonra geçersen yıldızları her zamanki gibi alırsın.

### Atlamak bir denizi tamamlar mı veya son sahneyi açar mı?

Hayır. Bir deniz yalnızca bölümleri geçildiğinde tamamlanır ve son sahne yalnızca gerçek bir zaferle açılır.
