---
title: Menyetel kesulitan dengan bot: lima level yang salah
description: Kami memainkan setiap level dengan bot sederhana pada 40 seed per level, dan menemukan level yang mustahil, terlalu singkat, atau terlalu sulit. Lima perubahan, tingkat kemenangan sebelum dan sesudahnya, serta alasan bot bukan manusia.
slug: tuning-the-difficulty
lang: id
translation_of: en
category: making-of
keywords: Inkisle, keseimbangan game, penyetelan kesulitan, simulasi bot, tingkat kemenangan, desain level
image_alt: Pertempuran ramai antara beberapa pihak berwarna di prototipe Inkisle.
---
Kami belum punya pemain uji, jadi kami mengajukan pertanyaan lain: level mana yang *jelas* salah? Dua bot sederhana memainkan setiap level masing-masing 40 kali, dengan 40 seed berbeda, lalu kami membaca tingkat kemenangannya.

## Dua bot

- **Bot sederhana:** setiap 10 tick, ia menyerang pulau termurah yang bisa dikalahkannya. Ia mewakili pemain kasual.
- **Bot mahir:** setiap 5 tick, ia mengumpulkan hingga tiga pulau dan menyerang bersama.

Keduanya bukan manusia. Mereka memberi tahu arah, bukan kesulitan seperti yang dirasakan manusia.

## Lima level yang salah

| Level | Masalah | Perubahan | Bot sederhana sebelum → sesudah |
|---|---|---|---|
| 1-1 | Target tiga bintang "kehilangan paling banyak 5" mustahil: pulau netral saja sudah menelan 13 | Target diubah menjadi "paling banyak 14" | Tiga bintang tercapai 0% → 100% |
| 1-5 | Selesai dalam 18 detik | Markas musuh 20 → 26, satu pulau netral diberikan ke musuh | 100%, kini 30 dtk |
| 1-8 bos | Praktis tidak bisa dikalahkan | Pulau kedua musuh diperkecil, pulau bendera 24 → 26, satu pulau kecil diberikan ke pemain | **0% → 53%** |
| 2-2 | Selesai dalam 23 detik | Markas pemain 15 → 20, satu pulau diberikan ke musuh | 100%, kini 38 dtk |
| 2-8 bos | Terlalu sulit | Pulau bendera 24 → 28, satu benteng musuh dijadikan benteng netral berkekuatan 14 | **10% → 38%** |

Kami membiarkan 11 level lainnya apa adanya. Targetnya adalah level bos yang dikalahkan pemain kasual setelah sekitar satu kali mengulang, yaitu 40 sampai 60% untuk bot sederhana.

## Efek samping yang kami temukan

- Pada satu set 20 seed, tingkat kemenangan keseluruhan bot sederhana naik dari 84% menjadi 91% dan bot mahir dari 78% menjadi 82%.
- Level 2-2 menjadi *lebih sulit* bagi bot mahir, turun dari 100% ke 65%. Kami menduga bot punya kebiasaan mengosongkan benteng, tetapi itu **[belum terverifikasi]**.
- Level 2-4 dan 2-7 menunjukkan tingkat kemenangan rendah untuk bot mahir, 40% dan 38%. Dalam pertempuran yang padat, mengumpulkan pasukan mungkin merugikan. Ini juga **[belum terverifikasi]**.
- Batas waktu dua bintang tampak terlalu longgar, karena bot hampir selalu memenuhinya. Kami akan memperketatnya setelah melihat waktu manusia.

![Tiga layar ponsel dari pertempuran yang ramai di prototipe. Teks pada tangkapan layar berbahasa Korea.](/assets/posts/img/tuning-boss.jpg)
*Level yang ramai di prototipe: pertempuran campur aduk di tengah laut, level bos dengan pulau bendera yang dikepung, dan layar selebar 320 px.*

## Mengapa bot bukan manusia

Bot tidak pernah salah membaca angka, tidak pernah bosan, dan tidak pernah salah seret. 30 menit pertama seseorang adalah ujian sesungguhnya: di mana ia mengulang, di mana ia berhenti, berapa lama ia sampai ke "berikutnya". Rencananya, kami menambahkan log permainan lebih dulu, lalu mengamati lima sampai delapan orang. Sampai saat itu, angka-angka ini hanya mengatakan bahwa tidak ada level yang jelas rusak, dan itu klaim yang lebih lemah daripada "kesulitannya sudah tepat".
