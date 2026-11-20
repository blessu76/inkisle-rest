---
title: Menjaga dua perangkat tetap seirama: memindahkan sinkronisasi iCloud ke kit aplikasi bersama
description: Progres, tinta, dan pengaturan Inkisle sebelumnya sudah disamakan antarperangkat lewat iCloud. Pada 16 November kami memindahkan jembatan itu ke kit aplikasi bersama. Bagaimana kami menjaga data tersimpan tetap utuh, aturan penggabungan yang tidak pernah menyusut, bagaimana tanda pembelian ditangani, dan apa yang belum kami periksa di perangkat sungguhan.
slug: keeping-two-devices-in-step
lang: id
translation_of: en
category: making-of
keywords: Inkisle, iCloud, sinkronisasi antarperangkat, data simpanan, penggabungan, game mobile
image_alt: Dua layar berukuran berbeda yang disambung seutas benang tipis, dengan pulau di kedua peta berwarna sama.
---

Di Inkisle, game strategi penaklukan pulau kami untuk iOS, progres, tinta, dan pengaturan utama (bahasa dan nama panggilan) disamakan antarperangkat dengan Apple ID yang sama lewat penyimpanan key-value iCloud milik pemain sendiri. Sinkronisasi itu sudah ada. Yang kami lakukan pada 16 November bukan membangunnya, melainkan memindahkan jembatan buatan kami sendiri ke kit aplikasi bersama, dan kekhawatiran terbesarnya adalah jangan sampai satu pun nilai tersimpan hilang. Kami belum memeriksa pulang-pergi antara iPhone dan iPad sungguhan. Game ini masih dalam pengembangan dan belum dirilis.

## Apa yang kami pindahkan

Instruksi pemilik proyek hari itu adalah bahwa sinkronisasi data game antarperangkat Apple harus wajib dan harus masuk ke kit aplikasi bersama. Kami mendapati entitlement key-value iCloud sudah menyala, dan jembatan Swift beserta pembungkus penyimpanan buatan sendiri berjalan di dalam aplikasi. Jadi:

| Bagian | Apa yang berubah |
|---|---|
| Jembatan | Menghapus jembatan Swift dan pembungkus buatan kami, lalu beralih ke penyimpanan platform milik kit: iCloud di iOS, hanya lokal di tempat lain |
| Kunci dan penyandian | Kunci penyimpanan, penyandian string, dan pengenal penyimpanan dibiarkan seperti semula |
| Sebelum membaca | Di iOS, membangunkan sinkronisasi sekali tepat sebelum membaca (sinkronisasi tetap berjalan jika gagal) |
| Pengaturan proyek | Menambahkan kapabilitas iCloud ke berkas proyek juga |

## Tidak kehilangan data

Karena kunci dan format tidak berubah, build baru membaca apa yang ditulis build lama, dan build lama membaca apa yang ditulis build baru. Kami mengunci kedua arah itu dengan uji: membaca potongan format lama dengan kode baru, membaca potongan baru dengan kode lama, dan membaca potongan pengaturan lama. Hanya kode yang dihapus; nilai yang tersimpan tidak disentuh.

## Penggabungan tidak pernah menyusut

Ketika dua perangkat memiliki progres berbeda, kami mempertahankan penggabungan milik aplikasi. Kit juga punya penggabung, tetapi tidak kami pakai. Penggabungan aplikasi sudah hanya bertambah, dan mempertahankan kunci dan format yang sama lebih aman jika dibiarkan apa adanya.

- Bintang dan rekor terbaik per tahap mengambil nilai yang lebih besar.
- Progres mengambil perangkat yang melangkah lebih jauh, dan tinta serta pengaturan hanya digabungkan, tidak pernah menyusut.
- Jika nilai di cloud berbeda dari yang terakhir kami kirim, kami mengirimnya lagi, untuk memulihkan diri dari build lama yang menimpa kunci yang sama.

## Apa yang terjadi pada tanda pembelian

Postingan sebelumnya mengatakan bahwa pembukaan tidak berpindah ke perangkat lain. Pekerjaan ini mengubahnya. Potongan sinkronisasi kini membawa tanda bahwa Buka Semua Laut sudah dibeli, dan perangkat lain yang membacanya ikut terbuka. Tanda itu **hanya bertambah.** Potongan tanpa tanda itu tidak mencabutnya; kami mengirimnya lagi.

Ini perubahan desain mengikuti instruksi "sinkronisasi wajib" dari pemilik proyek, dan ada satu batasan: setelah tanda tersinkron, pengembalian dana tidak mencabutnya di perangkat lain. Cara memperlakukan pengembalian dana dibiarkan sebagai keputusan kebijakan. Alur pembelian itu sendiri juga belum dijalankan di perangkat sungguhan.

## Ukuran dan uji

Penyimpanan key-value iCloud memiliki batas total (1 MB). Potongan sinkronisasi untuk simpanan dengan semua 240 tahap tamat berukuran sekitar 6,3 KB, dan sebuah uji menjaganya tetap di bawah 16 KB. 14 uji baru mencakup kunci dan penyandian yang tidak berubah, penggabungan dua perangkat, tanda pembelian yang menyebar dan tidak pernah dicabut, tetap lokal saat offline atau belum masuk akun, dan penggabungan setelah kembali online. Di keempat berkas uji cloud, 77 uji lulus.

## Apa yang belum kami periksa

- **Sinkronisasi sungguhan antara iPhone dan iPad belum diperiksa.** Hal ini hanya bisa dilihat di perangkat sungguhan atau TestFlight.
- Penghapusan tidak berpindah ke perangkat lain, karena sinkronisasi ini hanya menggabungkan.
- Android tidak berlaku. Data tetap di perangkat.
- Jika build lama di perangkat lain menimpa kunci yang sama, tanda pembelian bisa sesaat hilang, dan build baru mengirimnya lagi.
- Kebijakan privasi kini menjelaskan sinkronisasi ini: data game disimpan di iCloud milik pemain sendiri, bukan di server kami, dan bisa dimatikan di pengaturan perangkat.

## FAQ

### Apakah progres Inkisle disimpan di server?

Tidak. Progres disamakan antarperangkat dengan Apple ID yang sama lewat penyimpanan key-value iCloud milik pemain sendiri, dan tidak dikirim ke server kami.

### Bisakah sinkronisasi dimatikan?

Bisa. Mematikan iCloud untuk aplikasi ini di pengaturan iOS menghentikan sinkronisasi dan membiarkan data hanya di perangkat.

### Apakah tersinkron di Android?

Tidak. Di Android data tetap di perangkat.
