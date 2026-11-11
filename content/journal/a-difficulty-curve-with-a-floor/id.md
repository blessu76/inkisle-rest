---
title: Kurva kesulitan dengan batas bawah: tidak ada stage yang tak pernah bisa dimenangkan bot paling sederhana
description: Dengan ratusan stage, beberapa stage sulit bukan sekadar beberapa stage sulit, melainkan tembok. Kami menyetel ulang semua 14 laut ke kurva dengan satu stage istirahat di setiap laut, membatasi seberapa kuat AI musuh, dan menambahkan tes yang gagal jika bot paling sederhana menang 0 dari 40. Sebelum dan sesudahnya.
slug: a-difficulty-curve-with-a-floor
lang: id
translation_of: en
category: making-of
keywords: Inkisle, kurva kesulitan, keseimbangan game, simulasi bot, desain level, tingkat kemenangan, level AI
image_alt: Barisan pulau yang berkelok, naik dan turun seperti gelombang, digambar dengan warna vektor yang lembut.
published: 2026-11-11T19:00+09:00
---
Satu komentar dari pemilik mengubah pekerjaan ini: jika hanya 40 dari 800 stage yang bisa dimenangkan, game-nya terlalu sulit, meskipun setiap stage tampak baik jika dilihat sendiri-sendiri. Jadi kami berhenti menyetel stage satu per satu dan menuliskan sebuah **kurva**.

## Kurvanya

- Setiap laut punya delapan stage dengan satu **peran**: pembuka, penguatan, stage istirahat, tanjakan, bos. Stage istirahat dimaksudkan mudah, dengan bot paling sederhana menang setidaknya 80% dari waktu.
- Target tingkat kemenangan juga mengikuti **gelombang lintas volume**: satu laut sedikit lebih sulit daripada yang sebelumnya, lalu ada lagi laut yang lebih landai.
- Laut 1 sampai 3 sudah ada di build TestFlight, jadi kami membiarkan nilai mudahnya apa adanya.

## Batas untuk musuh

Beberapa stage sulit karena AI musuhnya terlalu pintar, bukan karena petanya berat. Kami menambahkan **batas atas AI**: level 5 hanya untuk stage dengan beberapa musuh, level 4 untuk laut 11 ke atas, untuk bos, dan untuk stage ketujuh mulai laut 6, level 3 di tempat lain. AI apa pun di atas batasnya diturunkan saat stage dimuat. Satu contoh: di 10-8, sang laksamana turun dari level 5 ke 3, dan pertahanan mercusuar netral dari 10 ke 5.

## Pengukuran

Semua 14 laut, lima bot, masing-masing 40 seed. "Bot sederhana" adalah yang terlemah dari kelima bot dan mewakili seorang manusia.

| | Sebelum | Sesudah |
|---|---|---|
| Stage yang tak pernah dimenangkan bot sederhana | **9** (3-8, 4-3, 4-6, 5-5, 6-8, 7-6, 10-3, 10-8, 14-2) | **0** |
| Stage terlemah | 0 kemenangan dari 40 | 4 kemenangan dari 40 (8-8), lalu 5 dari 40 (10-8) |
| Stage istirahat, bot sederhana | tidak dilacak | setidaknya 80% |

Beberapa contoh kemenangan bot sederhana dari 40: 3-8: 0 → 30. 4-3: 0 → 18. 6-1: 2 → 39. 7-6: 0 → 17.

## Tes yang menjaga batas bawah

`curve_floor_test` gagal jika bot sederhana menang 0 dari 40 di mana pun, jika stage istirahat turun di bawah 80%, atau jika rata-rata kelima bot menyimpang terlalu jauh dari target kurva. Target-targetnya berada di satu file, jadi mengubah kurva berarti mengubah satu tabel.

## Apa yang sengaja dibuat lebih mudah, dan harganya

Membuat stage lebih mudah membuat item **Tinta** lebih bernilai, karena stage yang lebih mudah dimenangkan juga mendapat lebih banyak dari sebuah bonus. Untuk mempertahankan stage yang kami inginkan, kami melonggarkan dua pengaman Tinta: batas tingkat kemenangan bos dengan Tinta naik dari 55% menjadi 75% di lima stage bos, dan keuntungan dari satu kali pakai Tinta naik dari 25 menjadi 35 poin persentase di empat stage. Ini adalah pengecualian yang kami catat, dan masih perlu keputusan tentang seberapa besar nilai Tinta. **[belum diverifikasi sebagai kebijakan]**

## Yang belum kami periksa

- Tingkat kemenangan berasal dari bot. Beberapa stage (4-6, 5-7, 9-5, 10-2, 10-3, 11-6) meleset sekitar sepuluh poin dari target, dan 10-8 punya rata-rata bot 62% terhadap target 33%, karena sang laksamana sangat sulit bagi bot paling sederhana tetapi mudah bagi yang lain.
- Belum ada yang memainkan kurva baru ini secara manual, jadi masalah "40 dari 800 terlalu sulit" baru teratasi pada angka-angka bot. **[belum diverifikasi]**
- Game ini sedang dalam pengembangan dan belum dirilis.
