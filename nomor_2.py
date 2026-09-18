modal_awal = float(input("Masukkan angka Modal Awal: Rp"))

keuntungan = 0.20 * modal_awal
total_penjualan = modal_awal + keuntungan

print(f"\nModal Awal        : Rp{modal_awal:,.2f}")
print(f"Target Keuntungan : Rp{keuntungan:,.2f}")
print(f"Total Penjualan   : Rp{total_penjualan:,.2f}")
