---
title: Peta laut yang mengubah jalurnya: satu gaya garis per laut
description: Dengan 14 laut pada satu peta yang bisa digulir, jalan antar stage tampak sama di mana-mana. Kami memberi setiap laut gaya garis, warna, dan liukan sendiri, membuat sudutnya berlanjut melewati batas laut, dan hanya menggambar apa yang ada di layar. Nilai-nilainya, tesnya, dan apa yang belum kami lihat di ponsel.
slug: a-chart-that-changes-its-road
lang: id
translation_of: en
category: making-of
keywords: Inkisle, peta laut, peta level, gaya rute, UI seluler, Flutter, performa rendering
image_alt: Jalan titik-titik yang berkelok di antara pulau-pulau, berubah dari garis tali menjadi garis gelombang, digambar dengan warna vektor yang lembut.
published: 2026-11-12T19:00+09:00
---
Peta adalah layar tempat kamu menghabiskan waktu tenang di antara pertempuran: jalan panjang berisi stage. Dengan 14 laut, jalannya tampak sama dari awal sampai akhir. Gulir panjang tanpa perubahan terasa seperti satu laut yang berulang. Maka setiap laut mendapat jalannya sendiri.

## Apa yang berubah per laut

| Laut | Garis | Warna jalan yang sudah diselesaikan |
|---|---|---|
| 1 | solid (seperti sebelumnya) | koral |
| 2 | tali | krem layar |
| 3 | garis putus panjang, samar | putih mercusuar |
| 4 | gelombang | hijau tosca |
| 5 | manik | merah muda koral |
| 6 | garis putus panjang | emas pasir |
| 7 | solid tebal | biru tua |
| 8 | solid tipis | kobalt |
| 9 | manik | emas lentera |
| 10 | solid tebal | emas |
| 11 | kuas | tinta |
| 12 | garis ganda | perak |
| 13 | gelombang | layar putih |
| 14 | manik | tinta pekat |

Setiap laut juga punya ayunannya sendiri (seberapa jauh jalan berayun ke samping dan seberapa sering). Tujuh jenis garis dipakai bersama oleh 14 laut, dan semua warnanya berbeda. Jalan menuju sebuah stage digambar dengan gaya laut tempat stage itu berada. Setelah laut 14, gayanya berulang, sebagai pengganti sementara.

## Dua hal yang bukan soal tampilan

- **Tidak ada lompatan di batas laut.** Ayunannya satu fungsi yang berkesinambungan, sehingga sudutnya berlanjut di tempat satu laut berakhir dan laut berikutnya dimulai, dan pulau-pulau tidak melompat ke samping.
- **Gambar hanya yang terlihat.** Peta akan memiliki ratusan stage, jadi pulau dan jalan di luar area yang terlihat dilewati. Dalam tes widget, menggambar sepuluh jalan yang terlihat memakan waktu kurang dari 16 ms.

## Hiasan menyusul

Langkah kedua menambahkan tanda-tanda kecil di sepanjang jalan untuk setiap laut: simpul, kurung, jejak kaki, bintang, tetes tinta. Setelah itu, di laut 7, 10, dan 11 kami mengubahnya menjadi pusaran, suar, dan sebaran, dan tetes di laut 14 menjadi tetes yang runcing.

## Tes

Tujuh tes memeriksa bahwa setiap laut punya gaya, bahwa ayunan tetap di bawah .32, bahwa 14 warna semuanya berbeda, bahwa setiap jenis garis dipakai, bahwa jalan yang sudah diselesaikan memiliki kontras minimal 3:1 terhadap tepinya, bahwa pulau tetap berada dalam 18% hingga 82% lebar pada 320 px, dan bahwa setiap laut menggambar piksel yang berbeda. Tata letak laut pertama tidak bergeser.

## Yang belum kami periksa

- Semua render sejauh ini adalah tangkapan tes, di mana fontnya berupa kotak. Kami belum melihatnya di iPhone atau ponsel Android sungguhan. **[belum diverifikasi]**
- Kami tidak mengukur waktu frame dengan seluruh 800 stage, hanya pemeriksaan sepuluh jalan. **[belum diverifikasi]**
- Di laut malam yang gelap (11 dan 14), jalan berwarna tinta ditopang oleh tepi putih. Apakah tampilannya sudah benar adalah pemeriksaan desain yang masih menjadi utang kami.
- Game ini sedang dalam pengembangan dan belum dirilis.
