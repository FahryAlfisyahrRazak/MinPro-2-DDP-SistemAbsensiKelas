# MinPro-2-DDP-SistemAbsensiKelas
<img width="1550" height="831" alt="Flowchart_Login drawio" src="https://github.com/user-attachments/assets/69acae33-a086-4ff8-9506-a50a0438b08c" />
<br>
Flowchart Login, Dimulai dari memasukkan Username dan Password, Bila Password/Username salah, maka akan terkunci selama 10 detik, jika user melakukan kesalahan sebanyak 3 kali, maka program akan otomatis berhenti
<br>
Jika Username dan Password benar maka User akan masuk sesuai dengan role dari user tersebut
<br>
<img width="1269" height="620" alt="Flowchart_Mahasiswa drawio" src="https://github.com/user-attachments/assets/4844ad1c-cf10-4cc7-ae78-c7a4a4eedaff" />
<br>
Flowchart Mahasiswa, Sesuai dengan Flowchart login tadi, Apabila masuk ke akun dengan role mahasiswa, maka aksesnya hanyalah melihat data absensi dan logout saja, jika logout, akan ada looping kembali ke Flowchart Login, untuk melakukan pergantian akun atau memberhentikan proses dari program
<br>
<img width="1962" height="1550" alt="Flowchart_Dosen drawio" src="https://github.com/user-attachments/assets/992f60a2-b4b9-4049-a7a3-d7e30bb0badc" />
<br>
Flowchart Dosen, Jika masuk ke program menggunakan akun dengan role dosen, maka akses yang diberikan adalah CRUD Program,
Bisa Menambah,Melihat,Mengubah, dan Menghapus data Absensi yang ada, apabila melakukan logout, maka akan terjadi looping yang sama seperti sebelumnya yaitu bisa memilih untuk menghentikan program atau berganti akun
<br>
<img width="715" height="309" alt="image" src="https://github.com/user-attachments/assets/86ac58f6-33f2-4ae4-ad6e-ee0a81e0182d" />
<br>
List, Tuple, Dictionary dan Library yang digunakan untuk Kode ini
<br>
<img width="640" height="393" alt="image" src="https://github.com/user-attachments/assets/cf209494-66aa-488c-ad1e-bfc843168e45" />
<br>
Perulangan for dengan range (3) yang berarti program akan berhenti apabila percobaan login ke 3 gagal, dengan menggunakan return yang memiliki value "None", menggunakan library "time" untuk memberikan jeda 10 detik sebelum bisa menginput ulang Username dan Password, di Input username, menggunakan (.strip(),.lower()) untuk membantu user agar apabila terjadi typo seperti terpencet tombol spasi ataupun capslock yang tidak sesuai dengan akun
<br>
Apabila Username atau Password kosong, maka akan muncul peringatan "Username dan Password Tidak Boleh Kosong!" karna menggunakan logika OR.
<br>
Jika Username dan Password ada, maka akan muncul "login berhasil" lalu program akan mengembalikan value kepada pemanggil, tergantung pada "role" dari akun, maka akses yang didapat akan berbeda
<br>
<img width="607" height="363" alt="image" src="https://github.com/user-attachments/assets/e7ad73d5-a46b-45a5-9b2e-5b6c97609718" />
<br>
Fungsi untuk menginput data absensi dari murid yang ada di Dictionary, Saat akan menambahkan data baru, akan diperlihatkan daftar nama, lalu bisa meng-input nama sesuai dengan yang ada di dalam daftar nama tersebut, apabila nama tidak ada di dalam daftar nama, maka akan mengeluarkan peringatan "Nama Tidak Ada Di Daftar Nama".
<br>
Sama seperti di daftar nama, user akan diperlihatkan jenis status dari murid yang akan di Absen, Apabila kondisi yang di input tidak sesuai dengan pilihan yang ada di dalam opsi Status, maka akan mengeluarkan peringatan "Status Tidak Valid".
<br>
Di bagian pertemuan, User diharuskan untuk menggunakan Angka (int) untuk bisa memasukkan data karena penggunaan (.isdigit()), serta angka yang diberikan haruslah angka positif karena logika <1 yang membuatnya harus menginput minimal angka 1 positif, apabila semua syarat telah terpenuhi, maka value tersebut akan dikembalikan ke pemanggil nya dan data berhasil ditambahkan
<br>
<img width="404" height="175" alt="image" src="https://github.com/user-attachments/assets/c1e07a1e-09e9-4f37-9a74-3652c921e923" />
<br>
Bagian ini pada dasarnya adalah persambungan dari fungsi diatas, yang berguna untuk mengatur nomor keberapa kah data yang telah berhasil dimasukkan menggunakan fungsi tadi dan menambahkan nomor menggunakan increment, global digunakan untuk memberitahu python jika di dalam fungsi tersebut ada variabel eksternal yang digunakan, dan bukan variabel dari function itu sendiri, menggunakan increment +=1 pada variabel data yang tersambung dengan variabel no_baru, apabila input tersebut telah terkonfirmasi berhasil ditambahkan maka akan mengeluarkan pernyataan "Data berhasil ditambahkan!"
<br>
<img width="576" height="172" alt="image" src="https://github.com/user-attachments/assets/0e18e871-63e6-47cd-9b5e-97e9f5d1ba79" />
<br>
Apabila data absensi kosong, akan menampilkan pemberitahuan "Data Masih Kosong" lalu melakukan return,
Apabila data sudah terisi, maka akan menampilkan data yang sudah di input menggunakan (.items())
<br>
<img width="482" height="273" alt="image" src="https://github.com/user-attachments/assets/85acdff5-22bf-4065-bc73-08e35f21b7df" />
<br>
Bagian ini digunakan untuk mengubah data, Apabila data absensi kosong, akan mengeluarkan peringatan "Data kosong, tidak bisa diubah" lalu melakukan return, apabila ada data yang di dalam dictionary, maka akan mengeluarkan pernyataan "Pilih data yang mau diubah", jika memilih nomor data yang sudah ada, maka user akan diberi opsi untuk melakukan input ulang menggunakan function input data, jika memilih nomor data yang tidak ada, maka akan mengeluarkan peringatan "Nomor tidak Valid".
<br>
<img width="465" height="236" alt="image" src="https://github.com/user-attachments/assets/b486fd30-b923-4215-a964-03648de8b9e1" />
<br>
Digunakan untuk menghapus data yang sudah ada, Apabila data masih kosong maka akan mengeluarkan peringatan "Data kosong, Tidak bisa Dihapus", Apabila ada data di dalam dictionary maka akan mengeluarkan opsi nomor data yang dapat dihapus, jika memilih nomor data yang ada, maka akan keluar pernyataan "Data berhasil Dihapus", jika memilih nomor yang tidak ada di dalam data, maka akan mengeluarkan peringatan "Nomor tidak valid"

