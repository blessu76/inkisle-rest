---
title: Uygulama içindeki sürüm notları: 12 dilli bir sayfa ve uzunluk kontrolü
description: Inkisle'ın sürüm notları bir web sayfası değil, Ayarlar içinde bir sayfadır. Her derlemenin notlarının 12 dilde nasıl yazıldığı, öğe sayısı ve uzunluğu kontrolleri ve boş bir sayfa göstermiş olan test hatası anlatılıyor.
slug: release-notes-inside-the-app
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, sürüm notları, yerelleştirme, çok dilli, test, mobil oyun
image_alt: Ekranın alt kısmından yukarı doğru yükselen bir kağıt, üzerinde bir sıra halinde on iki küçük dil sekmesi.
published: 2026-11-20T17:45+09:00
---

iOS için geliştirdiğimiz ada fethi strateji oyunu Inkisle'ın sürüm notları, Ayarlar'dan açılan bir uygulama içi sayfadır; bir web sayfası değildir. Her derlemenin notları 12 dilde yazılır ve bir kontrol betiği öğe sayısını ve uzunluklarını doğrular. Derleme 34'ün kontrolü 0 hata ve 0 uyarı verdi. Oyun hâlâ geliştirme aşamasında ve henüz yayımlanmadı.

## Web sayfasını kaldırdık

Başlangıçta ana ekranda bir "Sürüm Notları" bağlantısı ve bir bilgi düğmesi (ⓘ) vardı. Derleme 32'de ikisini de kaldırdık. Bilgi penceresindeki içerik (gizlilik politikası, koşullar, sürüm, açık kaynak lisansları, işletmeci, iletişim ve 16+ uyarısı) Ayarlar'a taşındı ve sürüm notları, oradaki "Sürüm notları" satırından açılan bir sayfa oldu. Web sitesindeki sürüm notları sayfasını da 15 Kasım'da kaldırdık. Ayrı bir site olmadığı için uygulamanın içindeki metin tek kaynaktır.

Sayfa, diğer açılır pencerelerimizle aynı çerçeveyi kullanır (InkSheet). Ekran yüksekliğinin en fazla %60'ını kaplar, başlık satırı ve kapatma X'i (48×48) yerinde kalır ve yalnızca içerik sayfanın içinde kayar.

## Bir derleme, bir dosya, 12 dil

Her derleme için `release_notes/<build>.json` dosyası başlığı, girişi ve öğeleri 12 dilde tutar (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). Dosyalar, uygulamayla birlikte gelen `assets/release_notes.json` içinde paketlenir ve sayfa bunu okur.

## Uzunluk ve sayı kontrolleri

Bir kontrol betiği dosyaları okur ve kural ihlallerini bildirir.

- **RN06:** bir öğe en fazla 200 karakter olmalıdır. Almanca metin uzundu, bu yüzden derleme 34'teki sezon sonu öğesi 183 karaktere kısaltıldı. Derleme 31'de, bir satın alma öğesini sınırın içinde kalması için ikiye böldük.
- **RN05:** 3 ila 6 öğe önerilir. Bu yalnızca bir uyarıdır ve yayımlamayı engellemez. Kalan uyarılar 1 ya da 2 öğesi olan eski derlemelerde; yazılanın dürüst bir kaydı olduklarından onları olduğu gibi bıraktık.
- Mevcut sürüm ve derleme numarası için bir kayıt yoksa bir test başarısız olur; bu yüzden her derleme numarası artışında 12 dilli notun önce yazılması gerekir.
- iOS yükleme betiği, yeşil kapıdan önce (biçim, analiz, testler) sürüm notları kontrolünü çalıştırır.

## Boş bir sayfayı gören test

Sürüm notları sayfasıyla ilgili iki test boş bir sayfa görmeye başladı. Sorun uygulamada değil, testteydi. Paket gerçek bir varlık dosyasıdır ve büyüdükçe, ekranın yerleşmesini bekleyen `pumpAndSettle`, dosya okuması bitmeden sona erdi. Testleri sayfayı açacak, `runAsync` ile 300 ms bekleyecek ve sonra yeniden çizecek şekilde değiştirdik. Uygulama kodu değişmedi.

## Kontrol etmediklerimiz

- Korece ve İngilizce dışındaki çeviriler makine çevirisidir ve ana dili konuşanlar tarafından gözden geçirilmedi [doğrulanmadı].
- Sayfanın gerçek bir cihazda %60 yükseklikte açıldığını görmedik. 375×667 ve 320×568'de yapılan widget testleri bunun yerini tutuyor [doğrulanmadı].

## Sık sorulan sorular

### Inkisle'ın sürüm notlarını nerede bulurum?

Uygulamada Ayarlar'daki "Sürüm notları" satırına dokunun, bir sayfa açılır. Ayrı bir web sayfası yoktur. Oyun henüz yayımlanmadı.

### Kaç dilde yazılmış?

12 dilde. Korece ve İngilizce dışındakiler makine çevirisidir ve henüz gözden geçirilmedi.

### Bir öğe çok uzunsa ne olur?

Bir öğe 200 karakteri aşarsa kontrol betiği bir hata bildirir ve biz onu kısaltır ya da ikiye böleriz.
