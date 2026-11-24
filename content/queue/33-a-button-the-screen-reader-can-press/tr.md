---
title: Ekran okuyucunun basabildiği bir düğme
description: Inkisle’ın kapatma simgesi ve deniz feneri sesli okunan etiketlere sahipti, ancak erişilebilirlik eylemleri eksikti. Hem okunan sözcükleri hem de denetim etkinleştirildiğinde ne olduğunu kontrol ettik.
slug: a-button-the-screen-reader-can-press
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, erişilebilirlik, ekran okuyucu, arayüz, widget testleri
image_alt: İki küçük kartta bir çarpı ve bir deniz feneri simgesi var. İki denetimin de çevresinde odak halkası bulunuyor.
---

Inkisle, geliştirilmekte olan bir ada fetih strateji oyunu. Erişilebilirlik çalışmasında oyunun denetimleri ekran okuyucuya nasıl tanıttığına baktık. İki denetim öne çıktı: paneli kapatan çarpı ve haritada son sahneyi yeniden açan deniz feneri. Oyunu iOS için geliştiriyoruz.

## Addan eyleme

İki denetimin de adı vardı. Flutter’ın erişilebilirlik ağacında, simgenin varsayılan açıklamasını değiştirdiğimizde adın bulunduğu düğüm dokunma eylemini kaybetmişti. Eylemi etiketle aynı düğüme bağladık. Testlerde Kapat’ı etkinleştirmek paneli kapatıyor, deniz fenerini etkinleştirmek son sahneyi açıyor.

## Bir kez duymak yeter

Nelerin iki kez okunduğuna da baktık. Filo oranı düğmesi, etiketinde ve görünür yazıda aynı yüzdeyi veriyordu. Açılışı atlama denetiminde ve haritanın numaralı işaretlerinde de benzer tekrarlar vardı. Her biri için, oyuncunun denetimi tanımasına yetecek bilgiyi içeren tek bir sesli etiket bıraktık.

## Sıkça sorulan sorular (FAQ)

### Bu değişiklikler telefonda ekran okuyucuyla denendi mi?

Widget testleri etiketleri ve erişilebilirlik eylemlerini kontrol etti. Değişiklikleri henüz bir iPhone’da VoiceOver ile doğrulamadık.

### Haritadaki deniz feneri ne işe yarar?

Son sahneyi yeniden izlemek için deniz fenerini etkinleştir.
