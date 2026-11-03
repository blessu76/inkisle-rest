---
title: Dua item Tinta sekaligus: slot, jeda, dan yang ditunjukkan bot kepada kami
description: Di lautan awal, kamu hanya bisa menjalankan satu item Tinta dalam satu waktu. Mulai laut 5 kamu bisa menjalankan dua, lalu tiga, dengan jeda di antara setiap awalan. Tabel aturan, cara tombol menampilkannya, dan simulasi yang menemukan efek jauh lebih kecil daripada dugaan kami.
slug: two-inks-at-once
lang: id
translation_of: en
category: making-of
keywords: Inkisle, item Tinta, desain game, keseimbangan game, simulasi bot, UI seluler, aksesibilitas
image_alt: Dua tetes tinta kecil berdampingan di atas deretan pulau, digambar dengan warna vektor yang lembut.
---
Item Tinta (lonjakan, jangkar, kabut, lentera, pembalik pasang) dulu berjalan satu per satu. Itu mudah dipahami, tetapi juga berarti tahap yang lebih lanjut tidak pernah terasa seperti memberi lebih banyak alat. Jadi kami memberi tombol Tinta **slot**.

## Aturannya

| Laut | Slot sekaligus | Jeda antar-awal |
|---|---|---|
| 1 sampai 4 | 1 | tidak ada (seperti sebelumnya) |
| 5 sampai 10 | 2 | 10 detik |
| Volume 2, laut 11 sampai 20 | 2 | 5 detik |
| Volume 3, mulai laut 21 | 3 | 5 detik |

Yang tetap sama: bos menambah 5 detik pada jeda, batas penggunaan per tahap (5 atau 6) dibagi oleh semua slot, kamu tidak bisa menjalankan dua item dengan jenis yang sama, slot jangkar atau kabut dibebaskan saat pulaunya direbut, dan 20 detik pertama setiap tahap tetap mengunci semua Tinta.

## Cara tombol menampilkannya

Tombol Tinta memiliki satu titik per slot, terisi selama slot berjalan. Cincin tipis di dalam tombol menghitung jeda sebelum kamu boleh memulai item berikutnya. Di lembar pelabuhan, kartu yang terblokir menulis "Tinta berikutnya dalam N detik" saat jeda, atau "menyebar" ketika slot penuh. Label aksesibilitas dibaca seperti "1 dari 2 slot". Semua ini tersedia dalam 12 bahasa.

## Mengapa mesin tidak membutuhkan hash baru

Status game sudah menyimpan daftar waktu berakhir untuk Tinta yang berjalan dan jumlah penggunaan, sehingga laut 1 sampai 4 berperilaku dan menghasilkan hash persis seperti sebelumnya. Pengujian mencakup setiap baris tabel, perilaku laut pertama, penolakan jenis yang sama, slot penuh, tiga slot, batas bersama, dan pembebasan saat perebutan, serta tombol pada 320 dan 375 px.

## Yang dikatakan bot

Kami mensimulasikan 80 tahap dari laut 5 sampai 14, lima bot, masing-masing 24 seed, untuk empat rencana dua atau tiga item yang dimulai pada detik ke-20, lalu membandingkan rencana terbaik di bawah aturan lama (satu slot, tanpa jeda) dengan aturan baru.

- Rata-rata peningkatannya **+1,1 poin persentase** (+0,9 di laut 5 sampai 10, +1,5 di laut 11 sampai 14). Kami menduga 3 sampai 8.
- Pada bos, peningkatannya +0,9. Tingkat kemenangan terbaik dengan Tinta dibandingkan tanpa Tinta adalah +36 poin, masih dalam batas kami yaitu 40.
- Tahap demi tahap, perubahannya bergerak antara −7 dan +10, yang kira-kira setara dengan derau dari 24 seed.

Bot jarang memakai slot kedua dengan baik, jadi angka kecil ini mungkin lebih banyak bercerita tentang bot daripada tentang aturannya. **[belum diverifikasi]** Seorang manusia mungkin mendapat peningkatan lebih besar.

## Yang belum kami periksa

- Apakah seseorang merasa dua slot dan jeda itu jelas, atau terasa seperti kunci. Kami belum mengujinya di ponsel sungguhan. **[belum diverifikasi]**
- Pemberitahuan satu baris saat pemain pertama kali mencapai laut dengan dua slot (5-1) belum dibuat.
- Game ini sedang dikembangkan dan belum dirilis.
