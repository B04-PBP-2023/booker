# Booker

Booker adalah aplikasi web untuk meminjam, mendonasikan, dan membeli buku.

## Fitur-Fitur Booker

1. Front Page

Tampilan awal web, di mana pengguna dapat melihat koleksi buku-buku yang tersedia.

2. Autentikasi

Setiap pengguna harus mendaftar dan login ketika ingin mengakses *website*, agar data-data pengguna pada *website* aman.

3. Pinjam buku

Pengguna dapat meminjam buku. Buku yang dipinjam dapat diakses di bookshelf masing-masing pengguna. Setiap buku yang telah selesai masa pinjamnya, akan otomatis dikembalikan. Ketika pengguna mengembalikan buku, pengguna akan mendapatkan poin yang dapat ditukar dengan buku.

4. Beli buku (Toko Buku)

Pengguna dapat membeli buku. Buku yang telah dibeli dapat diakses di bookshelf masing-masing pengguna. Pengguna juga dapat menggunakan poin yang diperoleh dari meminjam buku atau donasi untuk membeli buku.

5. *Bookshelf*

Bookshelf menyimpan dan memungkinkan pengguna mengakses semua buku yang telah dibeli dan/atau sedang dipinjam oleh pengguna.

6. Donasi buku

Pengguna dapat mendonasikan buku. Setiap buku yang didonasikan, pengguna akan mendapat poin yang dapat ditukarkan dengan buku di Toko Buku. Buku yang telah didonasikan, akan tersedia untuk dipinjam oleh pengguna lain.

7. Review buku

Pengguna yang sudah pernah meminjam/membeli buku, dapat memberikan ulasan untuk buku tersebut. Setiap pengguna memberi ulasan, pengguna akan mendapatkan poin yang dapat ditukar dengan buku.

## Pembagian Tugas

1. Front page (Tampilan dataset buku)

Ahmad Fatih Faizi

2. Fitur autentikasi

Sandria Rania Isanura

3. Fitur pinjam buku

Rashif Aunur Rasyid

4. Fitur beli buku

Ahmad Fatih Faizi

5. Fitur *bookshelf*

Nasywa Kamila Az Zahra

6. Fitur donasi buku

Mahesa Farih Prasetyo

7. Fitur review buku

Muhammad Rafi Zia Ulhaq

# Spesifikasi Fitur

## Front Page

- Berisi daftar koleksi buku yang tersedia di Booker.
- Diharapkan menggunakan `card`.
- Card tersebut memuat tombol untuk pinjam dan beli (jika dapat dibeli).
- Jika card diklik, maka pengguna akan di-`redirect` ke laman yang menampilkan info lengkap buku tersebut dan juga memuat tombol pinjam dan beli (jika dapat dibeli).
- Pengguna dapat mengakses fitur ini tanpa login, tetapi tidak dapat meminjam maupun membeli.
- Terdapat wishlist yang berfungsi untuk menandai buku yang pengguna ingin pinjam/beli.

## Autentikasi

- Akan ada satu (1) role saja, yakni User.
- Pengguna dapat mengakses front page tanpa login, tetapi tidak dapat membeli ataupun meminjam buku.

## Pinjam buku

- Ketika user meng-klik tombol pinjam, maka pengguna akan di-redirect ke laman atau muncul popup yang berisi form yang meminta user untuk memasukkan lama peminjaman (maksimal 7 hari).
- Setelah pengguna berhasil meminjam, pengguna akan di-redirect ke laman *Bookshelf*
- Pengguna tidak dapat meminjam buku yang sama ketika masih dalam masa pinjam.
- Ketika masa peminjaman selesai, buku otomatis dikembalikan, lalu poin pengguna akan bertambah.

## Beli buku

TODO!
