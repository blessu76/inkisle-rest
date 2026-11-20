---
title: Lewati stage setelah tiga kali kalah: tawaran lembut dengan harga
description: Di Inkisle, kalah tiga kali di stage yang sama menawarkan untuk melewatinya dengan 3 Ink. Kapan tawaran muncul, stage mana yang dikecualikan, bagaimana stage yang dilewati tampil di peta laut, dan bagaimana disimpan.
slug: skip-a-stage-after-three-losses
lang: id
translation_of: en
category: making-of
keywords: Inkisle, lewati stage, tingkat kesulitan, desain game, data tersimpan, game seluler
image_alt: Peta laut dengan satu pulau yang ditandai bendera karang kecil, dan jalur putus-putus yang melewatinya menuju pulau berikutnya.
---

Di Inkisle, game strategi penaklukan pulau kami untuk iOS, kalah tiga kali di stage yang sama memunculkan pertanyaan: "Lewati stage ini dan coba lagi nanti?" Melewati butuh 3 Ink. Stage yang dilewati mendapat bendera di peta laut dan bisa dimainkan kapan saja. Game ini masih dalam pengembangan dan belum dirilis, dan kami belum melihat popup ini di perangkat nyata [belum diverifikasi].

## Mengapa menawarkan lewati

Beberapa stage tetap sulit meski sudah disetel tingkat kesulitannya. Kami tidak ingin pemain berhenti di satu pulau. Tawaran ini membiarkan mereka maju dan kembali nanti, alih-alih berhenti bermain.

## Kapan muncul

- Popup muncul setelah **kekalahan ketiga** di stage yang sama, setelah lembar hasil tenang (1,1 detik).
- Jika pemain menolak, popup tidak muncul pada kekalahan ke-4 dan ke-5. Popup bertanya lagi pada kekalahan ke-**6, ke-9**, dan seterusnya. Bertanya setiap kali itu mengganggu; bertanya sekali saja akan melewatkan pemain yang masih buntu.
- Kekalahan dihitung per stage. Memenangkan stage mengembalikan hitungan ke 0. Kekalahan di stage yang sudah tamat atau dilewati tidak dihitung.

## Berapa harganya

Melewati butuh **3 Ink**, Ink yang sama yang sudah didapat pemain di dalam game atau dibelinya. Tidak ada mata uang atau produk baru. Nilainya satu konstanta di kode, dan teks popup, tombol, serta tautan ke toko mengikutinya.

Awalnya kami menetapkan 1 Ink, lalu menaikkannya ke 3 setelah pemilik meminta 2 sampai 3. Jika pemain punya kurang dari 3 Ink, tombol lewati berubah menjadi "Tidak ada Ink, buka toko" dan membuka lembar toko yang sudah ada. Dengan 3 Ink atau lebih, tombol lewati kembali.

## Stage yang dikecualikan

- Stage 1-1 sampai 1-4, bagian tutorial tanpa Ink. Melewatinya berarti tidak pernah belajar kontrolnya.
- Stage 1-5, tempat game memberi Ink pertama sebagai hadiah.
- Stage terakhir, karena tidak ada stage berikutnya untuk dibuka.
- Stage bos termasuk.

## Arti stage yang dilewati

- Stage berikutnya terbuka, dan stage yang dilewati punya **0 bintang**. Melewati bukan menamatkan, jadi bintang tidak bisa dibeli.
- Di peta laut, node mendapat bendera karang. Pembaca layar menambahkan "dilewati". Kartu stage berbunyi: "Stage ini dilewati. Tantang lagi kapan pun kamu siap."
- Jika dimenangkan kemudian, bendera hilang dan bintang tercatat seperti biasa.
- Sebuah laut selesai hanya jika stage-stagenya ditamatkan, jadi stage berbendera tetap harus dimenangkan agar laut selesai.
- Ending hanya terbuka dengan kemenangan sungguhan, jadi melewati stage 10-8 tidak membukanya.

## Cara penyimpanannya

Catatan progres yang ada mendapat dua kunci opsional: jumlah kegagalan per stage dan daftar stage yang dilewati. Jika keduanya kosong, kunci tidak ditulis, sehingga save lama tetap identik byte demi byte. Saat membaca, id tak dikenal serta nilai negatif atau teks dibuang, dan stage yang sudah tamat kehilangan tanda lewati, karena penamatan menang.

Pada penggabungan iCloud, jumlah kegagalan yang lebih besar dipertahankan, daftar lewati digabung, dan penamatan di perangkat lain menang. Menggabungkan snapshot yang sama lagi tidak mengubah apa pun, dan sebuah tes memeriksanya.

## Yang belum kami periksa

- Popup dan bendera di perangkat nyata atau simulator. Tes widget pada lebar 375 dan 320 px tidak menemukan overflow di 16 kolom bahasa, tetapi kami belum melihat tangkapan layar [belum diverifikasi].
- Apakah versi app lama yang menimpa snapshot iCloud menghilangkan dua kunci baru itu. Jika ya, stage yang tamat dan bintang tetap ada, hanya tanda lewati yang hilang [belum diverifikasi].
- Terjemahan selain bahasa Korea dan Inggris belum ditinjau penutur asli [belum diverifikasi].

## FAQ

### Kapan Inkisle menawarkan untuk melewati stage?

Setelah kalah tiga kali di stage yang sama, dan lagi setelah kekalahan ke-6, ke-9, dan seterusnya jika terus mencoba. Stage awal, stage hadiah 1-5, dan stage terakhir dikecualikan.

### Berapa biayanya, dan apakah dapat bintang?

Biayanya 3 Ink. Stage yang dilewati memberi 0 bintang. Jika dimenangkan kemudian, bintang didapat seperti biasa.

### Apakah melewati menyelesaikan laut atau membuka ending?

Tidak. Sebuah laut selesai hanya jika stage-stagenya ditamatkan, dan ending hanya terbuka dengan kemenangan sungguhan.
