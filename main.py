import sys
from produk import Produk
from inventaris import Inventaris
from benchmark import jalankan_benchmark

def tampilkan_menu():
    print("\n=== SISTEM MANAJEMEN INVENTARIS PRODUK E-COMMERCE ===")
    print("1. Tambah Produk Baru")
    print("2. Cari Detail Produk (by ID)")
    print("3. Hapus Produk (by ID)")
    print("4. Tampilkan Semua Produk")
    print("5. Jalankan Benchmark Performa (Dict vs List)")
    print("6. Keluar")
    print("======================================================")

def main():
    sistem_inventaris = Inventaris()

    sistem_inventaris.tambah_produk(Produk("PRD-001", "Laptop Gaming", 15000000, 10))
    sistem_inventaris.tambah_produk(Produk("PRD-002", "Mouse Wireless", 250000, 50))
    sistem_inventaris.tambah_produk(Produk("PRD-003", "Keyboard Mechanical", 750000, 25))

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            print("\n--- TAMBAH PRODUK BARU ---")
            id_p = input("Masukkan ID Produk  : ").strip()
            nama = input("Masukkan Nama Produk: ").strip()
            try:
                harga = float(input("Masukkan Harga      : "))
                stok = int(input("Masukkan Jumlah Stok: "))
            except ValueError:
                print("Error: Harga dan stok harus berupa angka!")
                continue

            produk_baru = Produk(id_p, nama, harga, stok)
            if sistem_inventaris.tambah_produk(produk_baru):
                print("✓ Produk berhasil didaftarkan!")
            else:
                print("✕ Gagal: ID Produk sudah ada di sistem.")

        elif pilihan == "2":
            print("\n--- CARI DETAIL PRODUK ---")
            id_p = input("Masukkan ID Produk yang dicari: ").strip()
            produk = sistem_inventaris.cari_produk(id_p)
            if produk:
                print("✓ Produk Ditemukan:")
                print(produk.display_info())
            else:
                print("✕ Produk tidak ditemukan.")

        elif pilihan == "3":
            print("\n--- HAPUS PRODUK ---")
            id_p = input("Masukkan ID Produk yang akan dihapus: ").strip()
            if sistem_inventaris.hapus_produk(id_p):
                print("✓ Produk berhasil dihapus dari inventaris.")
            else:
                print("✕ Gagal: ID Produk tidak ditemukan.")

        elif pilihan == "4":
            print(f"\n--- DAFTAR INVENTARIS ({sistem_inventaris.total_produk()} Produk) ---")
            semua = sistem_inventaris.tampilkan_semua()
            if not semua:
                print("Inventaris kosong.")
            else:
                for p in semua:
                    print(p.display_info())

        elif pilihan == "5":
            try:
                n = input("Masukkan jumlah data simulasi (default 100,000): ").strip()
                n = int(n) if n else 100_000
                jalankan_benchmark(n)
            except ValueError:
                print("Masukkan angka yang valid.")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan Sistem Inventaris.")
            sys.exit(0)

        else:
            print("Pilihan menu tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()