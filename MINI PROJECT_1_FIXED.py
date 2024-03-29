import csv
from prettytable import from_csv
filename_csv = 'MINI PROJECT_1_FIXED.csv'
class HP(object):
    def __init__(self,kode, brand , ram, rom, warna):
        self.kode = kode
        self.brand = brand
        self.ram = ram
        self.rom = rom
        self.warna = warna
    def add(self):
        kode = input("Masukkan Kode HP = ")
        brand = input("Masukkan Brand HP = ")
        ram = input("Masukkan RAM HP = ")
        rom = input("Masukkan Penyimpanan HP = ")
        warna = input("Masukkan Warna HP = ")
        addon = [kode, brand, ram, rom, warna]
        with open(filename_csv, "r") as infile:
            reader = list(csv.reader(infile))
            reader.append(addon)
            
        with open(filename_csv, "w", newline='') as outfile:
            writer = csv.writer(outfile)
            for line in reader:
                writer.writerow(line)
        print("Success")
    def print(self):
        with open (filename_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print(csv_reader)
            for code in csv_reader:
                code = from_csv(csv_file)
                print(code)
    def update(self):
        update = []
        with open(filename_csv, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                update.append(row)
            for data in update:
                    print("-----------------------")
                    kode = input("Pilih Kode yang ingin diubah> ")
                    brand = input("Brand baru: ")
                    ram = input("RAM baru: ")
                    rom = input("Penyimpanan baru: ")
                    warna = input("Warna baru: ")
                    indeks = 0
                    for data in update:
                        if (data['Kode'] == kode):
                            update[indeks]['Brand'] = brand
                            update[indeks]['RAM'] = ram
                            update[indeks]['ROM'] = rom
                            update[indeks]['Warna'] = warna                                
                        indeks = indeks + 1
                    with open(filename_csv, mode="w", newline='') as csv_file:
                        fieldnames = ['Kode','Brand','RAM','ROM','Warna']
                        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                        writer.writeheader()
                        for new_data in update:
                            writer.writerow({'Kode': new_data['Kode'], 'Brand': new_data['Brand'], 'RAM': new_data['RAM'], 'ROM': new_data['ROM'], 'Warna': new_data['Warna']})
                    break
            print("Success")
    def delete(self):
        delete = []
        with open(filename_csv, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                delete.append(row)
            for data in delete:
                print(f"{data['Kode']} \t {data['Brand']} \t {data['RAM']} \t {data['ROM']} \t {data['Warna']}")
            print("-----------------------")
            kode = input("Hapus Kode> ")
            indeks = 0
            for data in delete:
                if (data['Kode'] == kode):
                    delete.remove(delete[indeks])
                    indeks = indeks + 1
                with open(filename_csv, mode="w", newline='') as csv_file:
                    fieldnames = ['Kode', 'Brand', 'RAM', 'ROM', 'Warna']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in delete:
                        writer.writerow({'Kode': new_data['Kode'], 'Brand': new_data['Brand'], 'RAM': new_data['RAM'], 'ROM': new_data['ROM'], 'Warna': new_data['Warna']})
                    break
            print("Success")
def main():
    while True:
        handphone = HP(1,2,3,4,5)
        print("Selamat Datang, Admin Toko HATSUNE CELL")
        print("1. Tambah HP")
        print("2. Tampilkan Seluruh HP")
        print("3. Edit HP")
        print("4. Hapus HP")
        print("5. Exit")
        pilih = int(input("Pilih Menu (1/2/3/4/5) = "))
        if pilih == 1:
            handphone.add()
        elif pilih == 2:
            handphone.print()
        elif pilih == 3:
            handphone.update()
        elif pilih == 4:
            handphone.delete()
        elif pilih == 5:
            print("Terima Kasih")
            return False
        else:
            print("Input Tidak Diketahui")
            return False
main()