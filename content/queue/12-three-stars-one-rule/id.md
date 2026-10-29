---
title: Tiga bintang, satu aturan: bagaimana sebuah stage dinilai
description: Setiap stage di Inkisle bisa mendapat hingga tiga bintang. Arti tiap bintang, mengapa bintang tidak pernah menghalangi kemajuan atau turun, 13 jenis target tiga bintang, dan label keliru yang kami temukan dan perbaiki.
slug: three-stars-one-rule
lang: id
translation_of: en
category: making-of
keywords: Inkisle, penilaian bintang, progres game, desain game, game mobile, daya main ulang
image_alt: Deretan tiga bintang, dua yang pertama terisi warna koral dan yang ketiga hanya garis tepi.
---
Masing-masing dari 16 stage Inkisle memberi satu sampai tiga bintang. Bintang adalah cara game berkata "Anda bisa lebih baik" tanpa memaksa Anda. Berikut aturannya, dan satu kesalahan yang kami buat dalam menjelaskannya.

## Arti tiap bintang

1. **★1: menang.** Anda mengalahkan stage.
2. **★2: menang dalam batas waktu stage.** Setiap stage punya batasnya sendiri.
3. **★3: target khas stage.** Target yang berbeda untuk tiap stage, ditampilkan di kartunya.

Game menentukan ketiga syarat ini di satu tempat, dan layar hanya menanyakan hasilnya. Kedengarannya jelas, tetapi saat pertama kali kami menulis bagan dan lembar hasil, potongan aturan sudah bocor ke keduanya. Sebuah tinjauan menemukannya, dan kami memindahkan pemeriksaan ke fungsi bantu kecil di samping aturan, sehingga jika aturan berubah hanya ada satu tempat yang perlu diubah.

## Bintang tidak pernah menghalangi

- **Bintang tidak membuka apa pun.** Memenangkan sebuah stage membuka yang berikutnya. Mengalahkan bos membuka laut berikutnya.
- **Bintang tidak pernah turun.** Main ulang sebuah stage lalu kalah, tidak ada yang dicatat. Main ulang lalu menang, game menyimpan yang terbaik dari semuanya: bintang yang sudah diperoleh tetap ada, dan waktu terbaik disimpan.

Jadi main ulang hanya bisa membantu Anda.

## Tiga belas jenis target tiga bintang

Target ★3 berbeda di hampir setiap stage. Sejauh ini ada 13 jenis, misalnya:

- kehilangan paling banyak sejumlah pasukan,
- menang tanpa pernah mengirim 100%,
- merebut setiap pulau kosong,
- tidak kehilangan satu pulau pun,
- merebut benteng dalam satu serangan,
- menahan serangan musuh yang serentak satu kali,
- tidak menyerang pulau markas musuh sebelum waktu tertentu.

Setiap target ditulis dengan kata-kata sederhana di aplikasi, misalnya "Menang tanpa mengirim 100%."

## Label yang keliru

Label ★1 pada awalnya berbunyi "**menang sambil mempertahankan pulau Anda**". Padahal syaratnya hanya "menang": Anda bisa kehilangan pulau dan tetap mendapat bintang. Label itu menjanjikan sesuatu yang tidak diperiksa game. Sebuah tinjauan menangkapnya, dan kini labelnya sekadar "**menang**".

## Yang belum kami periksa

- Batas waktu untuk ★2 ditetapkan oleh prototipe dan, seperti ditunjukkan tes bot di tulisan sebelumnya, tampak **terlalu longgar** untuk bot. Kami belum tahu seperti apa waktu manusia.
- Kami tidak tahu apakah pemain akan merasa 13 target yang berbeda itu menarik atau hanya membingungkan.
