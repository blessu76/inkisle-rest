---
title: Yang tidak dimiliki aplikasi ini: tanpa iklan, tanpa akun, tanpa pelacakan
description: Sebagian desain Inkisle adalah soal apa yang ditinggalkan. Aplikasi tidak meminta akun dan tidak punya iklan maupun alat pelacak, berjalan di iOS dan Android dari satu basis kode, dan kami menggambar ikon baru untuk keduanya. Apa yang kami putuskan dan apa yang belum kami periksa.
slug: what-the-app-does-not-have
lang: id
translation_of: en
category: making-of
keywords: Inkisle, privasi, tanpa iklan, tanpa akun, ikon aplikasi, iOS, Android, Flutter, game seluler
image_alt: Sebuah pulau berwarna karang yang digambar sebagai noda tinta sederhana di atas latar krem, ikon aplikasi Inkisle.
---
Banyak hal yang membuat sebuah aplikasi terasa nyaman adalah apa yang **tidak** dilakukannya. Untuk rilis pertama Inkisle, kami memutuskan daftar singkat hal-hal yang ditinggalkan.

## Tanpa akun, tanpa iklan, tanpa pelacakan

- **Tanpa akun.** Kamu membuka aplikasi dan bermain. Tidak ada pendaftaran dan tidak ada masuk.
- **Tanpa iklan dan tanpa alat pelacak.** Daftar paket luar aplikasi ini pendek: satu untuk menyimpan pengaturan kecil di ponsel, satu untuk memutar suara, dan satu untuk membuka halaman web. Di dalamnya tidak ada paket iklan, tidak ada paket analitik, dan tidak ada paket masuk.
- **Progres tetap di ponsel.** Bintang yang tersimpan dan pengaturan suara disimpan secara lokal dan tidak dikirim ke mana pun.

Aplikasi ini memiliki layar informasi dengan tautan ke kebijakan privasi, yaitu halaman yang sama dengan yang ada di situs web ini. Satu-satunya hal yang menyentuh jaringan adalah membuka halaman itu, dan itu hanya terjadi ketika pemain mengetuknya. Kebijakan itu pertama kali ditulis untuk situs web ini, jadi masih harus diperiksa dan diperbarui agar mencakup aplikasi sebelum apa pun dikirim ke toko aplikasi.

## Satu basis kode, dua platform

Inkisle dibuat dengan Flutter, sehingga **iOS dan Android dikembangkan bersama** dari kode yang sama, dan setiap perubahan diuji untuk keduanya. Rencananya adalah **rilis di iOS lebih dulu**. Kami tetap membangun dan menguji Android sepanjang waktu, supaya tidak menjadi proyek kedua di kemudian hari. Game dikunci pada orientasi potret di keduanya. Versi minimumnya adalah iOS 13 dan Android API level 24.

## Ikon

Ikonnya adalah **pulau tinta berwarna karang** yang sederhana di atas latar krem. Satu kode gambar menghasilkan tiga berkas:

- ikon persegi biasa untuk iOS dan Android lama,
- latar depan "adaptif" Android, digambar di dalam area aman 66% yang dipotong oleh Android,
- siluet satu warna untuk ikon bertema Android 13.

Kami pernah merilis bug di sini dan sudah memperbaikinya: ikon adaptif diperkecil dua kali (sekali oleh kami dan sekali oleh pengaturan build), sehingga tampak terlalu kecil di Android. Sekarang pengecilan hanya terjadi di satu tempat.

## Yang belum kami periksa

- Kami belum menjalankan aplikasi di **iPhone atau ponsel Android sungguhan** dari build toko, dan belum mengirimkannya ke toko mana pun. Hal-hal seperti peninjauan toko, layar aplikasi dalam bahasa lain, dan tampilan ikon di berbagai launcher masih terbuka.
- "Tanpa pelacakan" menggambarkan apa yang ada di kode kami sendiri dan daftar paket kami. Kami belum mengaudit paket-paket yang kami andalkan selain membaca deskripsinya.
