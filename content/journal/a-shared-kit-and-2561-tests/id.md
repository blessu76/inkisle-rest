---
title: Apa yang kami jaga saat meningkatkan kit bersama: gerbang 2.561 tes
description: Setiap kali Inkisle meningkatkan kit bersama yang dipakai aplikasi kami, kit itu harus lolos gerbang format, analisis, dan tes penuh. Mengapa kami tidak mengganti satu fitur kit secara utuh, bagaimana tes waktu goyah saat beban tinggi, file apa yang berubah pada peningkatan terakhir, dan apa yang belum kami periksa.
slug: a-shared-kit-and-2561-tests
lang: id
translation_of: en
category: making-of
keywords: Inkisle, kit bersama, tes, Game Center, peningkatan versi, game mobile
image_alt: Beberapa balok kecil berbentuk sama dalam satu bingkai, dengan satu titik hijau yang melintas di atasnya.
published: 2026-11-24T12:45+09:00
---

Inkisle, game strategi penaklukan pulau kami untuk iOS, memakai kit bersama yang diandalkan beberapa aplikasi kami. Setiap kali kami menaikkan versi kit, satu gerbang menjalankan format, analisis statis, dan seluruh rangkaian tes sebelum kami melakukan commit. Pada 19 November kami memindahkan kit dari 0.15.2 ke 0.15.3: gerbang meloloskan 2.561 tes (8 dilewati), dan hanya dua file yang berubah, `pubspec.yaml` dan `pubspec.lock`. Tulisan ini membahas bagaimana angka itu dijaga dan apa yang goyah di sepanjang jalan. Game ini masih dalam pengembangan dan belum dirilis.

## Gerbang punya tiga langkah

Satu skrip menjalankannya berurutan sebelum commit: format kode tidak boleh berubah, analisis statis harus melaporkan 0 masalah, dan semua tes harus lolos. Jika ada yang gagal, kami tidak melakukan commit. Saat orang lain berkata "sudah lolos", kami menjalankannya lagi sendiri sebelum commit.

## 14 November: kami tidak mengganti seluruh fitur kit

Dengan memindahkan kit dari 0.12.0 ke 0.13.0, kit itu bisa menangani nama panggilan dan papan peringkat Game Center. Instruksi pemilik proyek adalah setiap game membiarkan pemain menetapkan nama panggilan saat pertama kali dibuka dan tampil di papan peringkat Game Center. Kami **tidak mengganti seluruh fitur pemain milik kit.** Ada empat alasan kami menganggap versi kami sendiri lebih baik:

1. Nama panggilan tersimpan di dalam catatan pengaturan, yang disinkronkan antarperangkat lewat iCloud. Memindahkannya ke penyimpanan kit akan merusak sinkronisasi itu.
2. Kami sudah punya lembar nama panggilan dalam 16 bahasa dan tes yang dibekukan untuk kombinasi bahasa dan ukuran layar.
3. Papan peringkatnya adalah 24 papan dinamis, dengan nilai yang diturunkan dari catatan kemajuan yang disinkronkan. Memindahkannya akan menyisakan dua tempat yang menyimpan skor terbaik.
4. Play Games di Android masih membutuhkan pustaka yang dipakainya.

Jadi hanya koneksi Game Center di iOS yang pindah ke kit, dan ID papan, nama panggilan tersimpan, dan skor terbaik terbawa tanpa berubah. Pengiriman ulang antrean setelah masuk terlambat dan pengisian awal nama panggilan dengan nama Game Center masuk bersamaan. Kami menambah 10 tes, dan gerbang lalu meloloskan 1.990 tes (7 dilewati).

## Tes waktu goyah

Dua kali di gerbang ini, tes yang mengukur waktu goyah saat beban tinggi. Tes anggaran bingkai yang menggambar 800 jalan gagal sekali ketika tes berjalan paralel, dan saat pekerjaan iCloud, tes anggaran performa gagal sekali. Keduanya lolos saat dijalankan sendiri atau saat seluruh rangkaian dijalankan lagi. Kami membacanya sebagai beban, bukan perubahan kami, tetapi kami tidak menelusuri penyebabnya. Kami tidak melonggarkan anggarannya.

## 19 November: dua file berubah

Versi 0.15.3 membiarkan API publik seperti semula; versi ini membuat penghitungan ulang dalam sinkronisasi iCloud berhenti setelah pembongkaran dan menambahkan dokumentasi. Kami tidak mengubah kode maupun tes di aplikasi. Batas ukuran yang dipakai aplikasi (512 KB) memang disengaja, jadi kami mempertahankannya. File yang berubah adalah `pubspec.yaml` dan `pubspec.lock`, dan gerbang lolos pada percobaan pertama, kali ini tanpa goyangan waktu. Jumlah tes bertambah dari 1.990 pada 14 November menjadi 2.561.

## Yang belum kami periksa

- **Masuk ke Game Center, pengiriman skor, layar papan peringkat, dan bolak-balik iCloud belum diperiksa di perangkat sungguhan.** Kami akan melihatnya di TestFlight.
- Tampilan 375px dan 320px tercakup oleh uji widget pada 320×568, bukan dilihat langsung.
- Kami tidak menemukan akar penyebab tes yang goyah saat beban tinggi.
- Angka di sini adalah hasil gerbang pada hari itu, dan jumlah tes akan berubah kemudian.

## Pertanyaan yang sering diajukan

### Apa itu kit bersama?

Kumpulan kode yang dipakai bersama oleh beberapa aplikasi kami. Inkisle memakai bagian nama panggilan, Game Center, dan sinkronisasi iCloud-nya.

### Apa yang kalian periksa saat meningkatkan kit?

Satu skrip memeriksa bahwa format tidak berubah, bahwa analisis statis melaporkan 0 masalah, dan bahwa semua tes lolos. Jika ada yang gagal, kami tidak melakukan commit.

### Apakah game ini sudah dirilis?

Belum. Game ini masih dalam pengembangan dan belum dirilis.
