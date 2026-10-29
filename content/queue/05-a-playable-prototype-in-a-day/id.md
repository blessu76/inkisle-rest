---
title: Prototipe yang bisa dimainkan dalam sehari
description: Enam belas stage, dua laut, dan satu file HTML sekitar 95 KB tanpa permintaan keluar. Bagaimana prototipe ini dibangun, apa yang kami uji di browser headless, dan apa yang tidak bisa kami uji.
slug: a-playable-prototype-in-a-day
lang: id
translation_of: en
category: making-of
keywords: Inkisle, prototipe, prototipe web, mesin game deterministik, game HTML, game mobile, canvas
image_alt: Banyak pulau kecil dengan angka pasukan dan armada yang menyeberangi laut di prototipe Inkisle.
---
Sebelum membuat aplikasi, kami ingin sesuatu yang bisa dimainkan di ponsel. Pada 2026-10-29 kami membangun prototipe web dalam satu hari. Tulisan ini menjelaskan isinya, cara menyusunnya, dan sama pentingnya, apa yang tidak bisa kami periksa.

![Tiga layar ponsel dari prototipe: peta laut dengan kartu stage, pertempuran dengan seretan yang sedang berlangsung, dan hasil kemenangan dengan tiga bintang. Teks di tangkapan layar berbahasa Korea.](/assets/posts/img/proto-shots.jpg)
*Peta laut dengan kartu stage, pertempuran dengan seretan yang sedang berlangsung, dan layar hasil.*

## Isinya

- **Enam belas stage:** laut 1, "Teluk Tenang" (Calm Bay), punya delapan, dan laut 2, "Selat Berangin" (Windy Strait), punya delapan. Laut berikutnya tampil sebagai kartu terkunci.
- **Alurnya:** peta, kartu stage, pertempuran, hasil dengan satu sampai tiga bintang, stage berikutnya.
- **Membuka kunci:** selesaikan satu stage dan yang berikutnya terbuka. Kalahkan bos dan laut berikutnya terbuka. Bintang tidak pernah menghalangi kemajuan; bintang adalah target tambahan.
- **Suara:** disintesis di browser, dengan tangga nada pentatonik berbeda untuk setiap laut dan nada yang naik pada setiap perebutan dalam satu rantai.
- **Kemajuan** disimpan di penyimpanan lokal browser, dan game tetap berjalan di memori jika penyimpanan diblokir.

## Cara membangunnya

- **Satu file.** Sekitar 95 KB, tanpa permintaan keluar dan tanpa font web, sehingga berjalan offline dan di dalam frame.
- **Mesin dan layar dipisah.** Mesinnya adalah modul murni tanpa DOM, tanpa jam, dan tanpa panggilan acak. Antarmuka hanya mengantrekan perintah seperti "kirim 50% dari pulau 0 ke pulau 1", dan sebuah loop menjalankan mesin setiap 100 ms.
- **Percepatan bekerja dengan menjalankan lebih cepat**, bukan mengubah aturan, sehingga batas waktu bintang tetap adil pada 2x.
- **Jeda** menghentikan tick, dan game menjeda diri sendiri saat tab disembunyikan.

Menjaga mesin tetap murni adalah taruhan untuk masa depan: kode yang sama nanti bisa berjalan bergiliran lewat jaringan, dan daftar perintah yang direkam bisa memutar ulang sebuah pertandingan.

## Yang kami uji

Kami menjalankan prototipe dengan Chrome headless. Pada layar 375 kali 812, prototipe mulai dari penyimpanan kosong, mengirim armada dengan seret mouse dan seret sentuh, menjeda (penghitung tick tetap membeku), memenangkan stage 1-1 dalam sekitar 12 detik dengan tiga bintang, menyimpan kemajuan, membuka 1-2, dan mempertahankan kemajuan setelah dimuat ulang. Pada 320 kali 568 tidak ada yang meluap ke samping. Konsol browser tidak menampilkan error.

Kami juga menjalankan pemeriksaan deterministik: peta dan perintah yang sama memberi hasil yang sama pada setiap kali jalan, dan menjalankan dalam waktu nyata maupun bergiliran memberi hasil akhir yang sama.

## Yang tidak bisa kami uji

- **Perangkat sungguhan.** iOS Safari dan ponsel Android kelas menengah **belum diperiksa**. Emulasi sentuh browser headless bukanlah jari.
- **Performa.** Target kami adalah 22 pulau dan 300 armada pada 60 frame per detik. Belum diukur.
- **Fitur yang belum ada:** mode bermain bebas, cara mengekspor log permainan, penyimpanan di tengah stage, dan beberapa animasi.
- **Kekurangan yang diketahui:** label seretan bisa menutupi angka pulau tetangga, dan kartu stage bisa menutupi simpul di peta.

Langkah berikutnya adalah uji 30 menit dengan lima sampai delapan orang, dengan log permainan dipasang terlebih dahulu. Tulisan berikutnya membahas pekerjaan penyeimbangan yang kami lakukan tanpa manusia.
