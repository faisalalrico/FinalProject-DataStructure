import csv
from queue import Queue

def cari_produk(full_produk):
    query = input("Masukkan nama atau merk produk yang ingin dicari: ").lower()
    print("")
    hasil_cari = []

    for p in full_produk:
        if p['jenis'] in ['pistol', 'smg', 'shotgun', 'sniper_rifle', 'assault_rifle']:
            if query in p['jenis_peluru'].lower() or query in p['nama'].lower():
                hasil_cari.append(p)
        elif p['jenis'] == 'equip':
            if query in p['jenis_equip'].lower() or query in p['nama'].lower():
                hasil_cari.append(p)
        elif p['jenis'] == 'throwable':
            if query in p['jenis_throwable'].lower() or query in p['nama'].lower():
                hasil_cari.append(p)
        elif p['jenis'] == 'ammo':
            if query in p['jenis_peluru'].lower() or query in p['nama'].lower():
                hasil_cari.append(p)

    if hasil_cari:
        print("======================")
        print("Hasil pencarian:")
        print("======================")
        for item in hasil_cari:
            if item['jenis'] in ['pistol', 'smg', 'shotgun', 'sniper_rifle', 'assault_rifle']:
                print(f"ID: {item['id']}, Jenis: {item['jenis']}, Jenis Peluru: {item['jenis_peluru']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
            elif item['jenis'] == 'equip':
                print(f"ID: {item['id']}, Jenis: {item['jenis']}, Jenis Equip: {item['jenis_equip']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
            elif item['jenis'] == 'throwable':
                print(f"ID: {item['id']}, Jenis: {item['jenis']}, Jenis Throwable: {item['jenis_throwable']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
            elif item['jenis'] == 'ammo':
                print(f"ID: {item['id']}, Jenis: {item['jenis']}, Jenis Peluru: {item['jenis_peluru']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
    else:
        print("Tidak ada produk yang sesuai dengan pencarian Anda.")