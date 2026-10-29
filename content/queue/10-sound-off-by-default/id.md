---
title: Suara mati secara default: satu tangga nada untuk tiap laut
description: Inkisle dimulai dalam keadaan senyap dan pemain yang menyalakan suara. Bagaimana suara dibuat lewat kode tanpa file audio, bagaimana setiap laut mendapat tangga nada lima nadanya sendiri, dan mengapa rantai perebutan naik di tangga nada.
slug: sound-off-by-default
lang: id
translation_of: en
category: making-of
keywords: Inkisle, audio game, suara prosedural, tangga nada pentatonik, game seluler, aksesibilitas, pengaturan
image_alt: Lima nada naik yang digambar sebagai titik-titik tinta kecil di atas deretan pulau.
---
Banyak orang bermain di ponsel di tempat umum atau di tempat tidur. Game yang dimulai dengan keras adalah game yang ditutup. Jadi di Inkisle **suara mati sampai pemain menyalakannya**, dan pengaturan itu disimpan.

## Mati berarti benar-benar mati

Saat suara mati, kode audio bahkan tidak dijalankan: pemutar suara dibuat pertama kali saat suara benar-benar dibutuhkan. Game yang dibisukan tidak pernah menyentuh sistem audio ponsel. Jika pengaturan tersimpan rusak atau penyimpanan gagal, jawabannya kembali "mati". Aplikasi juga menghormati sakelar senyap di ponsel. Kesalahan di dalam kode audio ditangkap, bukan dibiarkan bocor keluar, yang merupakan perbaikan setelah tinjauan kode menemukan bahwa satu jenis kesalahan audio bisa lolos dari jaring pengaman.

## Tanpa file suara

Setiap suara **dibuat lewat kode**. Aplikasi membangun WAV mono 16-bit yang singkat dengan 22.050 sampel per detik untuk setiap nada: sebuah gelombang (sinus, segitiga, atau gigi gergaji), attack 12 ms, dan peluruhan eksponensial. Tidak ada file rekaman yang perlu dilisensikan. Parameter nada berasal dari prototipe web, jadi aplikasi terdengar seperti prototipenya.

## Satu tangga nada untuk tiap laut

Setiap laut punya **tangga nada pentatonik**-nya sendiri, lima nada yang enak didengar dalam urutan apa pun:

| Laut | Langkah di atas nada dasar (semiton) |
|---|---|
| Teluk Tenang (Calm Bay) | 0, 2, 4, 7, 9 |
| Selat Berangin (Windy Strait) | 0, 2, 5, 7, 9 |

Nada dasarnya 523,25 Hz. Laut kedua berbeda pada satu nada, langkah ketiga (5, bukan 4).

## Rantai naik

Saat kamu merebut beberapa pulau berturut-turut, **setiap perebutan satu langkah lebih tinggi** di tangga nada laut itu. Setelah lima langkah, tangga nada naik satu oktaf, dan di atas langkah kesepuluh nadanya bertahan di nada tertinggi. Rantai yang bagus pun terdengar sebagai garis yang naik, dan karena tangga nada hanya berisi nada-nada yang serasi, rantai yang cepat tetap selaras.

## Yang belum kami periksa

- Tes memeriksa nada-nadanya dan bahwa bisu berarti senyap. Tes tidak bisa memberi tahu kami apakah suaranya **enak didengar**. Belum ada orang di luar tim yang mendengarkannya lewat speaker ponsel sungguhan atau headphone.
- Nada-nada ini hanyalah bip sederhana. Apakah akan tetap menjadi suara final atau diganti belum diputuskan.
