---
title: 5-8. bölümdeki takılma: suçlu oyun motoru değil, ekrandı
description: Inkisle'ın 5-8. bölümü takılıyordu. Hiçbir şeye dokunmadan önce ölçtük, maliyetin oyun kurallarında değil ekran çiziminde olduğunu gördük ve bir bilgisayarda bir karenin maliyetini 3,4 ms'den 1,3 ms'ye indirdik. Ne değiştirdik, neyi bıraktık ve telefonda neyi henüz kontrol etmedik.
slug: the-stutter-on-stage-5-8
lang: tr
translation_of: en
category: making-of
keywords: Inkisle, performans, takılma, kare süresi, oyun tasarımı, mobil oyun, optimizasyon
image_alt: Solda dört uzun mor çubuk, sağda dört kısa mercan rengi çubuk; aralarında bir ok ve bütçeyi gösteren kesikli bir çizgi var.
published: 2026-11-25T15:15+09:00
---

iOS için yaptığımız ada fethi strateji oyunu Inkisle, testler sırasında 5-8. bölümde takılıyordu. Kolay tahmin, filoları hareket ettiren ve ele geçirmeleri belirleyen oyun motorunun fazla ağırlaştığıydı. Önce ölçtük. Sorun motor değil, onu çevreleyen ekrandı. Değişiklikten sonra 5-8. bölümde bir karenin maliyeti bilgisayarımızda 3,4 ms'den 1,3 ms'ye düştü. Oyun geliştirme aşamasında ve yayımlanmadı; bu sayılar bir telefondan gelmiyor.

## Ne ölçtük

Bir karede iki tür iş vardır: oyun kurallarını bir tik ilerletmek ve ekranı kurup çizmek. 5-8. bölümde kuralların bir tiki ortalama yalnızca 3 ila 5 mikrosaniye tuttu. Ekran yaklaşık bin kat daha fazla tuttu.

Bu ekran maliyetinin çoğu üç şeyden geliyordu:

1. **Tüm başın üstü ekranı (HUD) her karede yeniden kuruluyordu.** Oyun denetleyicisi her karede bir değişiklik duyuruyordu; bu yüzden güç çubukları, hedef metni, sonuç sayfası, oran çubuğu, rozetler, seçim çubuğu, kriz katmanı ve gelgit düğmesi, hiçbir şey değişmemiş olsa bile yeniden kuruluyordu. 3,4 ms'nin yaklaşık 2,5 ms'si widget kurmaya gidiyordu.
2. **Sayı etiketleri önbelleği ıskalıyordu.** Önbellek anahtarı her sayının tam saydamlığını ve boyutunu içeriyordu; bunlar bir ele geçirme dalgası ya da solma sırasında sürekli değişir. Böylece her kare yeni yerleşimler üretiyordu ve önbellek 600 girdiyi aşınca bütünüyle temizleniyordu; bir karenin her şeyi yeniden yerleştirmesi gerekiyordu. En yavaş yüzde 1'lik karelerde çizim süresi ortalamanın 5 ila 10 katıydı.
3. **Küçük tekrarlanan işler.** Her filo mürekkep rengini iki kez arıyordu, her adanın konumu ve yarıçapı her filo için yeniden hesaplanıyordu ve bir gölgelendirici önbelleği metin anahtarı kullanıyordu.

## Ne değiştirdik

- HUD artık yalnızca gösterdiği bir şey değiştiğinde tetiklenen küçük bir sinyali dinliyor; örneğin tik, duraklatma, hız, kriz durumu, hedefler ya da ipuçları. Boyama eskisi gibi her karede yapılıyor.
- Sayı etiketleri önbelleğin isabet alması için kaba adımlara yuvarlanıyor (saydamlık 32 adım, boyut çeyrek piksel) ve dolduğunda yalnızca eski yarısı siliniyor.
- Tekrarlanan aramalar kare başına bir kez hesaplanıyor ve gölgelendirici anahtarı bir dizgiden kayda dönüştü.

Boyut ve saydamlık yuvarlaması gözle görülmez.

## Sayılar

Bir bilgisayarda, 375 × 667 ekranda, yalnızca öncesi ile sonrasını karşılaştırmak için uygun bir modda ölçüldü.

| | önce | sonra |
|---|---|---|
| 5-8. bölüm, tüm kare, ortalama | 3.433 µs | 1.267 µs |
| 5-8. bölüm, tüm kare, en yavaş %1 | 10.803 µs | 5.182 µs |
| 5-8. bölüm, çizim, ortalama | 818 µs | 201 µs |
| 5-8. bölüm, çizim, en yavaş %1 | 4.540 µs | 1.284 µs |

Saniyede 60 kare çalışan bir oyunun kare başına yaklaşık 16,6 ms'si vardır; dolayısıyla değişiklikten önce bile iş bilgisayarda bu bütçeye sığıyordu. Bu yüzden hissettiğimiz takılmanın başka bir nedeni de olabilir (aşağıya bakın).

## Neleri olduğu gibi bıraktık

Kuralların ve denge kodunun tek bir satırını bile değiştirmedik. Yalnızca ekran katmanı değişti: denetleyicinin güncellemeleri nasıl duyurduğu, hangi widget'ların dinlediği ve çizim önbellekleri. Aynı tohum hâlâ aynı 600 tiklik sonucu veriyor; altın görüntüler, deterministik oyun ve bot simülasyonları için mevcut kontroller yeşil kaldı.

Gerçek bir maliyeti de sonraya bıraktık. Kriz tahmini ekran iş parçacığında çalışır: ölçtüğümüz en ağır bölüm olan 17-3'te ortalama 3,4 ms sürdü ve en yavaş yüzde 1'i 11,8 ms'ye ulaştı; bu, her yarım saniyede küçük bir takılmaya yol açabilir. Bu işi birkaç kareye yaymak aynı sonucu verirdi, ancak kararları değiştirme riski taşıyor; bu yüzden şimdi yapmadık. 5-8. bölümde 0,17 ms tutuyor ve önemi yok.

## Ne ekledik

Motor için ekransız bir kıyaslama testi ve gevşek üst sınırları olan bir performans testi. Maliyetin filo sayısıyla patladığı ya da her karenin fazla bellek ayırdığı türden gerilemeleri yakalar. Sınırları bilerek gevşek tuttuk, çünkü sıkı sınırlar test makinesi meşgul olduğunda hep başarısız olurdu. Varsayılan olarak bu testlerin en ağırı atlanır ve yalnızca istendiğinde çalışır.

## Neleri kontrol etmedik

- **Gerçek bir telefonda saniyede 60 veya 120 kare hızı kontrol edilmedi.** Sayılarımız bir bilgisayardaki ekran iş parçacığı maliyetidir, bir cihazdaki grafik maliyeti değil.
- **Sis perdesi ve şerit katmanları ne ölçüldü ne de değiştirildi.** Tam ekran bulanıklıkla çiziliyorlar; bu da işlemciye değil grafik çipine yük bindirir. 5-8. bölüm telefonda hâlâ takılıyorsa ilk şüphelimiz bu.
- Hiçbir yerleşim değişmediği için tarayıcı çizimine 320, 375, 768 ve 1280 px'te bakmadık.
- Girdinin daha duyarlı hissettirdiği yalnızca bizim beklentimiz.

## SSS

### Inkisle'ın 5-8. bölümü neden takılıyordu?

Ölçümümüz oyun kurallarını değil, her karede yeniden kurulan ekranı ve yeniden yerleştirilen sayı etiketlerini gösterdi. Bunları düzelttik; gerçek telefondaki kare hızı henüz kontrol edilmedi.

### Optimizasyon oyunun oynanışını değiştirdi mi?

Hayır. Kurallara ve denge koduna dokunmadık; aynı tohum öncekiyle aynı sonucu veriyor.

### Telefonda hâlâ takılıyor mu?

Henüz bilmiyoruz. Sayılarımız bir bilgisayardan geliyor. TestFlight'ta gerçek bir cihazda kontrol edeceğiz.
