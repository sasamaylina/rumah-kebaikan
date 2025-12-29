-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 28 Des 2025 pada 09.39
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rumah_kebaikan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `campaigns`
--

CREATE TABLE `campaigns` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `kebutuhan` int(11) NOT NULL DEFAULT 0,
  `terkumpul` int(11) NOT NULL DEFAULT 0,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `campaigns`
--

INSERT INTO `campaigns` (`id`, `nama`, `deskripsi`, `alamat`, `kebutuhan`, `terkumpul`, `is_active`, `created_at`) VALUES
(1, 'Bantu Korban Banjir Jakarta', 'Bantuan untuk korban banjir di wilayah Jakarta Selatan yang membutuhkan makanan, pakaian, dan tempat tinggal sementara.', 'Jakarta Selatan', 50000000, 12500000, 1, '2025-12-27 04:03:42'),
(2, 'Beasiswa Anak Yatim', 'Program beasiswa pendidikan untuk anak-anak yatim piatu agar dapat melanjutkan pendidikan mereka.', 'Bandung', 100000000, 45000000, 1, '2025-12-27 04:03:42'),
(5, 'Renovasi Sekolah Insan Cendekia', 'Galang dana untuk merenovasi gedung sekolah Insan Cendekia yang terdampak banjir. ', 'Yogyakarta', 40000000, 3500000, 1, '2025-12-27 11:55:27'),
(6, 'Cahaya untuk Sahabat Tunanetra', 'Gerakan kebaikan untuk menghadirkan harapan bagi sahabat tunanetra. Donasimu menjadi cahaya yang membantu mereka hidup lebih mandiri, berdaya, dan penuh semangat.', 'Jakarta Utara', 100000000, 0, 1, '2025-12-28 02:03:48');

-- --------------------------------------------------------

--
-- Struktur dari tabel `donations`
--

CREATE TABLE `donations` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `campaign_id` int(11) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `message` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `donations`
--

INSERT INTO `donations` (`id`, `user_id`, `campaign_id`, `jumlah`, `message`, `created_at`) VALUES
(1, 2, 1, 500000, 'Semoga membantu korban banjir', '2025-12-27 04:03:42'),
(2, 2, 2, 1000000, 'Semoga bermanfaat untuk pendidikan anak yatim', '2025-12-27 04:03:42'),
(3, 3, 5, 500000, 'Semoga anak-anak dapat kembali menuntut ilmu dengan layak.', '2025-12-27 13:10:54'),
(4, 4, 5, 3000000, 'Semoga dapat bermanfaat', '2025-12-27 15:08:56');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','donatur') NOT NULL DEFAULT 'donatur',
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `role`, `created_at`) VALUES
(1, 'admin', 'admin@rumahkebaikan.id', '2wsx1qaz', 'admin', '2025-12-27 04:03:41'),
(2, 'donor1', 'donor1@example.com', '2wsx1qaz', '', '2025-12-27 04:03:41'),
(3, 'donatur1', 'donatur1@example.com', 'donatur111', '', '2025-12-27 13:09:21'),
(4, 'isan', 'isan@example.com', 'isan123', '', '2025-12-27 15:06:31');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `campaigns`
--
ALTER TABLE `campaigns`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `donations`
--
ALTER TABLE `donations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `campaign_id` (`campaign_id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `campaigns`
--
ALTER TABLE `campaigns`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `donations`
--
ALTER TABLE `donations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `donations`
--
ALTER TABLE `donations`
  ADD CONSTRAINT `donations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `donations_ibfk_2` FOREIGN KEY (`campaign_id`) REFERENCES `campaigns` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
