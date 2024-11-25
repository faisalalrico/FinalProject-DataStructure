import csv
from datetime import datetime, timedelta
from module import product_list_viewer

def tambah_produk(produk, jenis):
    id_baru = len(produk) + 1
    jenis_item = ''
    if jenis in ['pistol', 'smg', 'shotgun', 'sniper_rifle', 'assault_rifle', 'ammo']:
        jenis_item = 'jenis_peluru'
    elif jenis == 'equip':
        jenis_item = 'jenis_equip'
    elif jenis == 'throwable':
        jenis_item = 'jenis_throwable'
    
    jenis_peluru = input(f"Masukkan {jenis_item} {jenis}: ")
    nama = input(f"Masukkan nama {jenis}: ")
    harga = float(input(f"Masukkan harga {jenis}: "))
    stok = int(input(f"Masukkan stok {jenis}: "))
    produk_baru = {'id': id_baru, jenis_item: jenis_peluru, 'nama': nama, 'harga': harga, 'stok': stok, 'jenis': jenis}
    produk.append(produk_baru)
    simpan_data(f'data_produk_{jenis}.csv', produk)
    print(f"{jenis.capitalize()} baru telah ditambahkan.")

def hapus_produk(produk, jenis):
    if jenis in ['pistol', 'smg', 'shotgun', 'sniper_rifle', 'assault_rifle']:
        product_list_viewer.tampilkan_produk(produk, jenis)
    elif jenis == 'equip':
        product_list_viewer.tampilkan_produk_equip(produk)
    elif jenis == 'throwable':
        product_list_viewer.tampilkan_produk_throwable(produk)
    elif jenis == 'ammo':
        product_list_viewer.tampilkan_produk_ammo(produk)
    else:
        print("Jenis produk tidak valid.")
        return

    print("======================")
    print("0. Untuk Kembali")
    print("======================")
    id_hapus = int(input(f"Masukkan ID {jenis} yang ingin dihapus: "))
    
    if id_hapus == 0:
        return
    
    produk_dihapus = [p for p in produk if p['jenis'] == jenis and p['id'] == id_hapus]
    if produk_dihapus:
        produk.remove(produk_dihapus[0])
        produk = urutkan_id(produk, jenis)
        simpan_data(f'data_produk_{jenis}.csv', produk)
        print(f"{jenis.capitalize()} dengan ID {id_hapus} telah dihapus.")
    else:
        print(f"{jenis.capitalize()} dengan ID {id_hapus} tidak ditemukan.")

def atur_stok(produk, jenis):
    if jenis in ['pistol', 'smg', 'shotgun', 'sniper_rifle', 'assault_rifle']:
        product_list_viewer.tampilkan_produk(produk, jenis)
    elif jenis == 'equip':
        product_list_viewer.tampilkan_produk_equip(produk)
    elif jenis == 'throwable':
        product_list_viewer.tampilkan_produk_throwable(produk)
    elif jenis == 'ammo':
        product_list_viewer.tampilkan_produk_ammo(produk)
    else:
        print("Jenis produk tidak valid.")
        return

    print("======================")
    print("0. Untuk Kembali")
    print("======================")

    id_atur = int(input(f"Masukkan ID {jenis} yang ingin diatur stoknya: "))
    produk_ditemukan = [p for p in produk if p['jenis'] == jenis and p['id'] == id_atur]
    if produk_ditemukan:
        stok_baru = int(input(f"Masukkan stok baru untuk {jenis} dengan ID {id_atur}: "))
        produk_ditemukan[0]['stok'] = stok_baru
        simpan_data(f'data_produk_{jenis}.csv', produk)
        print(f"Stok {jenis.capitalize()} dengan ID {id_atur} telah diatur ulang.")
    else:
        print(f"{jenis.capitalize()} dengan ID {id_atur} tidak ditemukan.")

def urutkan_id(produk, jenis):
    id_baru = 1
    for item in produk:
        if item['jenis'] == jenis:
            item['id'] = id_baru
            id_baru += 1
    return produk

def baca_data_transaksi(file_csv):
    transaksi = []
    try:
        with open(file_csv, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                transaksi.append({
                    'id': int(row[0]),
                    'jenis_senjata': row[1],
                    'jenis_peluru': row[2],
                    'nama': row[3],
                    'harga': float(row[4]),
                    'jumlah': int(row[5]),
                    'total_harga': float(row[6]),
                    'tahun': int(row[7]),
                    'bulan': int(row[8]),
                    'hari': int(row[9]),
                    'detail_waktu': row[10]
                })
    except FileNotFoundError:
        print(f"File {file_csv} tidak ditemukan.")
    return transaksi

def hitung_total_hari_ini(transaksi):
    hasil_hari_ini = 0
    hari_ini = datetime.now().date()
    for trans in transaksi:
        tanggal = datetime(trans['tahun'], trans['bulan'], trans['hari']).date()
        if tanggal == hari_ini:
            hasil_hari_ini += trans['total_harga']
    return hasil_hari_ini

def hitung_total_mingguan(transaksi):
    hasil_mingguan = 0
    tanggal_sekarang = datetime.now().date()
    batas_waktu = tanggal_sekarang - timedelta(days=7)
    
    for trans in transaksi:
        tanggal = datetime(trans['tahun'], trans['bulan'], trans['hari']).date()
        if batas_waktu <= tanggal <= tanggal_sekarang:
            hasil_mingguan += trans['total_harga']
    return hasil_mingguan

def hitung_total_bulanan(transaksi):
    hasil_bulanan = {}
    for trans in transaksi:
        bulan = f"{trans['tahun']}-{trans['bulan']:02d}"
        if bulan not in hasil_bulanan:
            hasil_bulanan[bulan] = 0
        hasil_bulanan[bulan] += trans['total_harga']
    return hasil_bulanan

def hitung_total_tahunan(transaksi):
    hasil_tahunan = {}
    for trans in transaksi:
        tahun = trans['tahun']
        if tahun not in hasil_tahunan:
            hasil_tahunan[tahun] = 0
        hasil_tahunan[tahun] += trans['total_harga']
    return hasil_tahunan

def tampilkan_hasil(hasil, periode):
    print("===============================")
    if isinstance(hasil, dict):
        print(f"Hasil total perhitungan transaksi {periode.capitalize()} ialah:")
        for key, value in hasil.items():
            print(f"{key}: Rp.{value}")
    else:
        print(f"Total transaksi {periode.capitalize()}: Rp.{hasil}")

def menu_admin(produk_pistol, produk_smg, produk_shotgun, produk_sniper_rifle, produk_assault_rifle, produk_equip, produk_throwable, produk_ammo):
    while True:
        print("===============================")
        print("1. Tambahkan Produk")
        print("2. Hapus Produk")
        print("3. Atur Stok")
        print("4. Perhitungan Transaksi")
        print("===============================")
        print("9. Kembali")
        pilih_menu = input("Pilih menu : ")

        if pilih_menu == "1":
            print("===============================")
            print("1. Pistol")
            print("2. SMG")
            print("3. Shotgun")
            print("4. Sniper Rifle")
            print("5. Assault Rifle")
            print("6. Equip")
            print("7. Throwable")
            print("8. Ammo")
            print("===============================")
            print("9. Kembali")
            jenis_produk = input("Pilih jenis produk: ")
            if jenis_produk == "1":
                tambah_produk(produk_pistol, 'pistol')
            elif jenis_produk == "2":
                tambah_produk(produk_smg, 'smg')
            elif jenis_produk == "3":
                tambah_produk(produk_shotgun, 'shotgun')
            elif jenis_produk == "4":
                tambah_produk(produk_sniper_rifle, 'sniper_rifle')
            elif jenis_produk == "5":
                tambah_produk(produk_assault_rifle, 'assault_rifle')
            elif jenis_produk == "6":
                tambah_produk(produk_equip, 'equip')
            elif jenis_produk == "7":
                tambah_produk(produk_throwable, 'throwable')
            elif jenis_produk == "8":
                tambah_produk(produk_ammo, 'ammo')
            elif jenis_produk == "9":
                continue
            else:
                print("Pilihan tidak valid.")

        elif pilih_menu == "2":
            print("===============================")
            print("1. Pistol")
            print("2. SMG")
            print("3. Shotgun")
            print("4. Sniper Rifle")
            print("5. Assault Rifle")
            print("6. Equip")
            print("7. Throwable")
            print("8. Ammo")
            print("===============================")
            print("9. Kembali")
            jenis_produk = input("Pilih jenis produk: ")
            if jenis_produk == "1":
                hapus_produk(produk_pistol, 'pistol')
            elif jenis_produk == "2":
                hapus_produk(produk_smg, 'smg')
            elif jenis_produk == "3":
                hapus_produk(produk_shotgun, 'shotgun')
            elif jenis_produk == "4":
                hapus_produk(produk_sniper_rifle, 'sniper_rifle')
            elif jenis_produk == "5":
                hapus_produk(produk_assault_rifle, 'assault_rifle')
            elif jenis_produk == "6":
                hapus_produk(produk_equip, 'equip')
            elif jenis_produk == "7":
                hapus_produk(produk_throwable, 'throwable')
            elif jenis_produk == "8":
                hapus_produk(produk_ammo, 'ammo')
            elif jenis_produk == "9":
                continue
            else:
                print("Pilihan tidak valid.")

        elif pilih_menu == "3":
            print("===============================")
            print("1. Pistol")
            print("2. SMG")
            print("3. Shotgun")
            print("4. Sniper Rifle")
            print("5. Assault Rifle")
            print("6. Equip")
            print("7. Throwable")
            print("8. Ammo")
            print("===============================")
            print("9. Kembali")
            jenis_produk = input("Pilih jenis produk: ")
            if jenis_produk == "1":
                atur_stok(produk_pistol, 'pistol')
            elif jenis_produk == "2":
                atur_stok(produk_smg, 'smg')
            elif jenis_produk == "3":
                atur_stok(produk_shotgun, 'shotgun')
            elif jenis_produk == "4":
                atur_stok(produk_sniper_rifle, 'sniper_rifle')
            elif jenis_produk == "5":
                atur_stok(produk_assault_rifle, 'assault_rifle')
            elif jenis_produk == "6":
                atur_stok(produk_equip, 'equip')
            elif jenis_produk == "7":
                atur_stok(produk_throwable, 'throwable')
            elif jenis_produk == "8":
                atur_stok(produk_ammo, 'ammo')
            elif jenis_produk == "9":
                continue
            else:
                print("Pilihan tidak valid.")

        elif pilih_menu == "4":
            print("===============================")
            print("1. Harian")
            print("2. Mingguan")
            print("3. Bulanan")
            print("4. Tahunan")
            print("===============================")
            pilih_waktu = input("Pilih periode: ")
            transaksi = baca_data_transaksi('data_transaksi.csv')
            if pilih_waktu == "1":
                hasil = hitung_total_hari_ini(transaksi)
                tampilkan_hasil(hasil, 'harian')
            elif pilih_waktu == "2":
                hasil = hitung_total_mingguan(transaksi)
                tampilkan_hasil(hasil, 'mingguan')
            elif pilih_waktu == "3":
                hasil = hitung_total_bulanan(transaksi)
                tampilkan_hasil(hasil, 'bulanan')
            elif pilih_waktu == "4":
                hasil = hitung_total_tahunan(transaksi)
                tampilkan_hasil(hasil, 'tahunan')
            elif pilih_waktu == "9":
                continue
            else:
                print("Pilihan tidak valid.")

        elif pilih_menu == "9":
            break
        else:
            print("Pilihan tidak valid.")

def simpan_data(file_csv, produk):
    with open(file_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        if produk:
            header = produk[0].keys()
            writer.writerow(header)
            for item in produk:
                writer.writerow(item.values())

def baca_data(file_csv, jenis):
    produk = []
    try:
        with open(file_csv, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if jenis in ['pistol', 'smg', 'shotgun', 'sniper_rifle', 'assault_rifle']:
                    produk.append({
                        'id': int(row[0]),
                        'jenis_peluru': row[1],
                        'nama': row[2],
                        'harga': float(row[3]),
                        'stok': int(row[4]),
                        'jenis': jenis
                    })
                elif jenis == 'equip':
                    produk.append({
                        'id': int(row[0]),
                        'jenis_equip': row[1],
                        'nama': row[2],
                        'harga': float(row[3]),
                        'stok': int(row[4]),
                        'jenis': jenis
                    })
                elif jenis == 'throwable':
                    produk.append({
                        'id': int(row[0]),
                        'jenis_throwable': row[1],
                        'nama': row[2],
                        'harga': float(row[3]),
                        'stok': int(row[4]),
                        'jenis': jenis
                    })
                elif jenis == 'ammo':
                    produk.append({
                        'id': int(row[0]),
                        'jenis_peluru': row[1],
                        'merk': row[2],
                        'harga': float(row[3]),
                        'stok': int(row[4]),
                        'jenis': jenis
                    })
    except FileNotFoundError:
        print(f"File {file_csv} tidak ditemukan.")
    return produk

produk_pistol = baca_data('data_produk_pistol.csv', 'pistol')
produk_smg = baca_data('data_produk_smg.csv', 'smg')
produk_shotgun = baca_data('data_produk_shotgun.csv', 'shotgun')
produk_sniper_rifle = baca_data('data_produk_sniper_rifle.csv', 'sniper_rifle')
produk_assault_rifle = baca_data('data_produk_assault_rifle.csv', 'assault_rifle')
produk_equip = baca_data('data_produk_equip.csv', 'equip')
produk_throwable = baca_data('data_produk_throwable.csv', 'throwable')
produk_ammo = baca_data('data_produk_ammo.csv', 'ammo')
