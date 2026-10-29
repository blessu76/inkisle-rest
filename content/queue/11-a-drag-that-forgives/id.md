---
title: Seretan yang memaafkan: aturan-aturan kecil di balik satu gestur
description: Mengirim armada di Inkisle cukup dengan satu seretan. Aturan-aturan kecil yang membuatnya bekerja dengan jari sungguhan: area pilih yang lebih lebar, seretan yang mengambil sampel di seluruh jalurnya, satu jari dalam satu waktu, dan pesan yang jelas ketika pengiriman tidak bisa dilakukan.
slug: a-drag-that-forgives
lang: id
translation_of: en
category: making-of
keywords: Inkisle, kontrol sentuh, UX game mobile, seret dan lepas, multisentuh, desain game
image_alt: Sebuah ibu jari menyeret dari pulau koral melintasi laut ke pulau tetangga, dengan garis putus-putus di belakangnya.
---
Stage pertama mengajarkan seluruh kontrol dalam satu baris: **seret sebuah pulau ke pulau lain dan sebuah kapal berangkat**. Kalimat itu menyembunyikan banyak keputusan kecil, karena ibu jari jauh lebih tumpul daripada mouse. Tulisan ini mengumpulkan keputusan yang paling kami yakini.

## Jari lebih besar daripada pulau

Sebuah pulau di layar bisa lebih kecil daripada ujung jari, dan jari menutupinya saat Anda membidik. Karena itu, ketika Anda melewati pulau-pulau saat menyeret, area yang dihitung sebagai "di atas pulau ini" adalah **radius pulau ditambah 12 piksel**. Tanpa margin tambahan itu, seretan yang tampak jelas berakhir di sebuah pulau sering meleset.

## Gesekan cepat tidak bisa melewatkan pulau

Saat Anda menggesek melintasi beberapa pulau untuk memilihnya, layar hanya melaporkan posisi jari Anda sesekali. Gesekan cepat bisa melompat dari satu sisi pulau ke sisi lainnya tanpa pernah dilaporkan berada di dalamnya. Karena itu game **mengambil sampel sepanjang garis** di antara dua laporan, sehingga setiap pulau yang dilintasi jari dihitung.

## Satu jari dalam satu waktu

Tinjauan kode pertama kami menemukan kasus yang belum terpikirkan: jika **jari kedua** menyentuh layar di tengah seretan, sentuhan kedua menggantikan yang pertama, dan gerakan kedua jari bercampur. Itu bisa membuat pilihan berada dalam keadaan aneh atau mengirim armada yang tidak dimaksudkan siapa pun. Perbaikannya sederhana: game mengikuti **hanya jari pertama** dan mengabaikan yang lain sampai jari itu terangkat. Sebuah tes mencakup kasus jari kedua yang diabaikan.

## Beri tahu mengapa tidak ada yang terjadi

Jika Anda mencoba mengirim dari pulau yang pasukannya terlalu sedikit, pengiriman tidak terjadi. Diam terasa seperti bug, jadi game menampilkan pesan singkat: sebuah pulau membutuhkan **setidaknya 2 pasukan** untuk mengirim. Menekan dan menahan sebuah pulau selama **0,4 detik** memilih semua pulau Anda, dan sebuah pesan menyuruh Anda mengetuk atau menyeret ke target untuk serangan habis-habisan.

## Jumlah yang dikirim

Berapa banyak yang keluar dari sebuah pulau ditentukan oleh bilah rasio. Bawaannya **50%**. Stage 1-2 mengajarkan memilih rasio, dan target tiga bintangnya adalah menang **tanpa pernah mengirim 100%**, yang mendorong Anda mencoba pengaturan lain.

## Yang belum kami periksa

- Semua yang ada di sini diperiksa dengan sentuhan simulasi dalam tes. Kami **belum melihat orang sungguhan** memakainya di ponsel sungguhan, dan gestur yang tampak baik dalam tes tetap bisa terasa salah.
- Ukuran-ukuran itu (12 px, 0,4 d) adalah tebakan awal. Ukuran itu akan berubah jika pemain meleset dari pulau atau tidak sengaja memilih semuanya.
