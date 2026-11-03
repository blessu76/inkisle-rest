---
title: Mata air tinta di laut putih: ketika aturan tiga bintang tidak bisa diraih
description: Laut 14 punya mata air yang menyebarkan tinta ke pulau-pulau di dekatnya. Bot tidak bisa meraih target tiga bintang "buat mata air menyebar ke N pulau", jadi kami mengukur, mencoba memindahkan pulau, lalu mengganti aturannya dengan hitungan denyut mata air. Apa yang kami coba dan apa yang masih belum diperiksa.
slug: the-white-sea-ink-spring
lang: id
translation_of: en
category: making-of
keywords: Inkisle, desain level, aturan tiga bintang, mata air tinta, simulasi bot, keseimbangan game, laut 14
image_alt: Laut pucat dengan sebuah pulau mata air kecil di tengah dan beberapa pulau di sekitarnya, digambar dengan warna vektor yang lembut.
---
Laut 14, laut putih, menambahkan satu aturan: **mata air tinta**. Kuasai pulau mata air, dan setiap 150 tick ia berdenyut lalu menyebarkan tinta ke pulau di dekatnya. Denyut pertama datang 150 tick setelah kamu merebutnya. Target tiga bintang yang pertama kami tulis untuknya adalah "buat mata air menyebar ke N pulau". Target itu ternyata janji yang tidak bisa ditepati siapa pun.

## Pengukuran

Target ini dipakai di tujuh stage. Di enam di antaranya, kami membuat skrip permainan terbaik yang bisa kami pikirkan: rebut mata air pada tick 0, lalu biarkan selama 900 tick, dengan empat seed masing-masing. (14-8 tidak bisa diskripkan seperti ini, karena musuh menguasai mata air sejak awal.)

| Stage | Penyebaran yang dibutuhkan | Penyebaran yang kami dapat |
|---|---|---|
| 14-1 | 2 | 0 |
| 14-2 | 2 | 0 |
| 14-3 | 3 | 0 |
| 14-5 | 2 | 0 |
| 14-6 | 2 | 0 |
| 14-7 | 3 | 0 |

Musuh merebut pulau-pulau kecil di samping mata air antara tick 70 dan tick 250. Denyut pertama datang pada tick 150 atau lebih, jadi sering kali tidak ada lagi tempat untuk menyebar.

## Tiga hal yang kami coba

1. **Memindahkan pulau.** Pencarian atas pulau-pulau kecil di samping mata air menemukan tata letak yang mencapai jumlah yang dibutuhkan di 14-1 dan 14-5, tetapi hanya dengan menaruh empat atau lima pulau kecil di samping mata air. Itu melanggar batas tiga yang kami tetapkan sendiri, dan 14-5 lalu gagal memenuhi batas bawah "bot paling sederhana harus menang setidaknya beberapa kali". Di dalam batas itu, tidak ada tata letak yang memberi lebih dari satu penyebaran.
2. **Memajukan denyut pertama.** Dengan denyut pertama pada 60 tick, 14-1 menjadi mungkin dan lima stage lainnya tetap di 0 atau 1. Ini juga menekan 14-8 di bawah batas bawah kami untuk bot paling sederhana. Kami tidak mempertahankannya.
3. **Mengubah aturan.** Target seharusnya menghargai hal yang dikendalikan pemain: menguasai mata air. Jadi target tiga bintang menjadi **jumlah denyut mata air milikmu sendiri**. Angkanya dipilih setara atau di bawah yang benar-benar dicapai bot dalam permainan yang dimenangkan: 14-1: 4, 14-2: 3, 14-3: 2, 14-5: 3, 14-6: 1, 14-7: 3, 14-8: 1. Stage 14-4 tetap memakai targetnya sendiri.

Kami memilih yang ketiga. Ini hanya menyentuh laut 14, sehingga hash dan file golden laut 1 sampai 13 tidak berubah.

## Penyisiran terakhir di laut ini

Sekalian, kami melebarkan bagian tengah 14-1 (satu pulau pusat dari 4 menjadi 12) dan melunakkan 14-6, tempat satu bot menang jauh lebih banyak daripada yang lain. Kini ada tes baru yang menyatakan bahwa tidak ada satu bot pun yang boleh mengambil lebih dari setengah kemenangan di 14-8; hari ini hasilnya 8, 17, 12, dan 24 kemenangan untuk empat bot dan 0 untuk bot kelima.

## Yang belum kami periksa

- Di 14-6 dan 14-8 musuh menguasai mata air, jadi satu denyut adalah paling banyak yang bisa diandalkan. Bot jarang mencapainya, sehingga angka-angkanya bertumpu pada data yang tipis. **[belum diverifikasi]**
- Belum ada yang memainkan stage-stage ini dengan tangan. Apakah "buat mata air berdenyut" terasa jelas pada kartu stage dan layar hasil, perlu dicek di ponsel sungguhan. **[belum diverifikasi]**
- Game ini sedang dalam pengembangan dan belum dirilis.
