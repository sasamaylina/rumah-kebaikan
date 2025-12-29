# Rumah Kebaikan - Platform Donasi Online

Rumah Kebaikan adalah platform berbasis web yang dirancang untuk memfasilitasi penggalangan dana dan donasi secara online. Sistem ini memungkinkan pengguna untuk berkontribusi pada berbagai kampanye sosial dengan mudah, transparan, dan terorganisir.

## 🚀 Fitur Utama

### Untuk Donatur:
- **Eksplorasi Kampanye**: Menjelajahi berbagai kampanye sosial yang sedang aktif.
- **Sistem Donasi**: Melakukan donasi dengan pesan dukungan untuk penerima.
- **Riwayat Donasi**: Melihat catatan donasi yang telah dilakukan secara personal.
- **Manajemen Akun**: Fitur registrasi dan login untuk keamanan data donatur.

### Untuk Admin:
- **Dashboard Statistik**: Memantau total donasi, jumlah donatur, dan performa kampanye dalam satu layar.
- **Manajemen Kampanye**: Membuat, mengubah (edit), dan menghapus kampanye (CRUD).
- **Pemantauan Donasi**: Melihat seluruh transaksi donasi yang masuk ke platform.

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python 3.x dengan Framework **Flask**
- **Database**: **MySQL** (diakses melalui PyMySQL)
- **Frontend**: HTML5, CSS3, dan Bootstrap (untuk desain responsif)

## 📋 Prasyarat

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal:
- [Python 3.x](https://www.python.org/downloads/)
- [XAMPP](https://www.apachefriends.org/index.html) atau MySQL Server lainnya

## ⚙️ Instalasi & Persiapan

1.  **Clone atau Unduh Proyek**
    ```bash
    git clone <repository_url>
    cd responsi
    ```

2.  **Siapkan Database**
    - Jalankan MySQL di XAMPP/Control Panel MySQL Anda.
    - Buat database baru dengan nama `rumah_kebaikan`.
    - Impor file database `rumah_kebaikan.sql` ke database yang baru dibuat.

3.  **Instal Dependensi**
    Pastikan Anda berada di direktori proyek dan jalankan:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Konfigurasi Database**
    Buka file `models/db.py` dan sesuaikan kredensial MySQL Anda (host, user, password, database).

## 🏃 Menjalankan Aplikasi

Jalankan perintah berikut di terminal:
```bash
python app.py
```
Setelah itu, buka browser dan akses:
`http://127.0.0.1:5000`

## 👤 Akun Default (Demo)

| Role  | Username | Password |
|-------|----------|----------|
| Admin | admin    | 2wsx1qaz |
| Donor | donor1   | 2wsx1qaz |

---
**Catatan**: Proyek ini dikembangkan sebagai bagian dari tugas responsi sistem informasi berbasis web.
