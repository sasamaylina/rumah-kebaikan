-- =====================================================
-- Database: rumahkebaikan$rumahdb
-- Generated from PythonAnywhere MySQL Console
-- Date: 2025-12-29
-- =====================================================

-- Create Database
CREATE DATABASE IF NOT EXISTS `rumahkebaikan$rumahdb` 
    DEFAULT CHARACTER SET utf8mb3 
    DEFAULT ENCRYPTION='N';

USE `rumahkebaikan$rumahdb`;

-- =====================================================
-- Table: users
-- =====================================================
DROP TABLE IF EXISTS `donations`;
DROP TABLE IF EXISTS `campaigns`;
DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `role` enum('admin','donatur') COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'donatur',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =====================================================
-- Table: campaigns
-- =====================================================
CREATE TABLE `campaigns` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `deskripsi` text COLLATE utf8mb4_general_ci,
  `alamat` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `kebutuhan` int NOT NULL DEFAULT '0',
  `terkumpul` int NOT NULL DEFAULT '0',
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =====================================================
-- Table: donations
-- =====================================================
CREATE TABLE `donations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `campaign_id` int NOT NULL,
  `jumlah` int NOT NULL,
  `message` text COLLATE utf8mb4_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `campaign_id` (`campaign_id`),
  CONSTRAINT `donations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `donations_ibfk_2` FOREIGN KEY (`campaign_id`) REFERENCES `campaigns` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =====================================================
-- INSERT DATA: users
-- ID dimasukkan manual untuk menjaga relasi
-- =====================================================
INSERT INTO `users` (`id`, `username`, `email`, `password`, `role`, `created_at`) VALUES
(1, 'admin', 'admin@rumahkebaikan.id', '$2b$12$DyoyyPz5Lapb8x7u4wnJcuW3IJSOyTCFrCh7YZ92Pkv/BJW1H2tC2', 'admin', '2025-12-27 04:03:41'),
(2, 'donor1', 'donor1@example.com', '$2b$12$hfrcyNJ6RsKMlUFFtQlQpOIvFUGZdqpwxRT3fVGCxEblSzfOH/C0C', 'donatur', '2025-12-27 04:03:41'),
(3, 'donatur1', 'donatur1@example.com', '$2b$12$tjQpTR6uH8HTBPeisPcCTOrFi6zxlg1PxVU4oIK0O9eglN1zOd6TG', 'donatur', '2025-12-27 13:09:21'),
(4, 'isan', 'isan@example.com', '$2b$12$kHGUllFFoe0I3MZ9Hdn59u2xfCLXyszDLHcqob5mlUoySD6akOcMm', 'donatur', '2025-12-27 15:06:31'),
(5, 'zahra', 'zahra12@example.com', '$2b$12$JPDzxDce6GH93iG7yT/mduj3do91Y/2O54QyS.S/tg0kp6aRoh9Vi', 'donatur', '2025-12-29 08:54:31'),
(81, 'ahmad_maulana', 'ahmad.maulana@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(82, 'siti_nurhaliza', 'siti.nurhaliza@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(83, 'budi_santoso', 'budi.santoso@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(84, 'rina_wulandari', 'rina.wulandari@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(85, 'agus_prasetyo', 'agus.prasetyo@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(86, 'lina_maharani', 'lina.maharani@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(87, 'dedi_kurniawan', 'dedi.kurniawan@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(88, 'melisa_hartono', 'melisa.hartono@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(89, 'rizky_fadillah', 'rizky.fadillah@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(90, 'yuniastuti', 'yuniastuti@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(91, 'fajar_putra', 'fajar.putra@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(92, 'novita_sari', 'novita.sari@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(93, 'andika_pratama', 'andika.pratama@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(94, 'fitri_ayu', 'fitri.ayu@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(95, 'heri_sutanto', 'heri.sutanto@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(96, 'diana_anggraini', 'diana.anggraini@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(97, 'indra_setiawan', 'indra.setiawan@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(98, 'nia_kusuma', 'nia.kusuma@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(99, 'tono_prayogo', 'tono.prayogo@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(100, 'amelia_rizki', 'amelia.rizki@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(101, 'wahyu_hidayat', 'wahyu.hidayat@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(102, 'sarah_putri', 'sarah.putri@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(103, 'eko_susanto', 'eko.susanto@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(104, 'lucky_pratama', 'lucky.pratama@example.com', 'password123', 'donatur', '2025-12-29 09:23:05'),
(105, 'genta', 'jaharuddinhamzah92@gmail.com', '$2b$12$4Lrgaw9YU9s96rklUKmZpuXXa5O85mG8U38KowO/T/2wDIZkiqJeG', 'donatur', '2025-12-29 10:01:58');

-- Set AUTO_INCREMENT untuk user berikutnya
ALTER TABLE `users` AUTO_INCREMENT = 106;

-- =====================================================
-- INSERT DATA: campaigns
-- ID dimasukkan manual untuk menjaga relasi
-- =====================================================
INSERT INTO `campaigns` (`id`, `nama`, `deskripsi`, `alamat`, `kebutuhan`, `terkumpul`, `is_active`, `created_at`) VALUES
(33, 'Bantu Korban Banjir Jakarta', 'Bantuan makanan, pakaian, dan tempat tinggal sementara untuk korban banjir Jakarta Selatan', 'Jakarta Selatan', 50000000, 12500000, 1, '2025-12-29 09:41:50'),
(34, 'Beasiswa Anak Yatim', 'Program beasiswa pendidikan untuk anak-anak yatim piatu', 'Bandung', 100000000, 45000000, 1, '2025-12-29 09:41:50'),
(35, 'Renovasi Sekolah Insan Cendekia', 'Renovasi gedung sekolah yang terdampak bencana', 'Yogyakarta', 40000000, 3500000, 1, '2025-12-29 09:41:50'),
(36, 'Cahaya untuk Sahabat Tunanetra', 'Donasi untuk tunanetra agar hidup lebih mandiri', 'Jakarta Utara', 100000000, 0, 1, '2025-12-29 09:41:50'),
(37, 'Bantuan Panti Jompo Surabaya', 'Bantu lansia di panti jompo', 'Surabaya', 30000000, 5000000, 1, '2025-12-29 09:41:50'),
(38, 'Donasi Obat Gratis Bandung', 'Program obat gratis untuk pasien miskin', 'Bandung', 50000000, 10000000, 1, '2025-12-29 09:41:50'),
(39, 'Paket Sembako Desa Garut', 'Distribusi sembako untuk desa terpencil', 'Garut', 25000000, 0, 1, '2025-12-29 09:41:50'),
(40, 'Rumah Aman Korban Kebakaran Depok', 'Bantu korban kebakaran agar memiliki rumah', 'Depok', 60000000, 15000000, 1, '2025-12-29 09:41:50'),
(41, 'Program Literasi Anak Malang', 'Membangun perpustakaan dan literasi anak', 'Malang', 20000000, 5000000, 1, '2025-12-29 09:41:50'),
(42, 'Bantu Hewan Terdampak Banjir Jakarta Barat', 'Donasi untuk hewan peliharaan korban banjir', 'Jakarta Barat', 15000000, 2000000, 1, '2025-12-29 09:41:50'),
(43, 'Beasiswa Mahasiswa Kurang Mampu Semarang', 'Beasiswa kuliah untuk mahasiswa kurang mampu', 'Semarang', 80000000, 20000000, 1, '2025-12-29 09:41:50'),
(44, 'Donasi Air Bersih Banten', 'Air bersih untuk desa dan wilayah terdampak kekeringan', 'Banten', 40000000, 10000000, 1, '2025-12-29 09:41:50'),
(45, 'Rehabilitasi Rumah Korban Gempa Palu', 'Bantu bangun rumah korban gempa', 'Palu', 90000000, 225500000, 1, '2025-12-29 09:41:50'),
(46, 'Donasi Peralatan Sekolah Jakarta Timur', 'Alat tulis dan buku untuk anak-anak kurang mampu', 'Jakarta Timur', 20000000, 5000000, 0, '2025-12-29 09:41:50'),
(47, 'Bantuan Kesehatan Gratis Surabaya', 'Pengobatan gratis untuk warga miskin', 'Surabaya', 50000000, 15000000, 1, '2025-12-29 09:41:50'),
(48, 'Panti Asuhan Mandiri Bandung', 'Bantu operasional panti asuhan', 'Bandung', 30000000, 10000000, 1, '2025-12-29 09:41:50'),
(49, 'Program Vaksin Gratis Jakarta Pusat', 'Vaksinasi untuk anak-anak', 'Jakarta Pusat', 25000000, 5000000, 1, '2025-12-29 09:41:50'),
(50, 'Donasi Alat Olahraga Sekolah Yogyakarta', 'Peralatan olahraga untuk sekolah', 'Yogyakarta', 15000000, 2000000, 1, '2025-12-29 09:41:50'),
(51, 'Bantu Korban Kebakaran Hutan Riau', 'Bantu warga terdampak kebakaran hutan', 'Riau', 40000000, 5000000, 1, '2025-12-29 09:41:50'),
(52, 'Donasi Komputer untuk Sekolah Jakarta Selatan', 'Komputer untuk sekolah kurang mampu', 'Jakarta Selatan', 60000000, 10000000, 1, '2025-12-29 09:41:50'),
(53, 'Bantu Pasien Kanker Bandung', 'Bantu pengobatan pasien kanker', 'Bandung', 80000000, 20250000, 1, '2025-12-29 09:41:50'),
(54, 'Donasi Peralatan Medis Jakarta Timur', 'Peralatan medis untuk klinik gratis', 'Jakarta Timur', 50000000, 10000000, 1, '2025-12-29 09:41:50'),
(55, 'Bantu Anak Difabel Surabaya', 'Bantu pendidikan anak difabel', 'Surabaya', 30000000, 5000000, 1, '2025-12-29 09:41:50'),
(56, 'Program Pemulihan Lingkungan Bogor', 'Reboisasi dan bersih sungai', 'Bogor', 40000000, 5000000, 1, '2025-12-29 09:41:50'),
(57, 'Bantuan Darurat Banjir Jakarta Utara', 'Evakuasi dan bantuan korban banjir', 'Jakarta Utara', 50000000, 10000000, 1, '2025-12-29 09:41:50'),
(58, 'Beasiswa Prestasi Anak Bandung', 'Beasiswa untuk anak berprestasi', 'Bandung', 60000000, 20000000, 1, '2025-12-29 09:41:50');

-- Set AUTO_INCREMENT untuk campaign berikutnya
ALTER TABLE `campaigns` AUTO_INCREMENT = 59;

-- =====================================================
-- INSERT DATA: donations
-- ID dimasukkan manual untuk menjaga relasi
-- =====================================================
INSERT INTO `donations` (`id`, `user_id`, `campaign_id`, `jumlah`, `message`, `created_at`) VALUES
(106, 2, 33, 500000, 'Semoga membantu korban banjir', '2025-12-29 09:52:44'),
(107, 3, 34, 750000, 'Bantuan untuk anak yatim', '2025-12-29 09:52:44'),
(108, 4, 35, 1000000, 'Semoga sekolah cepat selesai direnovasi', '2025-12-29 09:52:44'),
(109, 5, 36, 500000, 'Bantu tunanetra lebih mandiri', '2025-12-29 09:52:44'),
(110, 81, 37, 1000000, 'Bantuan untuk lansia', '2025-12-29 09:52:44'),
(111, 82, 38, 500000, 'Obat gratis untuk warga', '2025-12-29 09:52:44'),
(112, 83, 39, 750000, 'Sembako untuk desa terpencil', '2025-12-29 09:52:44'),
(113, 84, 40, 1500000, 'Bantu korban kebakaran', '2025-12-29 09:52:44'),
(114, 85, 41, 500000, 'Perpustakaan untuk anak-anak', '2025-12-29 09:52:44'),
(115, 86, 42, 250000, 'Bantuan hewan terdampak banjir', '2025-12-29 09:52:44'),
(116, 87, 43, 1000000, 'Beasiswa mahasiswa kurang mampu', '2025-12-29 09:52:44'),
(117, 88, 44, 750000, 'Air bersih untuk desa', '2025-12-29 09:52:44'),
(118, 89, 45, 1500000, 'Rehabilitasi rumah korban gempa', '2025-12-29 09:52:44'),
(119, 90, 46, 500000, 'Alat tulis untuk anak-anak', '2025-12-29 09:52:44'),
(120, 91, 47, 1000000, 'Pengobatan gratis untuk warga miskin', '2025-12-29 09:52:44'),
(121, 92, 48, 500000, 'Bantu panti asuhan', '2025-12-29 09:52:44'),
(122, 93, 49, 250000, 'Vaksin gratis anak-anak', '2025-12-29 09:52:44'),
(123, 94, 50, 500000, 'Alat olahraga sekolah', '2025-12-29 09:52:44'),
(124, 95, 51, 1000000, 'Bantu korban kebakaran hutan', '2025-12-29 09:52:44'),
(125, 96, 52, 750000, 'Komputer untuk sekolah', '2025-12-29 09:52:44'),
(126, 97, 53, 500000, 'Bantu pasien kanker', '2025-12-29 09:52:44'),
(127, 98, 54, 250000, 'Peralatan medis untuk klinik', '2025-12-29 09:52:44'),
(128, 99, 55, 500000, 'Bantu pendidikan anak difabel', '2025-12-29 09:52:44'),
(129, 100, 56, 1000000, 'Program pemulihan lingkungan', '2025-12-29 09:52:44'),
(130, 2, 57, 500000, 'Bantuan darurat banjir', '2025-12-29 09:52:44'),
(131, 3, 58, 750000, 'Beasiswa anak berprestasi', '2025-12-29 09:52:44'),
(132, 105, 45, 60000000, 'Dari hamba allah', '2025-12-29 10:02:58'),
(133, 105, 45, 150000000, '', '2025-12-29 10:04:06'),
(134, 4, 53, 250000, 'Semoga segera diberi kesembuhan.', '2025-12-29 10:14:05'),
(135, 4, 45, 500000, 'Semoga bisa bermanfaat', '2025-12-29 10:59:48');

-- Set AUTO_INCREMENT untuk donation berikutnya
ALTER TABLE `donations` AUTO_INCREMENT = 136;

-- =====================================================
-- SELESAI
-- File ini berisi struktur tabel dan data lengkap
-- AUTO_INCREMENT sudah diset agar data baru dari sistem
-- akan memiliki ID yang otomatis increment
-- =====================================================
