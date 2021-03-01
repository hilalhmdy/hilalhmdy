# course-planning-scheduling
## Deskripsi Singkat Program
Aplikasi sederhana yang dapat menyusun rencana pengambilan kuliah, dengan memanfaatkan algoritma Decrease and Conquer. Penyusunan Rencana Kuliah diimplementasikan dengan menggunakan pendekatan Topological Sorting.
## Penjelasan singkat algoritma Decrease and Conquer yang diimplementasikan
Penyusunan rencana kuliah dapat dilakukan dengan pendekatan Algoritma topological sort. Mula-mula seluruh mata kuliah dibuat dalam pendekatan directed acyclic graph. Mata kuliah yang memiliki prerequisite akan memiliki edge dengan mata kuliah prerequisite-nya dengan arah dari mata kuliah prerequisite-nya menuju mata kuliah tersebut. Selanjutnya, topological sort akan diterapkan untuk menentukan mata kuliah apa saja yang diambil pada semester tertentu.
Pertama, hitung semua derajat masuk setiap node, yaitu banyaknya edge yang masuk pada node tersebut. Kemuan pilih seluruh node yang memiliki derajat masuk sama dengan 0. Ambil node tersebut, masukkan ke dalam solusi dan hilangkan node tersebut beserta semua edge yang keluar dari node tersebut, dan kurangi derajat node yang berhubungan dengan node tersebut. Kemudian langkah tersebut diulangi dan index solusi di-increment sebagai penentu semester yang bisa diambil dari mata kuliah tersebut.
## Requirements dan Instalasi
### Instalasi
- Python >= versi 3.8
- Install pyinstaller
```
pip3 install pyinstaller
```
atau
```
pip install pyinstaller
```
### Requirements input file
```
<kode_kuliah_1>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.
<kode_kuliah_2>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode_kuliah_3>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode_kuliah_4>.
```
## Cara Menggunakan Program
### Menjalankan melalui executable file
- Pastikan sudah berada di direktori bin, kemudian ketikkan perintah berikut di terminal.
```
chmod +x main_13519042
```
- Apabila berhasil, jalankan program dengan perintah berikut.
```
./main_13519024
```
- Kemudian masukkan input file yang berisi nama mata kuliah beserta prerequisite-nya.
### Menjalankan melalui 13519024,py
- Pastikan sudah berada di direktori src, kemudian ketikkan perintah berikut di terminal.
```
python3 main_13519024.py
```
atau
```
python main_13519024.py
```
- Kemudian masukkan input file yang berisi nama mata kuliah beserta prerequisite-nya.
### Contoh input dan output
- Input file
```
Fisika_IA.
Kalkulus_IA.
Pengenalan_Komputasi.
Fisika_IIA, Fisika_IA.
Kalkulus_IIA, Kalkulus_IA.
Statistika_Industri, Kalkulus_IIA.
Simulasi_Komputer, Pengenalan_Komputasi.
Ekonomi_Teknik, Statistika_Industri.
Proses_Manufaktur, Kalkulus_IIA.
Sistem_Manufaktur_Terintegrasi_Komputer, Simulasi_Komputer, Proses_Manufaktur.
```
- Output
```
You can follow this planning to grab your cumlaude
--------------------------------------------------
Semester  1  :  Fisika_IA Kalkulus_IA Pengenalan_Komputasi
Semester  2  :  Fisika_IIA
Semester  3  :  Kalkulus_IIA
Semester  4  :  Simulasi_Komputer
Semester  5  :  Statistika_Industri Proses_Manufaktur
Semester  6  :  Ekonomi_Teknik
Semester  7  :  Sistem_Manufaktur_Terintegrasi_Komputer
```
## Author
[M Hilal Alhamdy)](https://github.com/hilalhmdy)