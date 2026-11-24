---
title: Tombol yang bisa ditekan pembaca layar
description: Ikon tutup dan mercusuar di Inkisle punya label yang dibacakan, tetapi aksi aksesibilitasnya belum terhubung. Kami memeriksa kata yang dibacakan dan apa yang terjadi saat kontrol diaktifkan.
slug: a-button-the-screen-reader-can-press
lang: id
translation_of: en
category: making-of
keywords: Inkisle, aksesibilitas, pembaca layar, antarmuka, uji widget
image_alt: Tanda X dan ikon mercusuar pada dua kartu kecil, masing-masing dikelilingi garis penanda fokus.
---

Inkisle adalah gim strategi penaklukan pulau yang sedang dikembangkan. Saat meninjau aksesibilitas, kami memeriksa cara gim menyampaikan informasi tentang kontrol kepada pembaca layar. Ada dua kontrol yang menarik perhatian: tanda X untuk menutup panel dan mercusuar di peta yang memutar ulang akhir cerita. Kami mengembangkan gim ini untuk iOS.

## Dari nama ke aksi

Kedua kontrol sudah punya nama. Namun dalam pohon aksesibilitas Flutter, simpul yang memuat nama kehilangan aksi ketuk saat deskripsi bawaan ikon diganti. Kami menautkan aksi ke simpul yang sama dengan labelnya. Dalam pengujian, mengaktifkan Tutup menutup panel, dan mengaktifkan mercusuar membuka akhir cerita.

## Cukup sekali dibacakan

Kami juga memeriksa informasi yang dibacakan dua kali. Tombol pengatur proporsi armada memberikan persentase yang sama dalam label dan teks yang terlihat. Kontrol untuk melewati pembuka dan penanda bernomor di peta juga mengalami pengulangan serupa. Kami menyisakan satu label yang dibacakan untuk tiap kontrol, dengan informasi yang diperlukan untuk mengenalinya.

## Pertanyaan umum (FAQ)

### Apakah ini sudah diuji dengan pembaca layar di ponsel?

Uji widget memeriksa label dan aksi aksesibilitas. Kami belum memeriksa perubahan itu dengan VoiceOver di iPhone.

### Apa fungsi mercusuar di peta?

Aktifkan mercusuar untuk memutar ulang akhir cerita.
