---
title: Aturan dalam satu halaman: pulau, pasukan, penaklukan
description: Seluruh aturan Inkisle dalam satu halaman: bagaimana pulau menghasilkan pasukan, bagaimana armada terbang, bagaimana penaklukan dihitung, dan bagaimana pertandingan berakhir. Nilai awal, sebelum pengujian.
slug: the-rules-on-one-page
lang: id
translation_of: en
category: making-of
keywords: Inkisle, aturan permainan, penaklukan pulau, mesin deterministik, desain game, aturan penaklukan
image_alt: Pulau-pulau dengan angka pasukan dan rute putus-putus tempat armada bergerak di antara pulau.
published: 2026-10-30T05:40+09:00
---
Game strategi yang bagus bisa dijelaskan dalam satu menit. Ini upaya kami menjelaskan aturan Inkisle dalam satu halaman. **Setiap angka di sini adalah nilai awal dari dokumen desain.** Kami memperkirakan sebagian akan berubah setelah pengujian.

## Pulau menghasilkan pasukan

Angka-angka di bawah ini berlaku untuk pulau biasa. Ada empat jenis pulau seluruhnya, dan nilai awal tiga lainnya adalah: **pulau kecil** menghasilkan 1 pasukan setiap 1,6 detik dengan batas 25; **pulau besar** 1 pasukan setiap 0,6 detik dengan batas 80; **benteng** 1 pasukan setiap 2 detik dengan batas 60 dan pengali pertahanan 1,5.

- Setiap pulau yang kamu miliki menambah **1 pasukan per detik** (satu "tick" adalah 100 ms, jadi satu pasukan setiap 10 tick).
- Ada **batas** 45. Melewati batas, pulau berhenti berproduksi, dan pasukan berlebih dari bala bantuan turun kembali ke batas dengan laju 1 per detik. Ini mencegahmu menumpuk semuanya di satu pulau lalu menunggu.
- **Pulau netral tidak berproduksi.** Angkanya tetap, sehingga terbaca seperti label harga.
- Kamu mulai dengan pulau markas berisi 20 pasukan. Musuh biasanya juga begitu, dan kalau tidak, kartu tahap akan menyebutkannya.

## Mengirim armada

Seret dari salah satu pulaumu ke pulau lain lalu lepaskan. Sebuah bilah di bawah memilih persentase: **25, 50, 75, atau 100%**. Kamu mengirim hasil pembulatan ke bawah dari jumlah pasukan dikali persentase, minimal 1. Pada 100% kamu mengirim "semua dikurangi satu", sehingga pulau tidak pernah kosong dan tetap milikmu.

Armada terbang lurus dengan kecepatan **2,5 unit peta per detik**. Pulau tetangga yang berjarak 4 sampai 8 unit memakan waktu sekitar 1,6 sampai 3,2 detik, dan melintasi seluruh peta memakan waktu sekitar 11 detik. Armada tidak bertempur di laut; mereka saling melewati. Itu menjaga pratinjau kedatangan tetap jujur, dan ketegangan khas genre ini tetap ada: perjalanan jauh adalah risiko, karena target terus bertambah selama kamu bepergian.

## Penaklukan, dihitung saat tiba

- Tiba di pulau sendiri menambah pasukan.
- Tiba di pulau musuh atau netral, kamu butuh lebih dari **pertahanan dikali pengali**. Pengalinya 1,0 secara normal dan **1,5 untuk benteng**.
- Menyerang di atas syarat: kamu menaklukkan, dan pertahanan baru adalah sisanya. Sama: bertahan dengan 0 (seri dimenangkan oleh pihak bertahan). Di bawahnya: pihak bertahan kehilangan sebagian.

Dua contoh. Armada 18 tiba di benteng berpertahanan 10. Syaratnya ceil(10 × 1,5) = 15, jadi kamu menaklukkannya dengan sisa 3. Armada 12 yang tiba di benteng yang sama meninggalkannya dengan 2.

Jika beberapa armada tiba pada tick yang sama, mereka diselesaikan satu per satu sesuai urutan keberangkatan.

## Bagaimana pertandingan berakhir

- **Menang:** musuh tidak punya pulau maupun armada.
- **Menang telak:** jika kamu memegang tiga kali total pasukan musuh dan minimal 60% pulau selama 5 detik, musuh menyerah. Ini mengakhiri pembersihan yang membosankan dalam pertandingan yang sudah dimenangkan.
- **Kalah:** kamu tidak punya pulau maupun armada, atau kehilangan pulau yang diminta untuk kamu lindungi.
- **Batas waktu:** pada menit ke-8 simulasi, pemain dengan pulau terbanyak menang. Ini hampir tidak pernah terjadi.

## Satu mesin untuk waktu nyata dan giliran

Keadaan game hanya bergantung pada peta awal, sebuah seed, dan daftar perintah, tanpa jam dan tanpa keacakan di dalam mesin. Masukan yang sama menghasilkan hasil yang sama di setiap perangkat. Itulah yang memungkinkan mesin yang sama berjalan secara waktu nyata sekarang dan dalam giliran berjaringan nanti, dan membuat replay serta laporan bug cukup dengan menyimpan daftar perintah.
