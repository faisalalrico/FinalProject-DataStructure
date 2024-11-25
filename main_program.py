import csv
from queue import Queue
from module import product_finder, product_list_viewer, cart_manager, administrator_mode

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
                'nama': row[2],
                'harga': float(row[3]),
                'stok': int(row[4]),
                'jenis': jenis
            })
    return produk

def sistem_penjualan_produk():
    pistol = baca_data('data_produk_pistol.csv', 'pistol')
    smg = baca_data('data_produk_smg.csv', 'smg')
    shotgun = baca_data('data_produk_shotgun.csv', 'shotgun')
    sniper_rifle = baca_data('data_produk_sniper_rifle.csv', 'sniper_rifle')
    assault_rifle = baca_data('data_produk_assault_rifle.csv', 'assault_rifle')
    throwable = baca_data_throwable('data_produk_throwable.csv', 'throwable')
    equip = baca_data_equip('data_produk_equip.csv', 'equip')
    ammo = baca_data_ammo('data_produk_ammo.csv', 'ammo')
    equipment_other = throwable + equip + ammo
    produk = pistol + shotgun + smg + sniper_rifle + assault_rifle
    full_produk = produk + equipment_other
    antrian = Queue()

    while True:
        print("\nShop:")
        print("======================")
        print("1. Pencarian Produk")
        print("2. Pistol")
        print("3. Sub Machine Gun")
        print("4. Shotgun")
        print("5. Sniper Rifle")
        print("6. Assault Rifle")
        print("7. Equipment & Other")
        print("======================")
        print("8. Keranjang Belanja")
        print("9. Mode Admin")
        print("10. Keluar")
        print("")
        pilihan = input("Pilih menu: ")
        print("")

        if pilihan == '1':
            product_finder.cari_produk(full_produk)
        elif pilihan == '2':
            product_list_viewer.tampilkan_produk(produk, 'pistol')
            print("======================")
            print("0. Untuk Kembali")
            print("======================")
            id_pistol = int(input("Masukkan ID senjata yang ingin dibeli: "))
    
            if id_pistol == 0:
                continue
    
            pistol_dipilih = next((b for b in produk if b['id'] == id_pistol and b['jenis'] == 'pistol'), None)
            if pistol_dipilih:
                jumlah = int(input("Masukkan jumlah senjata yang ingin dibeli: "))
                if pistol_dipilih['stok'] >= jumlah:
                    antrian.put({**pistol_dipilih, 'jumlah': jumlah, 'total_harga': pistol_dipilih['harga'] * jumlah})
                    pistol_dipilih['stok'] -= jumlah
                    print(f"{jumlah} senjata {pistol_dipilih['nama']} ditambahkan ke antrian.")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Senjata tidak ditemukan atau stok tidak mencukupi.")

        elif pilihan == '3':
            product_list_viewer.tampilkan_produk(produk, 'smg')
            print("======================")
            print("0. Untuk Kembali")
            print("======================")
            id_smg = int(input("Masukkan ID senjata yang ingin dibeli: "))

            if id_smg == 0:
                continue

            smg_dipilih = next((b for b in produk if b['id'] == id_smg and b['jenis'] == 'smg'), None)
            if smg_dipilih:
                jumlah = int(input("Masukkan jumlah senjata yang ingin dibeli: "))
                if smg_dipilih['stok'] >= jumlah:
                    antrian.put({**smg_dipilih, 'jumlah': jumlah, 'total_harga': smg_dipilih['harga'] * jumlah})
                    smg_dipilih['stok'] -= jumlah
                    print(f"{jumlah} senjata {smg_dipilih['nama']} ditambahkan ke antrian.")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Senjata tidak ditemukan atau stok tidak mencukupi.")

        elif pilihan == '4':
            product_list_viewer.tampilkan_produk(produk, 'shotgun')
            print("======================")
            print("0. Untuk Kembali")
            print("======================")
            id_shotgun = int(input("Masukkan ID senjata yang ingin dibeli: "))

            if id_shotgun == 0:
                continue

            shotgun_dipilih = next((b for b in produk if b['id'] == id_shotgun and b['jenis'] == 'shotgun'), None)
            if shotgun_dipilih:
                jumlah = int(input("Masukkan jumlah senjata yang ingin dibeli: "))
                if shotgun_dipilih['stok'] >= jumlah:
                    antrian.put({**shotgun_dipilih, 'jumlah': jumlah, 'total_harga': shotgun_dipilih['harga'] * jumlah})
                    shotgun_dipilih['stok'] -= jumlah
                    print(f"{jumlah} senjata {shotgun_dipilih['nama']} ditambahkan ke antrian.")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Senjata tidak ditemukan atau stok tidak mencukupi.")

        elif pilihan == '5':
            product_list_viewer.tampilkan_produk(produk, 'sniper_rifle')
            print("======================")
            print("0. Untuk Kembali")
            print("======================")
            id_sniper_rifle = int(input("Masukkan ID senjata yang ingin dibeli: "))

            if id_sniper_rifle == 0:
                continue

            sniper_rifle_dipilih = next((b for b in produk if b['id'] == id_sniper_rifle and b['jenis'] == 'sniper_rifle'), None)
            if sniper_rifle_dipilih:
                jumlah = int(input("Masukkan jumlah senjata yang ingin dibeli: "))
                if sniper_rifle_dipilih['stok'] >= jumlah:
                    antrian.put({**sniper_rifle_dipilih, 'jumlah': jumlah, 'total_harga': sniper_rifle_dipilih['harga'] * jumlah})
                    sniper_rifle_dipilih['stok'] -= jumlah
                    print(f"{jumlah} senjata {sniper_rifle_dipilih['nama']} ditambahkan ke antrian.")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Senjata tidak ditemukan atau stok tidak mencukupi.")

        elif pilihan == '6':
            product_list_viewer.tampilkan_produk(produk, 'assault_rifle')
            print("======================")
            print("0. Untuk Kembali")
            print("======================")
            id_assault_rifle = int(input("Masukkan ID senjata yang ingin dibeli: "))

            if id_assault_rifle == 0:
                continue

            assault_rifle_dipilih = next((b for b in produk if b['id'] == id_assault_rifle and b['jenis'] == 'assault_rifle'), None)
            if assault_rifle_dipilih:
                jumlah = int(input("Masukkan jumlah senjata yang ingin dibeli: "))
                if assault_rifle_dipilih['stok'] >= jumlah:
                    antrian.put({**assault_rifle_dipilih, 'jumlah': jumlah, 'total_harga': assault_rifle_dipilih['harga'] * jumlah})
                    assault_rifle_dipilih['stok'] -= jumlah
                    print(f"{jumlah} senjata {assault_rifle_dipilih['nama']} ditambahkan ke antrian.")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Senjata tidak ditemukan atau stok tidak mencukupi.")

        elif pilihan == '7':
            print("1. Equipment")
            print("2. Throwable")
            print("3. Ammo")
            print("======================")
            print("0. Untuk Kembali")
            print("======================")
            pilihan_minor = input("Masukkan tipe peralatan yang ingin dibeli: ")

            if pilihan_minor == '0':
                continue

            if pilihan_minor == '1':
                product_list_viewer.tampilkan_produk_equip(equip)
                print("======================")
                print("0. Untuk Kembali")
                print("======================")
                id_equip = int(input("Masukkan ID equipment yang ingin dibeli: "))
        
                if id_equip == 0:
                    continue
            
                equip_dipilih = next((b for b in equipment_other if b['id'] == id_equip and b['jenis'] == 'equip'), None)
                if equip_dipilih:
                    jumlah = int(input("Masukkan jumlah equipment yang ingin dibeli: "))
                    if equip_dipilih['stok'] >= jumlah:
                        antrian.put({**equip_dipilih, 'jumlah': jumlah, 'total_harga': equip_dipilih['harga'] * jumlah})
                        equip_dipilih['stok'] -= jumlah
                        print(f"{jumlah} equipment {equip_dipilih['nama']} ditambahkan ke antrian.")
                    else:
                        print("Stok tidak mencukupi.")
                else:
                    print("Equipment tidak ditemukan atau stok tidak mencukupi.")
            elif pilihan_minor == '2':
                product_list_viewer.tampilkan_produk_throwable(throwable)
                print("======================")
                print("0. Untuk Kembali")
                print("======================")
                id_throwable = int(input("Masukkan ID throwable yang ingin dibeli: "))
        
                if id_throwable == 0:
                    continue
            
                throwable_dipilih = next((b for b in equipment_other if b['id'] == id_throwable and b['jenis'] == 'throwable'), None)
                if throwable_dipilih:
                    jumlah = int(input("Masukkan jumlah throwable yang ingin dibeli: "))
                    if throwable_dipilih['stok'] >= jumlah:
                        antrian.put({**throwable_dipilih, 'jumlah': jumlah, 'total_harga': throwable_dipilih['harga'] * jumlah})
                        throwable_dipilih['stok'] -= jumlah
                        print(f"{jumlah} throwable {throwable_dipilih['nama']} ditambahkan ke antrian.")
                    else:
                        print("Stok tidak mencukupi.")
                else:
                    print("Throwable tidak ditemukan atau stok tidak mencukupi.")
            elif pilihan_minor == '3':
                product_list_viewer.tampilkan_produk_ammo(ammo)
                print("======================")
                print("0. Untuk Kembali")
                print("======================")
                id_ammo = int(input("Masukkan ID ammo yang ingin dibeli: "))
        
                if id_ammo == 0:
                    continue
            
                ammo_dipilih = next((b for b in equipment_other if b['id'] == id_ammo and b['jenis'] == 'ammo'), None)
                if ammo_dipilih:
                    jumlah = int(input("Masukkan jumlah ammo yang ingin dibeli: "))
                    if ammo_dipilih['stok'] >= jumlah:
                        antrian.put({**ammo_dipilih, 'jumlah': jumlah, 'total_harga': ammo_dipilih['harga'] * jumlah})
                        ammo_dipilih['stok'] -= jumlah
                        print(f"{jumlah} ammo {ammo_dipilih['nama']} ditambahkan ke antrian.")
                    else:
                        print("Stok tidak mencukupi.")
                else:
                    print("Ammo tidak ditemukan atau stok tidak mencukupi.")
            else:
                print("Pilihan tidak valid, silakan coba lagi.")

        elif pilihan == '8':
            cart_manager.keranjang_belanja(antrian)

        elif pilihan == '9':
            print("= Verifikasi =")
            username = input("Masukkan username: ")
            if username == "admin123":
                password = input("Masukkan password: ")
                if password == "123":
                    administrator_mode.menu_admin(pistol, smg, shotgun, sniper_rifle, assault_rifle, equip, throwable, ammo)
                else:
                    print("(x) Password salah (x)")
                    sistem_penjualan_produk()
            else:
                print("(x) Username salah (x)")
                sistem_penjualan_produk()
                
        elif pilihan == '10':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def perjumpaan_awal():
    print("===================================")
    print("=  Selamat Datang Weapon Shop FA  =")
    print("=              IF23G              =")
    print("===================================")

perjumpaan_awal()
sistem_penjualan_produk()
