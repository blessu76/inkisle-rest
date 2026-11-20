---
title: Tersendatnya stage 5-8: penyebabnya layar, bukan mesin game
description: Stage 5-8 di Inkisle terasa tersendat. Kami mengukur sebelum menyentuh apa pun, menemukan bahwa biayanya ada pada penggambaran layar dan bukan aturan game, lalu menurunkan biaya satu frame dari 3,4 ke 1,3 ms di komputer. Apa yang kami ubah, apa yang kami biarkan, dan apa yang belum kami periksa di ponsel.
slug: the-stutter-on-stage-5-8
lang: id
translation_of: en
category: making-of
keywords: Inkisle, performa, tersendat, waktu frame, desain game, game seluler, optimasi
image_alt: Empat batang ungu tinggi di kiri dan empat batang koral pendek di kanan, dengan panah di antaranya dan garis putus-putus yang menandai anggaran.
---

Inkisle, game strategi penaklukan pulau kami untuk iOS, terasa tersendat di stage 5-8 saat pengujian. Dugaan yang mudah adalah mesin game, bagian yang menggerakkan armada dan memutuskan penaklukan, sudah menjadi terlalu berat. Kami mengukur dulu. Masalahnya bukan mesin, melainkan layar di sekelilingnya. Setelah perubahan, biaya satu frame di stage 5-8 turun dari 3,4 ms menjadi 1,3 ms di komputer kami. Game ini masih dalam pengembangan dan belum dirilis, dan angka-angka ini bukan dari ponsel [belum diverifikasi].

## Apa yang kami ukur

Satu frame berisi dua jenis pekerjaan: memajukan aturan game satu tick, dan menyusun serta menggambar layar. Di stage 5-8, satu tick aturan rata-rata hanya memakan 3 sampai 5 mikrodetik. Layar memakan sekitar seribu kali lebih banyak.

Sebagian besar biaya layar itu berasal dari tiga hal:

1. **Seluruh HUD dibangun ulang di setiap frame.** Pengontrol game mengumumkan perubahan di setiap frame, sehingga bilah kekuatan, teks tujuan, lembar hasil, bilah rasio, lencana, bilah pilihan, lapisan krisis, dan tombol pasang surut semuanya dibangun ulang, meski tidak ada yang berubah. Sekitar 2,5 ms dari 3,4 ms habis untuk membangun widget.
2. **Label angka meleset dari cache.** Kunci cache memuat transparansi dan ukuran persis tiap angka, padahal keduanya berubah terus-menerus saat gelombang penaklukan atau pemudaran. Jadi setiap frame menghasilkan tata letak baru, dan ketika cache melewati 600 entri, ia dikosongkan seluruhnya, sehingga satu frame harus menata ulang semuanya. Waktu gambar pada 1 persen frame paling lambat adalah 5 sampai 10 kali rata-rata.
3. **Pekerjaan kecil yang berulang.** Tiap armada mencari warna tintanya dua kali, posisi dan radius setiap pulau dihitung ulang untuk tiap armada, dan satu cache shader memakai kunci teks.

## Apa yang kami ubah

- HUD kini mendengarkan sinyal kecil yang hanya menyala saat sesuatu yang ditampilkannya berubah, seperti tick, jeda, kecepatan, status krisis, tujuan, atau petunjuk. Pengecatan tetap terjadi di setiap frame, seperti sebelumnya.
- Label angka dibulatkan ke langkah kasar (transparansi dalam 32 langkah, ukuran dalam seperempat piksel) agar cache kena, dan ketika penuh hanya separuh yang lebih lama yang dibuang.
- Pencarian berulang dihitung sekali per frame, dan kunci shader berubah dari string menjadi record.

Pembulatan ukuran dan transparansi tidak terlihat oleh mata.

## Angkanya

Diukur di komputer, pada layar 375 × 667, dalam mode yang hanya berguna untuk membandingkan sebelum dan sesudah.

| | sebelum | sesudah |
|---|---|---|
| Stage 5-8, satu frame penuh, rata-rata | 3.433 µs | 1.267 µs |
| Stage 5-8, satu frame penuh, 1% terlambat | 10.803 µs | 5.182 µs |
| Stage 5-8, menggambar, rata-rata | 818 µs | 201 µs |
| Stage 5-8, menggambar, 1% terlambat | 4.540 µs | 1.284 µs |

Game 60 frame per detik punya sekitar 16,6 ms per frame, jadi bahkan sebelum perubahan, pekerjaannya muat dalam anggaran itu di komputer. Itulah sebabnya tersendat yang kami rasakan mungkin juga punya penyebab lain (lihat di bawah).

## Yang kami biarkan

Kami tidak mengubah satu baris pun dari aturan atau kode keseimbangan. Hanya lapisan layar yang berubah: cara pengontrol mengumumkan pembaruan, widget mana yang mendengarkan, dan cache penggambaran. Seed yang sama tetap menghasilkan hasil 600 tick yang sama, dan pemeriksaan yang ada untuk gambar acuan, permainan deterministik, dan simulasi bot tetap hijau.

Kami juga menyisakan satu biaya nyata untuk nanti. Prakiraan krisis berjalan di thread layar: di stage terberat yang kami ukur, 17-3, rata-ratanya 3,4 ms dan 1 persen paling lambatnya mencapai 11,8 ms, yang bisa menimbulkan sendatan kecil setiap setengah detik. Membagi pekerjaan itu ke beberapa frame akan memberi hasil yang sama, tetapi berisiko mengubah keputusan, jadi kami tidak melakukannya sekarang. Di stage 5-8 biayanya 0,17 ms dan tidak berarti.

## Yang kami tambahkan

Benchmark mesin tanpa layar, dan tes performa dengan batas atas yang longgar. Tes ini menangkap jenis regresi di mana biaya meledak seiring jumlah armada atau setiap frame mengalokasikan terlalu banyak memori. Kami sengaja menjaga batasnya longgar, karena batas yang ketat akan gagal setiap kali mesin pengujian sibuk. Secara bawaan, tes terberat dilewati dan hanya berjalan bila diminta.

## Yang belum kami periksa

- **Frame rate di ponsel sungguhan, pada 60 atau 120 frame per detik, belum diperiksa [belum diverifikasi].** Angka kami adalah biaya thread layar di komputer, bukan biaya grafis di perangkat.
- **Tabir kabut dan lapisan pita belum diukur dan belum diubah [belum diverifikasi].** Keduanya digambar dengan blur layar penuh, yang membebani chip grafis, bukan prosesor. Jika stage 5-8 masih tersendat di ponsel, inilah tersangka pertama kami.
- Kami tidak melihat render browser pada 320, 375, 768, dan 1280 px, karena tidak ada tata letak yang berubah [belum diverifikasi].
- Bahwa input terasa lebih responsif hanyalah harapan kami [belum diverifikasi].

## FAQ

### Mengapa stage 5-8 di Inkisle tersendat?

Pengukuran kami menunjuk pada layar yang dibangun ulang dan label angka yang ditata ulang di setiap frame, bukan aturan game. Kami memperbaikinya; frame rate di ponsel sungguhan belum diperiksa.

### Apakah optimasi mengubah cara bermain?

Tidak. Kami tidak menyentuh aturan atau kode keseimbangan, dan seed yang sama memberi hasil yang sama seperti sebelumnya.

### Apakah masih tersendat di ponsel?

Kami belum tahu. Angka kami berasal dari komputer. Kami akan memeriksanya di perangkat sungguhan lewat TestFlight.
