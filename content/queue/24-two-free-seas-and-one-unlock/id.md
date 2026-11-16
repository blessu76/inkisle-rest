---
title: Dua laut gratis dan satu kali buka kunci: cara kami menyederhanakan pembayaran
description: Inkisle membuat laut 1 dan 2 tetap gratis dan membuka sisanya dengan satu kali pembelian, Buka Semua Laut. Mengapa kami menghapus toko tinta yang habis pakai, bagaimana kunci dihitung di kode, batas yang kami tarik untuk pemulihan dan pengembalian dana, dan hal-hal yang belum kami uji.
slug: two-free-seas-and-one-unlock
lang: id
translation_of: en
category: making-of
keywords: Inkisle, pembelian dalam aplikasi, non-konsumsi, laut gratis, pulihkan pembelian, game mobile
image_alt: Dua pulau terbuka, lalu deretan pulau dengan gembok di belakangnya, dan satu kunci tergeletak melintang di atas deretan itu.
---

Inkisle, game strategi penaklukan pulau kami untuk iOS, kini membuat laut 1 dan 2 tetap gratis dan membuka laut 3 sampai 30 (28 laut) dengan satu kali pembelian, Buka Semua Laut. Kami menghapus toko tinta yang habis pakai dan mempertahankan enam item tip. Produk di toko belum dibuat, jadi hari ini belum ada yang bisa dibeli. Game ini masih dalam pengembangan dan belum dirilis. Postingan ini tidak menyebutkan harga atau tanggal.

## Yang berubah

Desain pertama membuat semua tahap gratis, dan tinta yang menurunkan tingkat kesulitan dijual sebagai item kecil yang habis pakai. Pada 15 November, pemilik proyek mengubahnya. **Laut 1 dan 2 gratis, Buka Semua Laut adalah pembelian sekali bayar yang tidak habis pakai, dan tinta tidak lagi dijual.** Tinta sekarang hanya diperoleh lewat bintang: satu untuk setiap 5 bintang, dan 2 untuk mengalahkan bos. Tinta yang sudah dibeli sebelumnya tetap berfungsi.

## Kuncinya dihitung

Jumlah laut yang terkunci tidak diketik langsung di kode. Jumlahnya adalah total laut dikurangi jumlah laut gratis. Saat ini hasilnya 30 − 2 = 28, dan ketika laut ditambahkan, teks di lembar pembelian "membuka N laut" ikut menyesuaikan. Teks penjualan yang kami siapkan menjanjikan bahwa laut baru ikut termasuk.

- Di peta, tahap dari laut 3 ke atas memakai gembok merah, dan saat diketuk, yang terbuka adalah toko, bukan tahapnya.
- Membeli atau memulihkan akan membuka semuanya.
- Setelah menang, jika tahap berikutnya berada di laut yang terkunci, game kembali ke peta.

## Aplikasi harus berjalan tanpa produk

Jika toko belum punya produk, atau pengambilan harga gagal, hanya tombol beli yang dinonaktifkan dan muncul catatan "segera hadir". Aplikasi tidak rusak. Harga diambil ulang setiap kali lembar dibuka, sehingga begitu produknya ada, fitur ini berjalan tanpa perubahan kode. Itulah posisi kami sekarang. Pengaturan produk terhambat di sisi toko, jadi kami belum pernah menjalankan alur pembelian yang sebenarnya.

## Batas yang sengaja kami tarik

| Kasus | Perilaku |
|---|---|
| Pemain yang sudah melewati laut 2 | Terkunci. Catatan dan bintang tetap ada, dan pembelian atau pemulihan membukanya lagi |
| Perangkat lain | Kemajuan tiba lewat iCloud, tetapi buka kunci tidak. Ketuk "Pulihkan pembelian" di sana |
| Pengembalian dana | Kami tidak mencabut akses |
| "Buka semua" di TestFlight | Menghapus kunci kemajuan tetapi tidak kunci pembayaran, sehingga alur pembelian bisa diuji di sandbox |

Tidak mencabut akses setelah pengembalian dana adalah pilihan sekaligus batasan. Paket `in_app_purchase` dari Flutter tidak punya status yang melaporkan pengembalian dana, dan pada skala ini kami memutuskan untuk tidak memverifikasi bukti pembelian di server. Penilaian itu adalah perkiraan [belum diverifikasi].

## Yang belum kami periksa

- Kami belum membeli atau memulihkan di perangkat sungguhan [belum diverifikasi]. Sejauh ini ada uji widget (gembok, toko, pembelian, buka kunci) dan pemeriksaan konfigurasi StoreKit.
- Tampilan 375px dan 320px tercakup oleh uji widget, bukan simulator [belum diverifikasi].
- Android memakai jalur kode yang sama, tetapi tanpa produk yang terdaftar kami tidak bisa menguji pembayaran di sana [belum diverifikasi].
- Teks pembelian dalam 11 bahasa selain bahasa Korea diterjemahkan secara mesin [belum diverifikasi].

## Pertanyaan yang sering diajukan

### Berapa bagian Inkisle yang gratis?

Laut 1 dan 2. 28 laut lainnya terbuka bersamaan setelah Buka Semua Laut dibeli. Game ini belum dirilis.

### Berapa kali saya harus membeli?

Sekali. Ini pembelian non-konsumsi, dirancang agar laut baru juga ikut termasuk.

### Apakah tip memengaruhi permainan?

Tidak. Enam item tip tidak memberi keuntungan di dalam game dan tetap seperti apa adanya.
