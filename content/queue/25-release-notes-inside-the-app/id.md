---
title: Catatan rilis di dalam aplikasi: lembar 12 bahasa dan pemeriksaan panjang
description: Catatan rilis Inkisle berupa lembar di dalam Pengaturan, bukan halaman web. Cara catatan setiap build ditulis dalam 12 bahasa, pemeriksaan jumlah dan panjang item, serta bug tes yang menampilkan lembar kosong.
slug: release-notes-inside-the-app
lang: id
translation_of: en
category: making-of
keywords: Inkisle, catatan rilis, lokalisasi, multibahasa, pengujian, game mobile
image_alt: Selembar kertas naik dari bagian bawah layar, dengan dua belas tab bahasa kecil berderet di atasnya.
---

Catatan rilis Inkisle, game strategi penaklukan pulau kami untuk iOS, berupa lembar di dalam aplikasi yang dibuka dari Pengaturan, bukan halaman web. Catatan setiap build ditulis dalam 12 bahasa, dan sebuah skrip pemeriksa memastikan jumlah item dan panjangnya sesuai. Pemeriksaan untuk build 34 menghasilkan 0 galat dan 0 peringatan. Game ini masih dalam pengembangan dan belum dirilis.

## Kami menghapus halaman web

Awalnya layar utama punya tautan "Catatan Rilis" dan tombol info (ⓘ). Pada build 32 kami menghapus keduanya. Isi jendela info (kebijakan privasi, ketentuan, versi, lisensi open source, operator, kontak, dan keterangan 16+) pindah ke Pengaturan, dan catatan rilis menjadi lembar yang dibuka dari baris "Catatan rilis" di sana. Halaman catatan rilis di situs web juga kami cabut pada 15 November. Tanpa situs terpisah, teks di dalam aplikasi menjadi satu-satunya sumber.

Lembar ini memakai bingkai yang sama dengan popup kami yang lain (InkSheet). Tingginya paling banyak 60% layar, baris judul dan tombol tutup X (48×48) tetap di tempat, dan hanya isi di dalam lembar yang bisa digulir.

## Satu build, satu berkas, 12 bahasa

Untuk setiap build, `release_notes/<build>.json` berisi judul, pengantar, dan item dalam 12 bahasa (ko, en, ja, zh-Hant, es, pt-BR, fr, de, id, th, vi, tr). Berkas-berkas ini digabung ke `assets/release_notes.json`, yang ikut dikirim bersama aplikasi, dan lembar tersebut membacanya.

## Pemeriksaan panjang dan jumlah

Sebuah skrip pemeriksa membaca berkas-berkas itu dan melaporkan pelanggaran aturan.

- **RN06:** sebuah item harus 200 karakter atau kurang. Teks bahasa Jerman terlalu panjang, jadi item penutup musim pada build 34 dipangkas menjadi 183 karakter. Pada build 31, kami memecah satu item pembelian menjadi dua agar muat dalam batas.
- **RN05:** 3 sampai 6 item dianjurkan. Ini hanya peringatan dan tidak menghalangi rilis. Peringatan yang tersisa ada pada build lama dengan 1 atau 2 item; itu catatan jujur tentang apa yang ditulis, jadi kami membiarkannya.
- Sebuah tes gagal jika tidak ada entri untuk versi dan nomor build saat ini, jadi setiap kenaikan build memerlukan catatan 12 bahasa ditulis lebih dulu.
- Skrip unggah iOS menjalankan pemeriksaan catatan rilis sebelum gerbang hijau (format, analisis, tes).

## Tes yang melihat lembar kosong

Dua tes untuk lembar catatan rilis mulai melihat lembar kosong. Penyebabnya ada pada tes, bukan aplikasi. Bundel itu berkas aset sungguhan, dan ketika ukurannya bertambah, `pumpAndSettle`, yang menunggu layar tenang, selesai sebelum pembacaan berkas rampung. Kami mengubah tes agar membuka lembar, menunggu 300 ms dengan `runAsync`, lalu menggambar ulang. Kode aplikasi tidak berubah.

## Yang belum kami periksa

- Terjemahan selain bahasa Korea dan Inggris dibuat oleh mesin dan belum ditinjau penutur asli [belum diverifikasi].
- Kami belum melihat lembar terbuka setinggi 60% di perangkat sungguhan. Uji widget pada 375×667 dan 320×568 yang menggantikannya [belum diverifikasi].

## Pertanyaan yang sering diajukan

### Di mana saya bisa membaca catatan rilis Inkisle?

Di dalam aplikasi, ketuk baris "Catatan rilis" di Pengaturan dan sebuah lembar akan terbuka. Tidak ada halaman web terpisah. Game ini belum dirilis.

### Ditulis dalam berapa bahasa?

12 bahasa. Selain bahasa Korea dan Inggris, semuanya diterjemahkan oleh mesin dan belum ditinjau.

### Apa yang terjadi jika sebuah item terlalu panjang?

Jika sebuah item melebihi 200 karakter, skrip pemeriksa melaporkan galat, lalu kami memangkasnya atau memecahnya menjadi dua.
