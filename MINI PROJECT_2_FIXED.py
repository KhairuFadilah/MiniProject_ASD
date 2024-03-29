class HP:
    def __init__(self, kode, brand, ram, rom, warna):
        self.kode = kode
        self.brand = brand
        self.ram = ram
        self.rom = rom
        self.warna = warna

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def delete(self, brand):
        current = self.head
        if current.data.brand == brand:
            self.head = current.next_node
            return
        prev = None
        while current:
            if current.data.brand == brand:
                prev.next_node = current.next_node
                return
            prev = current
            current = current.next_node

    def update(self, brand, new_kode, new_brand, new_ram, new_rom, new_warna):
        current = self.head
        while current:
            if current.data.brand == brand:
                current.data.kode = new_kode
                current.data.brand = new_brand
                current.data.ram = new_ram
                current.data.rom = new_rom
                current.data.warna = new_warna
                return
            current = current.next_node
        print(f"HP dengan brand {brand} tidak ditemukan")

    def print_list(self):
        current = self.head
        while current:
            hp = current.data
            print(f"Kode: {hp.kode}, Brand: {hp.brand}, RAM: {hp.ram}, ROM: {hp.rom}, Warna: {hp.warna}")
            current = current.next_node

def main():
    list_hp = LinkedList()
    print("Selamat Datang, Admin Toko HATSUNE CELL")
    while True:
        print("Menu:")
        print("1. Tambah HP")
        print("2. Tampilkan Seluruh HP")
        print("3. Edit HP")
        print("4. Hapus HP")
        print("5. Exit")
        pilih = int(input("Pilih Menu (1/2/3/4/5): "))
        if pilih == 1:
            kode = input("Masukkan Kode HP = ")
            brand = input("Masukkan Brand HP = ")
            ram = input("Masukkan RAM HP = ")
            rom = input("Masukkan Penyimpanan HP = ")
            warna = input("Masukkan Warna HP = ")
            hp = HP(kode, brand, ram, rom, warna)
            list_hp.add(hp)
            print("Anda Berhasil Menambah HP Baru")
        elif pilih == 2:
            print("Daftar HP:")
            list_hp.print_list()
        elif pilih == 3:
            brand = input("Masukkan Brand HP yang Ingin Diubah = ")
            new_kode = input("Masukkan Kode HP Baru = ")
            new_brand = input("Masukkan Brand HP Baru = ")
            new_ram = input("Masukkan RAM HP Baru = ")
            new_rom = input("Masukkan Penyimpanan HP Baru = ")
            new_warna = input("Masukkan Warna HP Baru = ")
            list_hp.update(brand, new_kode, new_brand, new_ram, new_rom, new_warna)
        elif pilih == 4:
            brand = input("Masukkan Brand HP yang Ingin Dihapus = ")
            list_hp.delete(brand)
            print(f"HP dengan brand {brand} telah dihapus")
        elif pilih == 5:
            print("Terima Kasih")
            break
        else:
            print("Input Tidak Diketahui")

if __name__ == "__main__":
    main()
