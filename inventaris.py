from produk import Produk
from typing import Optional, List

class Inventaris:
    def __init__(self):
        # Key: id_produk (str), Value: Objek Produk
        self._data_produk: dict[str, Produk] = {}

    def tambah_produk(self, produk: Produk) -> bool:
        if produk.id_produk in self._data_produk:
            return False  # ID sudah ada
        self._data_produk[produk.id_produk] = produk
        return True

    def cari_produk(self, id_produk: str) -> Optional[Produk]:
        return self._data_produk.get(id_produk, None)

    def hapus_produk(self, id_produk: str) -> bool:
        if id_produk in self._data_produk:
            del self._data_produk[id_produk]
            return True
        return False

    def tampilkan_semua(self) -> List[Produk]:
        return list(self._data_produk.values())

    def total_produk(self) -> int:
        return len(self._data_produk)