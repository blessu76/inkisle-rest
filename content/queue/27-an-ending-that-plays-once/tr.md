---
title: Yalnızca bir kez oynayan bir son ve onu yeniden görmek için bir deniz feneri
description: Inkisle'ın 1. sezon sonu, 30. perdenin son aşaması ilk kez geçildiğinde tam olarak bir kez kendiliğinden oynar. Tekrar oynatma kurallarını nasıl belirledik, bunu zaten geçmiş oyuncular ve 10. perde sonu nasıl ele alınıyor, ve çevirilerde ile gerçek bir cihazda neleri henüz denetlemedik.
slug: an-ending-that-plays-once
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, 1. sezon, son, açık son, deniz feneri, oyun tasarımı, mobil oyun
image_alt: Sakin bir denizde tek bir deniz feneri yanan yalnız bir ada ve önünde duran harita rotası.
---

iOS için ada fethi strateji oyunumuz Inkisle'ın 1. sezon sonu, 30. perdenin 8. aşaması ilk kez geçildiğinde kendiliğinden bir kez oynar. Tekrar izlemek için oyuncu 30. perdenin en üstündeki deniz fenerine dokunur. Sonda kapanış sözü yok; tek iz "Inkisle · Season 1". Bu yazı, sonun ne gösterdiğinden çok, ne zaman oynayıp ne zaman oynamadığı ve bu kuralları nasıl belirlediğimiz üzerine. Oyun geliştirme aşamasında ve çıkmadı.

## Dört kural

Sonu eklediğimizde belirlediğimiz tekrar oynatma kuralları bunlar.

- **Bir kez, ilk geçişte.** 30. perdenin 8. aşaması ilk kez kazanıldığı anda kendiliğinden oynar.
- **Bir daha kendiliğinden asla.** Aynı aşamayı yeniden kazanmak ya da uygulamayı yeniden başlatmak onu otomatik oynatmaz.
- **İstenildiği an atlanabilir.** Tek dokunuş son sabit kareye götürür ve hareketi azalt açık olan bir cihaz sabit kareden başlar.
- **Tekrar, deniz fenerinden.** 30. perdenin en üstünde bir deniz feneri durur ve ona dokunmak aynı sonu yeniden oynatır.

Bir son 30 saniyeden kısa olsa bile, "bir kez, kazandıktan hemen sonra" bir armağan, "her kazandığında" ise bir kesinti diye karar verdik.

## "Zaten görüldü" nerede yazılı

Oynayıp oynamadığı, kayıt verisinde bir hikâye anahtarı olarak tutulur. Sezon sonunun anahtarı, 10. perde sonunun anahtarından **bilerek ayrı**. İkisi tek anahtar kullansaydı, 10. perde sonunu görmüş bir oyuncuda sezon sonu da görülmüş sayılabilirdi. Bunu bir test denetler: 10. perde sonunu izlemek sezon anahtarına dokunmaz.

## Zaten geçmiş oyuncular

Biri, son var olmadan önce 30. perdenin 8. aşamasını geçmiş olabilir. O kayıt için ilk geçiş anı çoktan geçti, bu yüzden kendiliğinden hiçbir şey oynamaz ve yalnızca deniz feneri görünür. Geçip giden bir anı zorlamamayı ve oyuncunun istediği zaman basmasına izin vermeyi seçtik.

Aynı değişiklikte 10. perdenin deniz feneri de ait olduğu yere, 10. perdenin en üstüne taşındı.

## Testlerin sabitledikleri

Sonun 18 testi var. Bu kurallara bağlı olanlar:

- 30. perdenin 8. aşamasının ilk galibiyetinde tam olarak bir kez oynar, oyuncu yeniden girdiğinde oynamaz.
- 30. perdenin 7. aşamasında ya da 29. perdenin 8. aşamasında hiçbir şey oynamaz.
- 30. perdenin 8. aşamasını zaten geçmiş bir kayıt otomatik oynatma almaz, yalnızca deniz fenerini alır.
- Widget testlerinde 375px ve 320px'te oynatma, atlama ve yarıda ayrılma çalışır.
- 12 dilin tamamının metni taşmadan sığar.

## Kapanış sözü yok

Son satır, Korece, "Derin su yansıtır." (「깊은 물이 비친다.」). Hiçbir dil sürümünde "Son" gibi bir sözcük yok ve alttaki iz "Inkisle · Season 1". Tekrar oynatma kuralları da aynı düşünceden gelir: hikâye kapanır, ama uygulama kapanmaz. 30. perdeden sonra oyuncular perdeleri yeniden oynayabilir, üç yıldız toplayabilir ve skor tablolarına bakabilir.

## Denetlemediklerimiz

- **Korece ve İngilizce dışındaki 10 dildeki son metni makine çevirisi ve gözden geçirilmedi.** Ekranda yalnızca birkaç satır olunca bir çevirinin kalitesi hemen belli olur.
- Yavaş solma, altın harfler ve çan sesinin düzeyi gerçek bir cihazda görülmedi.
- 375px ve 320px görünümleri yalnızca widget testlerinde denetlendi ve bu testlerin yazı tipi gerçeğinden çok daha geniş.
- 2. sezonun olup olmayacağı belli değil ve çıkış tarihi yok.

## SSS

### Son kendiliğinden kaç kez oynar?

Bir kez, 30. perdenin 8. aşaması ilk kez geçildiğinde. Sonrasında oyuncu tekrar görmek için 30. perdenin en üstündeki deniz fenerine dokunur.

### Son atlanabilir mi?

Evet. Tek dokunuş son sabit kareye atlar ve hareketi azalt açıkken sabit kareden başlar.

### Son metni her dilde gözden geçirildi mi?

Hayır. Korece ve İngilizce dışındaki çeviriler makine çevirisi ve henüz gözden geçirilmedi.
