class Produk:
    def __init__(self, id_produk: str, nama_produk: str, harga: float, stok: int):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.harga = harga
        self.stok = stok

    def display_info(self) -> str:
        return f"[ID: {self.id_produk}] {self.nama_produk} | Harga: Rp{self.harga:,.2f} | Stok: {self.stok}"

    def to_dict(self) -> dict:
        return {
            "id_produk": self.id_produk,
            "nama_produk": self.nama_produk,
            "harga": self.harga,
            "stok": self.stok
        }