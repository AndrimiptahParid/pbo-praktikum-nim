class buku:
    pass

b = buku()
b.judul = "contoh judul"
b.penulis = "contoh penulis"
print(b.judul, "-", b.penulis)


class Buku:
    def __init__(self, judul, tahun_terbit, penulis="tidak di ketahui"):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penulis = penulis
 
    def info(self):
        print(f"Judul   : {self.judul}")
        print(f"Tahun Terbit : {self.tahun_terbit}")
        print(f"Penulis : {self.penulis}")
        
buku1 = Buku("Dasar Pemrograman Python", "2004")
buku2 = Buku("Struktur Data", "2005")
buku3 = Buku("Basis Data", "2006")
 
buku1.info()
buku2.info()
buku3.info()