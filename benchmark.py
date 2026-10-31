import time
from produk import Produk
from inventaris import Inventaris
from linked_list import LinkedListInventaris

def jalankan_benchmark(jumlah_data: int = 100_000):
    print(f"\n==================================================")
    print(f" BENCHMARK 3 STRUKTUR DATA ({jumlah_data:,} DATA)")
    print(f"==================================================")
    dict_inv = Inventaris()              
    list_inv: list[Produk] = []          
    ll_inv = LinkedListInventaris()      

    print("Membuat data dummy...")
    for i in range(jumlah_data):
        p = Produk(id_produk=f"PRD-{i:07d}", nama_produk=f"Barang {i}", harga=10000 + i, stok=50)
        dict_inv.tambah_produk(p)
        list_inv.append(p)
        ll_inv.tambah_produk(p)

    target_id = "PRD-0000000"

    print("\n--- 1. Pengujian Operasi Pencarian (Search) ---")
    
    t0 = time.perf_counter()
    dict_inv.cari_produk(target_id)
    t_dict_search = time.perf_counter() - t0
    print(f"1. Hash Table (dict) : {t_dict_search:.8f} detik [O(1)]")

    t0 = time.perf_counter()
    next((p for p in list_inv if p.id_produk == target_id), None)
    t_list_search = time.perf_counter() - t0
    print(f"2. Array List (list) : {t_list_search:.8f} detik [O(n)]")

    t0 = time.perf_counter()
    ll_inv.cari_produk(target_id)
    t_ll_search = time.perf_counter() - t0
    print(f"3. Linked List (ADT) : {t_ll_search:.8f} detik [O(n)]")
    print("\n--- 2. Pengujian Operasi Penghapusan (Delete) ---")
    
    t0 = time.perf_counter()
    dict_inv.hapus_produk(target_id)
    t_dict_del = time.perf_counter() - t0
    print(f"1. Hash Table (dict) : {t_dict_del:.8f} detik [O(1)]")

    t0 = time.perf_counter()
    for idx, p in enumerate(list_inv):
        if p.id_produk == target_id:
            del list_inv[idx]
            break
    t_list_del = time.perf_counter() - t0
    print(f"2. Array List (list) : {t_list_del:.8f} detik [O(n)]")

    t0 = time.perf_counter()
    ll_inv.hapus_produk(target_id)
    t_ll_del = time.perf_counter() - t0
    print(f"3. Linked List (ADT) : {t_ll_del:.8f} detik [O(n)]")

    print("\n==================================================\n")

if __name__ == "__main__":
    jalankan_benchmark()