import time

daftar_nama = ("Adnan", "Alfi", "Miko", "Daffa")
users = {
    "dosen": {"password": "dosen123", "role": "dosen"},
    "adnan": {"password": "adnan123", "role": "mahasiswa"},
    "alfi": {"password": "alfi123", "role": "mahasiswa"},
    "daffa": {"password": "daffa123", "role": "mahasiswa"},
    "miko": {"password": "miko123", "role": "mahasiswa"},
}
data_absensi = {}
no_baru = 1


def login():
    for percobaan in range(3):
        username = input("Username: ").strip().lower()
        password = input("Password: ")

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
        elif username in users and users[username]["password"] == password:
            print("Login berhasil!")
            return users[username]["role"]
        else:
            print("Username atau password salah!")

        if percobaan < 2:
            print("Tunggu 10 detik sebelum mencoba lagi...")
            time.sleep(10)

    print("Terlalu banyak percobaan. Program ditutup.")
    return None


def input_data():
    print("Daftar Nama:", daftar_nama)
    nama = input("Nama: ").strip().capitalize()
    if nama not in daftar_nama:
        print("Nama tidak ada di daftar!")
        return None

    status = input("Status [Hadir/Izin/Alpha]: ").strip().capitalize()
    if status not in ("Hadir", "Izin", "Alpha"):
        print("Status tidak valid!")
        return None

    pertemuan = input("Pertemuan ke-: ").strip()
    if not pertemuan.isdigit() or int(pertemuan) < 1:
        print("Pertemuan harus dalam bentuk angka serta positif!")
        return None

    return {"nama": nama, "status": status, "pertemuan": int(pertemuan)}


def tambah_data():
    global no_baru
    data = input_data()
    if data:
        data_absensi[no_baru] = data
        no_baru += 1
        print("Data berhasil ditambahkan!")


def tampilkan_data():
    if not data_absensi:
        print("Data masih kosong")
        return
    print("No | Nama | Status | Pertemuan")
    for no, d in data_absensi.items():
        print(no, "|", d["nama"], "|", d["status"], "|", d["pertemuan"])


def ubah_data():
    if not data_absensi:
        print("Data kosong, tidak bisa diubah")
        return
    tampilkan_data()
    no = input("Nomor data yang mau diubah: ").strip()
    if not no.isdigit() or int(no) not in data_absensi:
        print("Nomor tidak valid!")
        return
    data = input_data()
    if data:
        data_absensi[int(no)] = data
        print("Data berhasil diubah!")


def hapus_data():
    if not data_absensi:
        print("Data kosong, tidak bisa dihapus")
        return
    tampilkan_data()
    no = input("Nomor data yang mau dihapus: ").strip()
    if not no.isdigit() or int(no) not in data_absensi:
        print("Nomor tidak valid!")
        return
    data_absensi.pop(int(no))
    print("Data berhasil dihapus!")


def jalankan_menu(role):
    if role == "dosen":
        menu = {
            "1": ("Tambah Data Absensi", tambah_data),
            "2": ("Tampilkan Semua Data", tampilkan_data),
            "3": ("Ubah Data Absensi", ubah_data),
            "4": ("Hapus Data Absensi", hapus_data),
        }
    else:
        menu = {"1": ("Tampilkan Semua Data", tampilkan_data)}
    keluar = str(len(menu) + 1)

    while True:
        print("MENU", role.upper())
        for kode, (label, _) in menu.items():
            print(kode + ".", label)
        print(keluar + ". Logout")

        pilihan = input(f"Pilih menu [1-{keluar}]: ").strip()
        if pilihan in menu:
            menu[pilihan][1]()
        elif pilihan == keluar:
            print("Logout berhasil")
            break
        else:
            print("Menu tidak valid!")


def main():
    print("SISTEM ABSENSI KELAS")

    while True:
        print("=== LOGIN ===")
        role = login()
        if role is None:
            break

        jalankan_menu(role)

        while True:
            lagi = input("Login sebagai pengguna lain? [y/n]: ").strip().lower()
            if lagi in ("y", "n"):
                break
            print("Ketik y atau n!")

        if lagi == "n":
            print("Program selesai")
            break


main()