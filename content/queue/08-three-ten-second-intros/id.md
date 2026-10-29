---
title: Intro sepuluh detik dalam tiga versi: langit, laut, dan daratan
description: Inkisle dibuka dengan intro sepuluh detik yang punya tiga versi. Bagaimana ketiganya berbagi satu akhir yang sama, mengapa kantong yang diacak menentukan versi mana yang kamu lihat, kapan intro memendek jadi tiga detik, dan apa yang terjadi saat reduce-motion aktif.
slug: three-ten-second-intros
lang: id
translation_of: en
category: making-of
keywords: Inkisle, intro game, peluncuran aplikasi, tombol lewati, kurangi gerakan, aksesibilitas, game seluler
image_alt: Pulau-pulau di laut hijau mint dengan tinta berwarna koral menyebar di salah satunya, gambar pembuka intro Inkisle.
---
Hal pertama yang kamu lihat saat membuka Inkisle adalah sebuah intro. Kami ingin intro terasa seperti peristiwa kecil beberapa kali pertama, lalu **tidak menghalangi** setelah itu. Tulisan ini menjelaskan cara intro dibuat dan aturan yang menentukan apa yang kamu lihat.

## Satu akhir, tiga awal

Intro lengkap berdurasi **10 detik**. 7 detik pertama hadir dalam tiga versi: **langit**, **laut**, dan **daratan**. 3 detik terakhir sama di semuanya: akhir yang mengarah ke menu. Dengan akhir yang dipakai bersama, kami cukup menggambarnya sekali, dan setiap versi sampai ke tempat yang sama.

## Kamu dapat yang mana?

Memilih secara acak bisa menampilkan intro yang sama tiga kali berturut-turut, dan itu terasa seperti bug. Karena itu aplikasi memakai **kantong yang diacak**: ketiga versi dimasukkan ke dalam kantong dengan urutan acak, lalu satu diambil setiap kali aplikasi dibuka. Saat kantong kosong, kantong diisi ulang. Dua akibatnya:

- Dalam satu putaran, **tiga kali buka berturut-turut menampilkan ketiga versi**.
- Versi pertama pada putaran baru tidak pernah sama dengan versi terakhir yang kamu lihat.

Kantong disimpan di ponsel, jadi tetap berfungsi di antara peluncuran.

## Panjang dulu, pendek kemudian

Pada **tiga peluncuran pertama** kamu mendapat 10 detik penuh. Mulai peluncuran keempat, aplikasi hanya memutar akhir yang dipakai bersama, yaitu **3 detik**. Tombol lewati muncul **0,6 detik** setelah intro dimulai, agar penonton pertama kali tidak diminta melewati sebelum melihat apa pun. Melewati memanggil langkah "selesai" yang sama seperti saat intro berakhir, dan sebuah tes memeriksa bahwa langkah itu hanya berjalan sekali.

## Reduce motion

Jika pengaturan reduce-motion di ponsel aktif (iOS "Reduce Motion", atau animasi dimatikan di Android), intro **tidak bergerak**. Intro menampilkan bingkai akhir yang sudah jadi selama **1,2 detik** lalu masuk ke menu. Tombol lewati sudah ada sejak awal.

## Saat kantong yang tersimpan rusak

Tinjauan kode kami menemukan bahwa kantong tersimpan yang rusak tidak pernah diperbaiki: aplikasi gagal membacanya, mulai dari awal di setiap peluncuran, dan terus menampilkan versi penuh 10 detik. Perbaikannya adalah memperlakukan data yang tidak terbaca sebagai "tidak ada data" dan langsung menulis yang baru. Jika penyimpanan sama sekali tidak tersedia, aplikasi memilih versi secara acak dan memutar intro penuh, dan tidak pernah menghalangi game untuk mulai. Ada tes untuk kasus-kasus ini.

## Yang belum kami periksa

- Kami belum mengukur bagaimana intro berjalan di **ponsel sungguhan**. Tes mencakup aturan di atas, bukan kelancaran animasinya.
- Apakah sepuluh detik adalah durasi yang tepat untuk peluncuran pertama hanyalah tebakan sampai orang lain melihatnya.
