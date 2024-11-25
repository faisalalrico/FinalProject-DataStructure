import csv
from queue import Queue

def tampilkan_produk(produk, jenis):
    print(f"Daftar {jenis.capitalize()} Tersedia:")
    for item in produk:
        if item['jenis'] == jenis:
            print(f"ID: {item['id']}, Jenis Peluru: {item['jenis_peluru']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")

def tampilkan_produk_equip(equip):
    print("Daftar Equipment Tersedia:")
    for item in equip:
        if item['jenis'] == 'equip':
            print(f"ID: {item['id']}, Jenis: {item['jenis_equip']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")

def tampilkan_produk_throwable(throwable):
    print("Daftar throwable Tersedia:")
    for item in throwable:
        if item['jenis'] == 'throwable':
            print(f"ID: {item['id']}, Jenis: {item['jenis_throwable']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")

def tampilkan_produk_ammo(ammo):
    print("Daftar Ammo Tersedia:")
    for item in ammo:
        if item['jenis'] == 'ammo':
            print(f"ID: {item['id']}, Jenis Peluru: {item['jenis_peluru']}, Nama: {item['nama']}, Harga: {item['harga']}, Stok: {item['stok']}")
