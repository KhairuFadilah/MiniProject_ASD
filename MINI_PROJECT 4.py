global Handphone
Handphone = ['Xiaomi','Iphone','Poco','Vivo']
Ram = [2,3,4,8]
class HP():
    def __init__(self, kode, brand , ram, rom, warna):
        self.kode = kode
        self.brand = brand
        self.ram = ram
        self.rom = rom
        self.warna = warna
    def create(self, brand, ram, rom, warna):
        self.brand = brand
        self.ram = ram
        self.rom = rom
        self.warna = warna
        print("Anda Berhasil Menambah HP Baru")
    def read(self):
        print(Handphone)
    def update(self, brand, ram, rom,warna):
        self.brand_up = brand
        self.ram_up = ram
        self.rom_up = rom
        self.warna_up = warna
        print("Anda Berhasil Mengubah HP")
    def delete(self,brand):
        self.brand = brand
        print("Anda Berhasil Menghapus HP")
    def jump_search(self, arr, x):
        n = len(arr)
        step = int(n **0.5)

        prev = 0
        while arr[min(step, n) - 1] < x:
            prev = step
            step += int(n **0.5)
            if prev >= n:
                return -1
        while arr[prev] < x:
            prev += 1

            if prev == min(step, n):
                return -1
        if arr[prev] == x:
            return prev
        return -1
class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d
    def has_next(self):
        if self.get_next() is None:
            return False
        return True
    def to_string(self):
        return "Node value: " + str(self.get_data())
class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = Node(d, self.root)
        if self.root == None:
            self.root = new_node
            self.size += 1
        else:
            current = self.root
            while current.next_node:
                current = current.next_node
            current.next_node = Node(d, self.root)
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()
        return False
    def print_list(self):
        print("Print List..........")
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())
            break
def quickSort1(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        
        less_than_pivot = [x for x in data [1:] if x <= pivot]
        greater_than_pivot = [x for x in data[1:] if x > pivot]
        
        return quickSort1(less_than_pivot) + [pivot] + quickSort1(greater_than_pivot)
def quickSort2(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        
        greater_than_pivot = [x for x in data[1:] if x > pivot]
        less_than_pivot = [x for x in data [1:] if x <= pivot]
        
        return quickSort2(greater_than_pivot) + [pivot] + quickSort2(less_than_pivot)
def main():
    list_hp = LinkedList()
    while True:
        print("Selamat Datang, Admin Toko HATSUNE CELL")
        print("1. Tambah HP")
        print("2. Tampilkan Seluruh HP")
        print("3. Cari HP")
        print("4. Urutkan HP")
        print("5. Edit HP")
        print("6. Hapus HP")
        print("7. Exit")
        pilih = int(input("Pilih Menu (1/2/3/4/5/6/7) = "))
        if pilih == 1:
            kode = input("Masukkan Kode HP = ")
            brand = input("Masukkan Brand HP = ")
            ram = input("Masukkan RAM HP = ")
            rom = input("Masukkan Penyimpanan HP = ")
            warna = input("Masukkan Warna HP = ")
            list_hp.add([kode, brand, ram, rom, warna])
        elif pilih == 2:
            list_hp.print_list()
        elif pilih == 3:
            print("1. Cari Berdasarkan Nama")
            print("2. Cari Berdasarkan RAM HP")
            pilih2 = int(input("Pilih Menu (1/2) = "))
            if pilih2 == 1:
                x = input("Masukkan Nama HP yang ingin dicari = ")
                HP(1,2,3,4,5).jump_search(x, Handphone)
            elif pilih2 == 2:
                x = input("Masukkan RAM HP yang ingin dicari = ")
                HP(1,2,3,4,5).jump_search(x, Ram)
        elif pilih == 4:
            print("1. A > Z")
            print("2. Z > A")
            piliih2 = int(input("Pilih Menu (1/2) = "))
            if piliih2 == 1:
                data = Handphone()
                hasil = quickSort1(data)
                print(hasil)
            elif piliih2 == 2:
                data = Handphone()
                hasil = quickSort2(data)
                print(hasil)
        elif pilih == 5:
            kode = input("Masukkan Kode HP yang Ingin Diubah (Kode 001 = Index 0) = ")
            brand = input("Masukkan Brand HP Baru = ")
            ram = input("Masukkan RAM HP Baru = ")
            rom = input("Masukkan Pemnyimpanan HP Baru = ")
            warna = input("Masukkan Warna HP Baru = ")
            list_hp.remove([kode, brand, ram, rom, warna])
            print("Please Wait...")
            list_hp.add([kode, brand, ram, rom, warna])
            print("Success")
        elif pilih == 6:
            kode = int(input("Masukkan Kode HP yang Ingin Dihapus = "))
            brand = input("Masukkan Brand HP yang Ingin Dihapus = ")
            list_hp.remove([kode, brand, ram, rom, warna])
        elif pilih == 7:
            print("Terima Kasih")
            break
        else:
            print("Input Tidak Diketahui")
            break
main()