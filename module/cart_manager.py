import csv
from datetime import datetime
from queue import Queue

def keranjang_belanja(antrian):
    if antrian.empty():
        print("Keranjang belanja kosong.")
        return

    print("Keranjang Belanja:")
    print("======================")
    temp_list = []
    total_transaksi = 0

    while not antrian.empty():
        item = antrian.get()
        temp_list.append(item)

    for idx, item in enumerate(temp_list, start=1):
        total_harga = item['harga'] * item['jumlah']
        total_transaksi += total_harga
        print(f"{idx}. ID: {item['id']}, Nama: {item['nama']}, Harga satuan: {item['harga']}, Jumlah: {item['jumlah']}, Total Harga: {total_harga}")

    for item in temp_list:
        antrian.put(item)

    print("======================")
    print(f"Total Harga Keseluruhan: Rp.{total_transaksi}\n")
    print("======================")
    print("1. Konfirmasi")
    print("2. Hapus Salah Satu Produk")
    print("======================")
    print("9. Kembali")
    pilihan = input("Pilih menu: ")
    print("")

    if pilihan == "1":
        konfirmasi_transaksi(antrian)
    elif pilihan == "2":
        baris_produk = int(input("Masukkan nomor baris produk yang ingin dihapus: "))
        if 1 <= baris_produk <= len(temp_list):
            item_dihapus = temp_list.pop(baris_produk - 1)
            print(f"Produk baris {baris_produk} berhasil dihapus dari keranjang.")
            antrian.queue.clear()
            for item in temp_list:
                antrian.put(item)
            keranjang_belanja(antrian)
        else:
            print("Nomor baris produk tidak valid.")
            keranjang_belanja(antrian)

def konfirmasi_transaksi(antrian):
    produk_pistol = baca_data('data_produk_pistol.csv', 'pistol')
    produk_smg = baca_data('data_produk_smg.csv', 'smg')
    produk_shotgun = baca_data('data_produk_shotgun.csv', 'shotgun')
    produk_sniper_rifle = baca_data('data_produk_sniper_rifle.csv', 'sniper_rifle')
    produk_assault_rifle = baca_data('data_produk_assault_rifle.csv', 'assault_rifle')
    produk_throwable = baca_data_throwable('data_produk_throwable.csv', 'throwable')
    produk_equip = baca_data_equip('data_produk_equip.csv', 'equip')
    produk_ammo = baca_data_ammo('data_produk_ammo.csv', 'ammo')

    produk = (
        produk_pistol + produk_smg + produk_shotgun + produk_sniper_rifle +
        produk_assault_rifle + produk_throwable + produk_equip + produk_ammo
    )
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    nota_filename = f'Nota_Pembelian_{timestamp}.txt'
    
    total_transaksi = 0
    
    with open('data_transaksi.csv', mode='a', newline='') as file_csv, open(nota_filename, mode='a') as file_txt:
        writer_csv = csv.writer(file_csv)
        file_txt.write("======================== Nota Pembelian ========================\n")
        
        while not antrian.empty():
            item = antrian.get()
            jenis_senjata = item['jenis']
            total_harga = item['harga'] * item['jumlah']
            total_transaksi += total_harga
            tahun_transaksi = datetime.now().strftime('%Y')
            bulan_transaksi = datetime.now().strftime('%m')
            hari_transaksi = datetime.now().strftime('%d')
            detail_transaksi = datetime.now().strftime('%H:%M:%S')
            waktu_transaksi = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            writer_csv.writerow([
                item['id'], 
                jenis_senjata, 
                item.get('jenis_peluru', ''),
                item['nama'], 
                item['harga'], 
                item['jumlah'], 
                total_harga, 
                tahun_transaksi,
                bulan_transaksi,
                hari_transaksi,
                detail_transaksi
            ])
            
            file_txt.write(f"ID: {item['id']}, {jenis_senjata}, {item.get('jenis_peluru', '')}, {item['nama']}, Rp.{item['harga']}, {item['jumlah']}, Total Harga: Rp.{total_harga}, Waktu: {waktu_transaksi}\n")

            for produk_item in produk:
                if produk_item['id'] == item['id'] and produk_item['jenis'] == item['jenis']:
                    produk_item['stok'] -= item['jumlah']
                    break

        file_txt.write("===============================================================\n")
        file_txt.write(f"Total Harga Keseluruhan: Rp.{total_transaksi}\n")

    write_data('data_produk_pistol.csv', [p for p in produk if p['jenis'] == 'pistol'], 'pistol')
    write_data('data_produk_smg.csv', [p for p in produk if p['jenis'] == 'smg'], 'smg')
    write_data('data_produk_shotgun.csv', [p for p in produk if p['jenis'] == 'shotgun'], 'shotgun')
    write_data('data_produk_sniper_rifle.csv', [p for p in produk if p['jenis'] == 'sniper_rifle'], 'sniper_rifle')
    write_data('data_produk_assault_rifle.csv', [p for p in produk if p['jenis'] == 'assault_rifle'], 'assault_rifle')
    write_data('data_produk_throwable.csv', [p for p in produk if p['jenis'] == 'throwable'], 'throwable')
    write_data('data_produk_equip.csv', [p for p in produk if p['jenis'] == 'equip'], 'equip')
    write_data('data_produk_ammo.csv', [p for p in produk if p['jenis'] == 'ammo'], 'ammo')

    print("Transaksi berhasil dikonfirmasi.")
    print("Keranjang belanja dikosongkan.")
    
def baca_data(file_csv, jenis):
    produk = []
    with open(file_csv, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            produk.append({
                'id': int(row[0]),
                'jenis_peluru': row[1],
                'nama': row[2],
                'harga': float(row[3]),
                'stok': int(row[4]),
                'jenis': jenis
            })
    return produk

def baca_data_throwable(file_csv, jenis):
    produk = []
    with open(file_csv, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            produk.append({
                'id': int(row[0]),
                'jenis_throwable': row[1],
                'nama': row[2],
                'harga': float(row[3]),
                'stok': int(row[4]),
                'jenis': jenis
            })
    return produk

def baca_data_equip(file_csv, jenis):
    produk = []
    with open(file_csv, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            produk.append({
                'id': int(row[0]),
                'jenis_equip': row[1],
                'nama': row[2],
                'harga': float(row[3]),
                'stok': int(row[4]),
                'jenis': jenis
            })
    return produk

def baca_data_ammo(file_csv, jenis):
    produk = []
    with open(file_csv, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            produk.append({
                'id': int(row[0]),
                'jenis_peluru': row[1],
                'merk': row[2],
                'harga': float(row[3]),
                'stok': int(row[4]),
                'jenis': jenis
            })
    return produk

def write_data(file_csv, produk, jenis):
    with open(file_csv, mode='w', newline='') as file:
        if jenis == 'ammo':
            writer = csv.writer(file)
            writer.writerow(['id', 'jenis_peluru', 'merk', 'harga', 'stok', 'jenis'])
            for item in produk:
                writer.writerow([item['id'], item['jenis_peluru'], item['merk'], item['harga'], item['stok'], item['jenis']])
        elif jenis == 'throwable':
            writer = csv.writer(file)
            writer.writerow(['id', 'jenis_throwable', 'nama', 'harga', 'stok', 'jenis'])
            for item in produk:
                writer.writerow([item['id'], item['jenis_throwable'], item['nama'], item['harga'], item['stok'], item['jenis']])
        elif jenis == 'equip':
            writer = csv.writer(file)
            writer.writerow(['id', 'jenis_equip', 'nama', 'harga', 'stok', 'jenis'])
            for item in produk:
                writer.writerow([item['id'], item['jenis_equip'], item['nama'], item['harga'], item['stok'], item['jenis']])
        else:
            writer = csv.writer(file)
            writer.writerow(['id', 'jenis_peluru', 'nama', 'harga', 'stok', 'jenis'])
            for item in produk:
                writer.writerow([item['id'], item['jenis_peluru'], item['nama'], item['harga'], item['stok'], item['jenis']])
