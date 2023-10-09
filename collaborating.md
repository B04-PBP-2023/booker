# Collaborating

## Feature Branching

- Kita akan mempunyai 2 (dua) long-lived branch, yakni `main` dan `dev`.

Branch `main` akan digunakan untuk deployment, sehingga semua *change(s)* yang dibuat akan live (di-*deploy*).

Branch `dev` akan digunakan untuk *merging* dari fitur-fitur yang telah kita *develop* di branch fitur masing-masing, dan juga untuk testing sebelum *merge* ke `main` dan di-*deploy*.

- Masing-masing fitur akan mempunyai penanggungjawab (PJ).

1. Fitur autentikasi
Sandria Rania Isanura

2. Fitur pinjam buku
Rashif Aunur Rasyid

3. Fitur toko buku
Ahmad Fatih Faizi

4. Fitur *bookshelf*
Nasywa Kamila Az Zahra

5. Fitur donasi buku
Mahesa Farih Prasetyo

6. Fitur review buku
Muhammad Rafi Zia Ulhaq

- Setiap PJ akan membuat *branch* baru untuk fiturnya masing-masing.

Branch diharapkan sesuai dengan nama fitur.

- PJ hanya push ke *branch*-nya masing-masing.

Sebisa mungkin untuk tidak push ke *branch* lain, apalagi ke *branch* `main`. PJ juga diharapkan untuk testing di *local* terlebih dahulu sebelum *push* ke *remote repository*.

- Setiap *incremental change(s)* yang akan di-*merge* ke `dev`, harus melalui *pull request* (PR).

Kode yang di-*submit* diharapkan untuk di-*peer review* terlebih dahulu melalui fitur *pull request* sebelum di-*merge*.

## Reading(s) on collaborating with GitHub

[The Ultimate Github Collaboration Guide](https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67)
