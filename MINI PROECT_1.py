global Handphone
global brand_baru
global ram_baru
global rom_baru
global warna_baru
loop = "y"
Handphone = []

class HP:
    def __init__(self,brand , ram, rom, warna):
        self.brand = brand
        self.ram = ram
        self.rom = rom
        self.warna = warna
    def create(self, brand_baru, ram_baru, rom_baru, warna_baru):
        self.brand_baru = brand_baru
        self.ram_baru = ram_baru
        self.rom_baru = rom_baru
        self.warna_baru = warna_baru
        print("Anda Berhasil Menambah HP Baru")
    def read(self):
        print(Handphone)
    def update(self, brand_up, ram_up, rom_up,warna_up):
        self.brand_up = brand_up
        self.ram_up = ram_up
        self.rom_up = rom_up
        self.warna_up = warna_up
        print("Anda Berhasil Mengubah HP")
    def delete(self,brand_del):
        self.brand_del = brand_del
        print("Anda Berhasil Menghapus HP")

def main():
    while loop == "y":
        print("Selamat Datang, Admin Toko HATSUNE CELL")
        print("1. Tambah HP")
        print("2. Tampilkan Seluruh HP")
        print("3. Edit HP")
        print("4. Hapus HP")
        print("5. Exit")
        pilih = int(input("Pilih Menu (1/2/3/4/5) = "))
        if pilih == 1:
            brand_baru = input("Masukkan Brand HP = ")
            ram_baru = input("Masukkan RAM HP = ")
            rom_baru = input("Masukkan Penyimpanan HP = ")
            warna_baru = input("Masukkan Warna HP = ")
            Handphone.append([brand_baru, ram_baru, rom_baru, warna_baru])
            HP(1,2,3,4).create(brand_baru, ram_baru, rom_baru, warna_baru)
        elif pilih == 2:
            HP(1,2,3,4).read()
        elif pilih == 3:
            global brand_up
            global ram_up
            global rom_up
            global warna_up
            edit = int(input("Masukkan Index Keberapa yang Ingin Diubah (List Pertama = Index 0) = "))
            brand_up = input("Masukkan Brand HP yang Ingin Diubah = ")
            ram_up = input("Masukkan RAM HP Baru = ")
            rom_up = input("Masukkan Pemnyimpanan HP Baru = ")
            warna_up = input("Masukkan Warna HP Baru = ")
            Handphone.pop(edit)
            Handphone.append([brand_up, ram_up, rom_up, warna_up])
            HP(1,2,3,4).update(brand_up, ram_up, rom_up, warna_up)
        elif pilih == 4:
            hapus = int(input("Masukkan Index Keberapa yang Ingin Hapus (List Pertama = Index 0) = "))
            brand_del = input("Masukkan Brand HP yang Ingin Dihapus = ")
            Handphone.pop(hapus)
            HP(1,2,3,4).delete(brand_del)
        elif pilih == 5:
            print("Terima Kasih")
            break
        else:
            print("Input Tidak Diketahui")
            break
main()