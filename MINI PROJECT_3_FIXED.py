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

#    def sort(self, order='asc'):
#        if self.head is None or self.head.next_node is None:
#            return
#
#        self.head = self._quicksort(self.head, order)
#
#    def _quicksort(self, head, order):
#        if head is None or head.next_node is None:
#            return head
#
#        pivot, left, right = head, Node(None), Node(None)
#        left_head, right_head = left, right
#        current = head.next_node
#        pivot.next_node = None  # Detach pivot
#
#        while current:
#            next_node = current.next_node
#            current.next_node = None  # Detach current
#            if (order == 'asc' and current.data.brand < pivot.data.brand) or (order == 'desc' and current.data.brand > pivot.data.brand):
#                left.next_node = current
#                left = left.next_node
#            else:
#                right.next_node = current
#                right = right.next_node
#            current = next_node
#
#        left_head = self._quicksort(left_head.next_node, order)
#        right_head = self._quicksort(right_head.next_node, order)
#
#        return self._concatenate(left_head, pivot, right_head)
#
#    def _concatenate(self, left_head, pivot, right_head):
#        dummy = Node(None)
#        current = dummy
#
#        # Attach left part
#        while left_head:
#            current.next_node = left_head
#            left_head = left_head.next_node
#            current = current.next_node
#
#        # Attach pivot
#        current.next_node = pivot
#        current = current.next_node
#
#        # Attach right part
#        while right_head:
#            current.next_node = right_head
#            right_head = right_head.next_node
#            current = current.next_node
#
#        return dummy.next_node

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
def main():
    list_hp = LinkedList()
    print("Selamat Datang, Admin Toko HATSUNE CELL")
    while True:
        print("Menu:")
        print("1. Tambah HP")
        print("2. Tampilkan Seluruh HP")
        print("3. Sort HP")
        print("4. Edit HP")
        print("5. Hapus HP")
        print("6. Exit")
        pilih = int(input("Pilih Menu (1/2/3/4/5/6): "))
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
            print("Daftar HP sebelum diurutkan:")
            list_hp.print_list()
            print("1. Berdasarkan Kode HP\n2. Berdasarkan RAM HP")
            choice = int(input("Pilih Menu (1/2): "))
            if choice == 1:
                key_function = lambda hp: hp.kode
            elif choice == 2:
                key_function = lambda hp: int(hp.ram)  # Convert RAM to int for proper numeric sorting
            else:
                print("Pilihan tidak valid.")
                return

            order = input("Ingin diurutkan secara ascending atau descending? (asc/desc): ")
            
            list_hp.generic_sort(key=key_function, order=order)
            print("\nDaftar HP setelah diurutkan:")
            list_hp.print_list()
        elif pilih == 4:
            brand = input("Masukkan Brand HP yang Ingin Diubah = ")
            new_kode = input("Masukkan Kode HP Baru = ")
            new_brand = input("Masukkan Brand HP Baru = ")
            new_ram = input("Masukkan RAM HP Baru = ")
            new_rom = input("Masukkan Penyimpanan HP Baru = ")
            new_warna = input("Masukkan Warna HP Baru = ")
            list_hp.update(brand, new_kode, new_brand, new_ram, new_rom, new_warna)
        elif pilih == 5:
            brand = input("Masukkan Brand HP yang Ingin Dihapus = ")
            list_hp.delete(brand)
            print(f"HP dengan brand {brand} telah dihapus")
        elif pilih == 6:
            print("Terima Kasih")
            break
        else:
            print("Input Tidak Diketahui")

if __name__ == "__main__":
    main()
