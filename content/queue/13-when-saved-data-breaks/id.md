---
title: Saat data tersimpan rusak: bagaimana aplikasi memulihkan diri
description: Ponsel bisa kehilangan, memotong, atau memblokir data tersimpan sebuah aplikasi. Bagaimana Inkisle menangani penyimpanan yang hilang, rusak, usang, dan tidak tersedia untuk progres, intro, dan pengaturan suara, serta di mana pemulihan kami masih kasar.
slug: when-saved-data-breaks
lang: id
translation_of: en
category: making-of
keywords: Inkisle, data simpanan, penanganan galat, ketangguhan, penyimpanan lokal, game seluler, simpanan berversi
image_alt: Sebuah buku catatan kecil dengan satu halaman robek di samping deretan pulau, cara yang tenang untuk menunjukkan simpanan yang rusak.
---
Inkisle tidak punya akun dan tidak punya server, jadi semua progres hidup **hanya di ponsel**. Itu membuat data tersimpan menjadi sederhana, dan juga berarti tidak ada yang bisa memulihkannya untukmu. Pertanyaan kami: apa yang harus dilakukan aplikasi ketika yang dibacanya kembali ternyata salah?

## Empat hal yang bisa salah

| Situasi | Yang dilakukan aplikasi |
|---|---|
| Belum ada yang tersimpan | Mulai dari level 1-1 |
| Teks tersimpan rusak (tidak bisa dibaca) | Anggap kosong, mulai dari awal |
| Disimpan oleh versi format yang berbeda | Abaikan, mulai dari awal |
| Penyimpanan ponsel sama sekali tidak bisa dibuka | Bermain di memori; tidak ada yang rusak, tetapi tidak ada yang tersimpan setelah ditutup |

Data tersimpan membawa nomor versi pada namanya dan pada isinya, sehingga perubahan format di masa depan bisa dikenali, bukan salah dibaca.

## Kerusakan di satu bagian tidak menghapus sisanya

Catatan progres memiliki satu entri per level. Tinjauan kami menunjukkan bahwa satu entri yang rusak dulu mengatur ulang semuanya. Sekarang setiap level dibaca sendiri-sendiri: entri yang tidak bisa dibaca dilewati dan level lain tetap dipertahankan. Hanya berkas yang sama sekali tidak bisa dibaca, atau versi yang berbeda, yang berarti mulai dari awal. Entri juga harus menyatakan bahwa level itu **dimenangkan**, karena hanya kemenangan yang pernah ditulis.

## Perbaikan yang benar-benar memperbaiki

Intro menyimpan simpanan kecilnya sendiri (kantong acak dari tulisan sebelumnya). Ketika itu rusak, pembacaan gagal sebelum aplikasi menulis sesuatu yang baru, sehingga teks yang rusak tetap di sana dan masalahnya berulang di setiap peluncuran. Perbaikannya: jika pembacaan gagal, mulai dari nilai bawaan dan **tulis nilai bawaan itu di atasnya**. Kode intro memiliki pengujian untuk simpanan yang rusak.

## Pengaturan kembali ke pilihan yang senyap

Satu-satunya pengaturan adalah suara. Jika data tersimpannya rusak, jawabannya adalah **mati**, bukan hidup. Berkas yang rusak tidak boleh membuat game menjadi lebih berisik.

## Progres hanya bisa bertambah

Bintang dan waktu terbaik hanya diperbaiki, dan pengulangan yang kalah tidak mengubah apa pun. Aturan pembukaan hanya melihat apakah level sebelumnya dimenangkan.

## Yang belum kami periksa

- Kami menguji teks rusak, versi yang salah, dan penyimpanan yang hilang di dalam kode. Kami **belum** menguji ponsel yang kehabisan ruang atau pencadangan dan pemulihan sistem operasi.
- Ketika seluruh berkas tidak bisa dibaca, pemain mulai lagi dari level 1-1. Bagi pemain dengan banyak bintang, itu akan terasa buruk, dan kami belum memutuskan apakah akan menambahkan sesuatu yang lebih lembut.
