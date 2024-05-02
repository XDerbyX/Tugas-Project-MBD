# Tugas-Project-MBD

Membuat GUI untuk Database MySQL dengan Python untuk integrasi dengan database MySQL.

[Link Repository Github](https://github.com/XDerbyX/Tugas-Project-MBD)

## Kelompok 15: Servis Mobil
- D121221082 | Muh. Naufal Jalaluddin
- D121221072 | Muh. Wahyu Ramadhan

## Library Python yang digunakan:
- **tkinter**: Digunakan untuk membuat antarmuka grafis (GUI) pada aplikasi Python.
- **ttkbootstrap**: Digunakan untuk mengatur tampilan GUI dengan gaya bootstrap yang modern.
- **mysql.connector**: Digunakan untuk menghubungkan program Python dengan database MySQL.

> Note:
> Penginstalan library tersebut dapat dilakukan melalui command-line interface (CLI):
>- Instalasi tkinter
>```
>pip install tk
>```
>- Instalasi ttkbootstrap
>```
>pip install ttkbootstrap
>```
>- Instalasi mysql.connector
>```
>pip install mysql-connector-python
>```
-------------------------------------------------------

## Fungsi Program:
- Mengakses Tabel pelanggan dari Database MySQL.
- Search Function untuk Nama Pelanggan dalam dalam tabel.
- Index Function untuk mempercepat pencarian data pada dalam tabel.
- Insert Function untuk memasukkan data pelanggan pada dalam tabel.
- Delete Function untuk menghapus data pelanggan pada dalam tabel.
- Pengkoreksian Auto-Increment ID untuk pelanggan pada dalam tabel.

> Note:
> ### Program hanya bisa berjalan jika sudah terkoneksi dengan host database MySQL yang digunakan.
>
> Berikut segment kode program yang digunakan untuk inisialisi koneksi database MySQL:
>```
> def connect_to_database():
>    try:
>        connection = mysql.connector.connect(
>            host="127.0.0.1",
>            user="root",
>            password="",
>            database="Servis_Mobil"
>        )
>        return connection
>    except mysql.connector.Error as error:
>        messagebox.showerror("Error", f"Failed to connect to database: {error}")
>        return None
>```
-------------------------------------------------------
## Tampilan Window Utama Pada GUI:
<img src='https://github.com/XDerbyX/Tugas-Project-MBD/assets/42211348/5a55e747-eb75-457c-ac99-9c746cc15cfac' width="640">


Data yang digunakan bisa dilihat pada file [PELANGGAN.txt](https://github.com/XDerbyX/Tugas-Project-MBD/blob/main/PELANGGAN.txt)

-------------------------------------------------------

### Pada GUI, terdapat 4 fungsi yang dapat digunakan dalam program:
- Menggunakan **_'Search'_** untuk mencari nama pelanggan yang ada pada tabel.
- Menggunakan **_'Create Index'_** untuk mempercepat pencarian data berdasarkan nilai Nama_Pelanggan.
- Memasukkan data pada tabel dengan tombol **_'Insert Data'_**
- Menghapus data pada tabel dengan tombol **_'Delete Data'_**
- Mengkoreksi Auto-Increment untuk ID tabel Pelanggan sebelum memasukkan data baru dengan tombol **_'Reset Increment'_**

### Contoh Pemasukan Data:
<img src='https://github.com/XDerbyX/Tugas-Project-MBD/assets/42211348/5d508efe-fa74-4a85-bb91-5cbc28fadfa2' width="740">

Data yang diisi adalah **Nama**, **Alamat**, dan **No. HP**. Setelah diisi, pencet tombol **_'Submit'_** untuk menambahkan data ke tabel.

> Note:
> Semua data harus diisi pada kolom yang ada. Jika ada yang kosong, maka akan muncul notifikasi untuk mengisi semua kolom yang belum diisi.

-------------------------------------------------------

### Contoh Penghapusan Data:
<img src='https://github.com/XDerbyX/Tugas-Project-MBD/assets/42211348/43395814-6501-4b0c-bdfa-4b078c795f5e' width="350">

Penghapusan data dilakukan dengan mengambil ID pelanggan dan menginput ID tersebut ke dalam kolom. Setelah itu pencet tombol _'Delete'_ untuk mengkonfirmasi penghapusan data pelanggan pada tabel.

-------------------------------------------------------

### Contoh Pengkoreksian Auto-Increment ID Pelanggan Pada Tabel:
<img src='https://github.com/XDerbyX/Tugas-Project-MBD/assets/42211348/6c7ec1d8-d522-497b-8f49-343f9700a470' width="350">

Masukkan angka yang ingin digunakan untuk memulai ulang perhitungan ID untuk tabel database.

> Note
> Angka yang dipakai adalah angka yang diinput ditambah 1. (Contohnya, jika input angka adalah 0, maka ID pelanggan berikutnya yang akan diberikan adalah 1).

-------------------------------------------------------

## Preview Video Penggunaan Program:
[![Nonton Video](https://github.com/XDerbyX/Tugas-Project-MBD/assets/42211348/39773641-803d-4d3d-906e-061dc1a1f306)](https://youtu.be/ihvoTHUZpqo)
