from produk import Produk
from typing import Optional

class Node:
    def __init__(self, data: Produk):
        self.data = data
        self.next: Optional['Node'] = None

class LinkedListInventaris:
    def __init__(self):
        self.head: Optional[Node] = None
        self._length = 0

    def tambah_produk(self, produk: Produk) -> bool:
        new_node = Node(produk)
        new_node.next = self.head
        self.head = new_node
        self._length += 1
        return True

    def cari_produk(self, id_produk: str) -> Optional[Produk]:
        current = self.head
        while current:
            if current.data.id_produk == id_produk:
                return current.data
            current = current.next
        return None

    def hapus_produk(self, id_produk: str) -> bool:
        current = self.head
        prev = None

        while current:
            if current.data.id_produk == id_produk:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self._length -= 1
                return True
            prev = current
            current = current.next
        return False