# Booker

Booker adalah aplikasi web untuk meminjam, mendonasikan, dan membeli buku.

## Fitur-Fitur Booker

1. Front Page

    Tampilan awal web, di mana pengguna dapat melihat koleksi buku-buku yang tersedia, dan mencari buku.

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

8. Laman admin

    Hanya pengguna dengan role Admin dapat mengakses laman ini. Pada laman ini, terdapat fitur untuk cek stok buku untuk peminjaman dan data penjualan buku.

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

8. Laman Admin

    TBD

# Spesifikasi Fitur

## Front Page

- Berisi daftar koleksi buku yang tersedia di Booker.
- Terdapat fitur pencarian buku, dan sorting, dan filter berdasarkan kategori.
- Diharapkan menggunakan card.
- Card tersebut memuat tombol untuk pinjam dan beli (jika dapat dibeli).
- Jika card diklik, maka pengguna akan di-*redirect* ke laman yang menampilkan info lengkap buku tersebut dan juga memuat tombol pinjam dan beli (jika dapat dibeli).
- Pengguna dapat mengakses fitur ini tanpa login, tetapi tidak dapat meminjam maupun membeli.
- Terdapat wishlist yang berfungsi untuk menandai buku yang pengguna ingin pinjam/beli.

## Autentikasi

- Akan ada dua (2) role, yakni Admin dan User.
- Role Admin dapat mengakses laman admin.
- User tidak dapat mengakses laman admin.
- Pengguna dapat mengakses front page tanpa login, tetapi tidak dapat membeli ataupun meminjam buku.

## Pinjam buku

- Buku mempunyai stok, sehingga jika buku telah habis dipinjam semua, buku tersebut tidak dapat dipinjam lagi sampai ada yang mengembalikan buku tersebut.
- Ketika pengguna meng-klik tombol pinjam, maka pengguna akan di-redirect ke laman yang berisi form yang meminta user untuk memasukkan lama peminjaman (maksimal 7 hari).
- Setelah pengguna berhasil meminjam, pengguna akan di-redirect ke laman *Bookshelf*.
- Pengguna tidak dapat meminjam buku yang sama ketika masih dalam masa pinjam.
- Ketika masa peminjaman selesai, buku otomatis dikembalikan, lalu poin pengguna akan bertambah.
- Pengguna dapat mengembalikan buku lebih awal.

## Beli buku

- Pengguna hanya bisa membeli buku yang terdapat di dataset (tidak bisa membeli buku yang didonasikan)
- Pengguna dapat memilih untuk bayar menggunakan uang, atau poin.
- Pengguna dapat membeli buku yang sama berulang kali, tetapi di Bookshelf, hanya akan ada satu (1) buku saja.
- Setelah pengguna berhasil membeli buku, pengguna akan di-redirect ke laman *Bookshelf*.

## Bookshelf

- Bookshelf akan berbasis card.
- Terdapat fitur sorting berdasarkan tanggal pinjam/beli.
- Terdapat fitur filter berdasarkan kategori (genre, dipinjam/dibeli, dll).
- Buku yang telah selesai masa pinjamnya akan hilang dari bookshelf.
- Di bookshelf, terdapat fitur untuk mengembalikan buku lebih awal.

## Donasi buku

- Pada laman donasi buku, akan terdapat form yang berisi data-data buku sesuai class model (judul, pengarang, jumlah halaman, ISBN, dll).
- Setelah donasi buku berhasil, poin pengguna akan ditambah lalu redirect ke laman utama (front page).

## Review buku

- Fitur review buku dapat diakses dari card di bookshelf, dan card di frontpage.
- Pengguna bisa melakukan review jika dan hanya jika sudah pernah meminjam, atau membeli buku tsb.
- Laman ini berisi form yang berisi isan bintang (1-5), dan text field untuk ulasan.
- Setelah pengguna memberikan review, poin pengguna akan bertambah, lalu akan diredirect ke front page.

## Laman admin

- Berisi data stok buku, beserta fitur pencarian buku.
- Berisi data statistik penjualan buku.
