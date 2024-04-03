print("=================Selamat Datang=================")
Menu = {"Nasi Goreng": 10000, "Ayam Bakar": 10000, "Seblak": 10000, "Es Teh": 5000, "Es Jeruk": 5000, "Teh Panas": 5000}
for item in Menu:
    print("Menu Warung : ", item, "\t", Menu[item])
print("================================================")
pembeli = input("Nama Pelanggan: ")
pesan = input("Menu Pesanan (pisahkan dengan koma): ").split(',')
jumlah_pesan = {}
for item in pesan:
    jumlah_pesan[item.strip()] = int(input(f"Jumlah pesanan untuk {item.strip()}: "))
total_pembayaran = 0
for item, jumlah in jumlah_pesan.items():
    total_pembayaran += jumlah * Menu[item]
pajak = total_pembayaran * 11 / 100
total_harga = total_pembayaran + pajak
print("PPN :", pajak)
print(f'Total : Rp.{total_harga}')
print("==================Terima Kasih==================")
