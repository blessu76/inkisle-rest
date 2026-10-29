---
title: Mengirim dari beberapa pulau sekaligus: tiga kali menulis ulang satu kontrol
description: Menyerang satu pulau dari beberapa pulau milik Anda adalah kontrol tersulit di Inkisle. Versi pertama berbasis seret, perbaikan ketuk-untuk-memilih, dan versi geser-untuk-memilih, serta apa yang diajarkan masing-masing.
slug: three-rewrites-of-multi-island-attack
lang: id
translation_of: en
category: making-of
keywords: Inkisle, kontrol sentuh, UX game mobile, multi-pilih, seret dan lepas, desain game, iterasi
image_alt: Pertempuran ketika beberapa pulau mengirim armada ke satu pulau musuh.
---
Mengirim satu armada itu mudah: seret dari pulau Anda ke target. Bagian tersulit dari kontrol Inkisle adalah **mengirim dari beberapa pulau sekaligus**, karena level-level akhir dimenangkan dengan tiba bersama. Kami menulis ulang kontrol itu tiga kali dalam beberapa jam, dan ceritanya menunjukkan alasannya.

## v0.1: semuanya sekaligus

Prototipe pertama mendukung beberapa cara:

- Seret dari sebuah pulau ke target, dan **lewati pulau Anda yang lain di sepanjang jalan** untuk menambahkannya sebagai sumber.
- **Tekan lama** (0,4 detik) sebuah pulau untuk memilih semua pulau Anda, lalu seret untuk serangan habis-habisan.
- Ketuk sebuah sumber, lalu ketuk target, sebagai alternatif untuk menyeret.

Di atas kertas, ini mencakup segalanya. Dalam praktiknya, jempol menutupi tepat pulau yang sedang dilewatinya, dan level yang mengajarkan "lewati pulau sambil menyeret" meminta gerakan yang sulit dilihat dan sulit dibidik.

## v0.1.1: pilih dulu, lalu berangkat

Perbaikannya adalah membagi gerakan menjadi dua. **Ketuk pulau Anda satu per satu untuk memilihnya**, lalu ketuk target dan semuanya berangkat. Menyeret pulau yang terpilih tetap mengirim seluruh kelompok. Kami menambahkan:

- lencana kecil di atas pilihan yang menunjukkan berapa pulau yang dipilih,
- ketukan di laut kosong untuk menghapus pilihan,
- area pilih yang lebih lebar saat bergabung sambil menyeret (radius pulau ditambah 12 px), karena jari lebih besar daripada pulau,
- petunjuk yang ditampilkan beberapa kali pertama, dan kartu level yang mengajarkan kontrol ini sekarang menjelaskan cara mengetuk.

Mengetuk itu presisi dan tenang, tetapi dengan banyak pulau berarti **banyak ketukan** sebelum setiap serangan. Dalam game real-time, itu adalah waktu.

## v0.1.2: geser untuk memilih

Versi terbaru memungkinkan Anda **menggeser jari melintasi pulau-pulau Anda untuk memilihnya dalam satu goresan**, lalu memilih target. Memilih empat pulau kini satu gerakan, bukan empat ketukan. Apakah cara-cara sebelumnya tetap dipertahankan sebagai cadangan, dan bagaimana rasa gesernya secara rinci, belum final **[belum terverifikasi saat penulisan]**.

## Yang kami pelajari, dan yang tidak kami ketahui

- **Gerakan yang mengharuskan jari mendarat pada target kecil sambil bergerak itu rapuh di ponsel.** Perbaikan pertama menghilangkan pembidikan; yang kedua menghilangkan pengulangan.
- Setiap versi memperbaiki satu masalah dan memperlihatkan masalah berikutnya, yang wajar, tetapi juga berarti kontrol ini belum mapan.
- Kami **tidak punya data dari pemain luar** untuk ketiga versi mana pun. Rasa persis v0.1.2 **[belum terverifikasi]** sampai orang lain mencobanya.

Pengujian dengan lima sampai delapan orang adalah tempat kontrol ini benar-benar akan dinilai. Jika mereka masih ragu sebelum menyerang, kami akan mengubahnya untuk keempat kalinya.
