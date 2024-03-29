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

    def generic_sort(self, key=lambda x: x, order='asc'):
        if self.head is None or self.head.next_node is None:
            return

        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next_node
            
        arr.sort(key=key, reverse=(order == 'desc'))
        
        self.head = None
        for item in arr:
            self.add(item)

    def find_all_matches(self, attribute, value):
        matches = []
        current = self.head
        while current:
            if str(getattr(current.data, attribute)) == str(value):
                matches.append(current.data)
            current = current.next_node
        return matches

def main():
    list_hp = LinkedList()
    list_hp.add(HP('01', 'Xiaomi', '3', '32', 'Red'))
    list_hp.add(HP('02', 'iPhone', '4', '64', 'Blue'))
    list_hp.add(HP('03', 'POCO', '8', '256', 'Silver'))
    list_hp.add(HP('04', 'Samsung', '8', '512', 'Gold'))
    list_hp.add(HP('05', 'OPPO', '2', '16', 'Purple'))
    print("Selamat Datang, Admin Toko HATSUNE CELL")
    while True:
        print("Menu:")
        print("1. Search HP")
        print("2. Tambah HP Baru")
        print("3. Tampilkan List HP")
        print("4. Sort List HP")
        print("5. Edit HP")
        print("6. Hapus HP")
        print("7. Exit")
        pilih = int(input("Pilih Menu (1/2/3/4/5/6/7): "))
        if pilih == 1:
            print("1. Berdasarkan Brand HP\n2. Berdasarkan RAM HP")
            choice = int(input("Pilih Menu (1/2): "))
            if choice == 1:
                list_hp.generic_sort(key=lambda hp: hp.brand, order='asc')
                cari_brand = input("Masukkan Brand HP = ")
                matching_hps = list_hp.find_all_matches('brand', cari_brand)
                if matching_hps:
                    print(f"Found {len(matching_hps)} HP(s) with {cari_brand}:")
                    for hp in matching_hps:
                        print(f"Kode: {hp.kode}, Brand: {hp.brand}, RAM: {hp.ram}, ROM: {hp.rom}, Warna: {hp.warna}")
                else:
                    print("HP not found.")
            elif choice == 2:
                list_hp.generic_sort(key=lambda hp: int(hp.ram), order='asc')
                cari_ram = input("Masukkan RAM HP = ")
                matching_hps = list_hp.find_all_matches('ram', cari_ram)
                if matching_hps:
                    print(f"Found {len(matching_hps)} HP(s) with {cari_ram}GB RAM:")
                    for hp in matching_hps:
                        print(f"Kode: {hp.kode}, Brand: {hp.brand}, RAM: {hp.ram}, ROM: {hp.rom}, Warna: {hp.warna}")
                else:
                    print("HP not found.")
            else:
                print("Pilihan tidak valid.")
        elif pilih == 2:
            kode = input("Masukkan Kode HP = ")
            brand = input("Masukkan Brand HP = ")
            ram = input("Masukkan RAM HP = ")
            rom = input("Masukkan Penyimpanan HP = ")
            warna = input("Masukkan Warna HP = ")
            hp = HP(kode, brand, ram, rom, warna)
            list_hp.add(hp)
            print("Anda Berhasil Menambah HP Baru")
        elif pilih == 3:
            print("Daftar HP:")
            list_hp.print_list()
        elif pilih == 4:
            print("Daftar HP sebelum diurutkan:")
            list_hp.print_list()
            print("1. Berdasarkan Penyimpanan HP\n2. Berdasarkan RAM HP")
            choice = int(input("Pilih Menu (1/2): "))
            if choice == 1:
                key_function = lambda hp: int(hp.rom)
            elif choice == 2:
                key_function = lambda hp: int(hp.ram)  # Convert RAM to int for proper numeric sorting
            else:
                print("Pilihan tidak valid.")
                return
            
            order = input("Ingin diurutkan secara ascending atau descending? (asc/desc): ")
            
            list_hp.generic_sort(key=key_function, order=order)
            print("\nDaftar HP setelah diurutkan:")
            list_hp.print_list()
        elif pilih == 5:
            brand = input("Masukkan Brand HP yang Ingin Diubah = ")
            new_kode = input("Masukkan Kode HP Baru = ")
            new_brand = input("Masukkan Brand HP Baru = ")
            new_ram = input("Masukkan RAM HP Baru = ")
            new_rom = input("Masukkan Penyimpanan HP Baru = ")
            new_warna = input("Masukkan Warna HP Baru = ")
            list_hp.update(brand, new_kode, new_brand, new_ram, new_rom, new_warna)
        elif pilih == 6:
            brand = input("Masukkan Brand HP yang Ingin Dihapus = ")
            list_hp.delete(brand)
            print(f"HP dengan brand {brand} telah dihapus")
        elif pilih == 7:
            print("Terima Kasih")
            break
        else:
            print("Input Tidak Diketahui")

if __name__ == "__main__":
    main()