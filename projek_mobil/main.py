from domain.models import Mobil
from infrastructure.in_memory_repo import InMemoryMobilRepository
from usecases.mobil_service import MobilService

def menu():
    print("\n=== Sistem Manajemen Mobil ===")
    print("1. Tambah Mobil")
    print("2. Lihat Semua Mobil")
    print("3. Lihat Mobil by ID")
    print("4. Edit Mobil")
    print("5. Hapus Mobil")
    print("0. Keluar")

def input_mobil():
    merk = input("Masukkan merk mobil: ")
    tahun = int(input("Masukkan tahun: "))
    warna = input("Masukkan warna: ")
    return Mobil(id=0, merk=merk, tahun=tahun, warna=warna)

def main():
    repo = InMemoryMobilRepository()
    service = MobilService(repo)

    while True:
        menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            mobil = input_mobil()
            hasil = service.add_mobil(mobil)
            print(f"Mobil berhasil ditambahkan dengan ID {hasil.id}")

        elif pilihan == "2":
            all_mobil = service.browse_mobil()
            for m in all_mobil:
                print(f"ID: {m.id} | Merk: {m.merk} | Tahun: {m.tahun} | Warna: {m.warna}")
        
        elif pilihan == "3":
            mobil_id = int(input("Masukkan ID Mobil: "))
            mobil = service.read_mobil(mobil_id)
            if mobil:
                print(f"ID: {mobil.id} | Merk: {mobil.merk} | Tahun: {mobil.tahun} | Warna: {mobil.warna}")
            else:
                print("Mobil tidak ditemukan.")
        
        elif pilihan == "4":
            mobil_id = int(input("Masukkan ID Mobil yang akan diedit: "))
            data_baru = input_mobil()
            updated = service.edit_mobil(mobil_id, data_baru)
            if updated:
                print("Mobil berhasil diperbarui.")
            else:
                print("Mobil tidak ditemukan.")
        
        elif pilihan == "5":
            mobil_id = int(input("Masukkan ID Mobil yang akan dihapus: "))
            deleted = service.delete_mobil(mobil_id)
            if deleted:
                print("Mobil berhasil dihapus.")
            else:
                print("Mobil tidak ditemukan.")

        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break

if __name__ == "__main__":
    main()