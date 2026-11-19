---
title: Akhir yang diputar sekali saja, dan sebuah mercusuar untuk melihatnya lagi
description: Akhir season 1 Inkisle diputar sendiri tepat satu kali, saat tahap terakhir babak 30 pertama kali diselesaikan. Bagaimana kami menetapkan aturan pemutaran ulang, bagaimana pemain yang sudah menamatkannya dan akhir babak 10 ditangani, dan apa yang belum kami periksa pada terjemahan maupun di perangkat sungguhan.
slug: an-ending-that-plays-once
lang: id
translation_of: en
category: making-of
keywords: Inkisle, season 1, akhir cerita, akhir terbuka, mercusuar, desain game, game mobile
image_alt: Sebuah pulau sunyi di laut yang tenang dengan satu mercusuar menyala, dan rute peta laut berhenti di depannya.
---

Akhir season 1 Inkisle, game strategi penaklukan pulau kami untuk iOS, diputar sendiri satu kali, saat tahap 8 babak 30 pertama kali diselesaikan. Untuk menontonnya lagi, pemain mengetuk mercusuar di bagian atas babak 30. Akhir ini tidak punya kata penutup; satu-satunya tanda adalah "Inkisle · Season 1". Tulisan ini lebih membahas kapan akhir ini diputar dan kapan tidak, serta bagaimana kami menetapkan aturannya, ketimbang apa yang ditampilkannya. Game ini masih dalam pengembangan dan belum dirilis.

## Empat aturan

Ini adalah aturan pemutaran ulang yang kami tetapkan saat akhir ini dimasukkan.

- **Sekali, pada penyelesaian pertama.** Diputar sendiri begitu tahap 8 babak 30 pertama kali dimenangkan.
- **Tidak pernah lagi dengan sendirinya.** Memenangkan tahap yang sama lagi, atau memulai ulang aplikasi, tidak memutarnya secara otomatis.
- **Bisa dilewati kapan saja.** Satu ketukan menuju bingkai diam terakhir, dan perangkat dengan kurangi gerakan aktif langsung mulai di bingkai diam.
- **Pemutaran ulang lewat mercusuar.** Sebuah mercusuar berada di bagian atas babak 30, dan mengetuknya memutar akhir yang sama lagi.

Sekalipun sebuah akhir berdurasi kurang dari 30 detik, kami memutuskan bahwa "sekali, tepat setelah menang" adalah hadiah dan "setiap kali menang" adalah gangguan.

## Di mana "sudah ditonton" dicatat

Apakah akhir ini sudah diputar disimpan sebagai kunci cerita dalam data simpanan. Kunci untuk akhir season **sengaja dipisahkan** dari kunci untuk akhir babak 10. Jika keduanya memakai satu kunci, pemain yang sudah menonton akhir babak 10 bisa dianggap sudah menonton akhir season. Satu pengujian memeriksa hal ini: menonton akhir babak 10 tidak menyentuh kunci season.

## Pemain yang sudah menamatkannya

Seseorang mungkin sudah menyelesaikan tahap 8 babak 30 sebelum akhir ini ada. Untuk simpanan itu, momen penyelesaian pertama sudah lewat, sehingga tidak ada yang diputar sendiri dan hanya mercusuar yang muncul. Kami memilih tidak memaksakan momen yang sudah berlalu, dan membiarkan pemain menekannya kapan pun ia mau.

Dalam perubahan yang sama, mercusuar babak 10 dipindahkan ke bagian atas babak 10, tempat yang semestinya.

## Apa yang dikunci oleh pengujian

Akhir ini punya 18 pengujian. Yang terkait dengan aturan-aturan ini:

- Diputar tepat sekali pada kemenangan pertama tahap 8 babak 30, dan tidak saat pemain masuk kembali.
- Tidak ada yang diputar pada tahap 7 babak 30 atau tahap 8 babak 29.
- Simpanan yang sudah menyelesaikan tahap 8 babak 30 tidak mendapat pemutaran otomatis, hanya mercusuar.
- Pada 375px dan 320px dalam uji widget, memutar, melewati, dan keluar di tengah semuanya berfungsi.
- Teks di semua 12 bahasa muat tanpa meluap.

## Tanpa kata penutup

Baris terakhir, dalam bahasa Korea, adalah "Air yang dalam memantulkan." (「깊은 물이 비친다.」). Tidak ada versi bahasa yang membawa kata seperti "Tamat", dan tanda di bagian bawah adalah "Inkisle · Season 1". Aturan pemutaran ulang berasal dari pemikiran yang sama: ceritanya tertutup, tetapi aplikasinya tidak. Setelah babak 30, pemain masih bisa mengulang babak, mengumpulkan tiga bintang, dan melihat papan skor.

## Apa yang belum kami periksa

- **Teks akhir dalam 10 bahasa selain Korea dan Inggris diterjemahkan oleh mesin dan belum ditinjau [belum diverifikasi].** Dengan hanya beberapa baris di layar, kualitas terjemahan langsung terlihat.
- Pudar yang lambat, huruf emas, dan volume lonceng belum dilihat di perangkat sungguhan [belum diverifikasi].
- Tampilan 375px dan 320px hanya diperiksa dalam uji widget, yang font ujinya jauh lebih lebar daripada yang asli [belum diverifikasi].
- Apakah akan ada season 2 belum diputuskan, dan tanggal rilis belum ditetapkan.

## FAQ

### Berapa kali akhir ini diputar sendiri?

Sekali, saat tahap 8 babak 30 pertama kali diselesaikan. Setelah itu pemain mengetuk mercusuar di bagian atas babak 30 untuk melihatnya lagi.

### Bisakah akhir ini dilewati?

Bisa. Satu ketukan melompat ke bingkai diam terakhir, dan dengan kurangi gerakan aktif, akhir ini mulai di bingkai diam.

### Apakah teks akhir sudah ditinjau di semua bahasa?

Belum. Terjemahan selain Korea dan Inggris diterjemahkan oleh mesin dan belum ditinjau.
