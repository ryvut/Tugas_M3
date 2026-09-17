print("=== Masukkan 12 Data Biodata Mahasiswa & Rencana Karier ===")

nama_lengkap = input("1. Nama Lengkap: ")
usia = int(input("2. Usia (Angka): "))
kontak = input("3. Nomor Kontak/HP: ")
alamat_asal = input("4. Alamat Asal: ")
kampus = input("5. Kampus: ")
fakultas_dept = input("6. Fakultas / Dept: ")
nrp = input("7. NRP: ")
angkatan = int(input("8. Angkatan (Angka): "))
sks = int(input("9. Jumlah SKS (Angka): "))
matkul = input("10. Mata Kuliah: ")
dream_job = input("11. Target Karier (Dream Job): ")
motto = input("12. Motto Hidup / Motivasi: ")

print("\n" + "=" * 54)
print(f"|{'DASBOR PROFIL MAHASISWA & RENCANA KARIER':^52}|")
print("=" * 54)
print(f"|{'INFORMASI PERSONAL':<52}|")
print("-" * 54)

baris_nama = f"Nama Lengkap    : {nama_lengkap}"
print(f"|{baris_nama:<52}|")

baris_usia_kontak = f"Usia & Kontak   : {usia} Tahun | {kontak}"
print(f"|{baris_usia_kontak:<52}|")

baris_alamat = f"Alamat Asal     : {alamat_asal}"
print(f"|{baris_alamat:<52}|")

print("-" * 54)
print(f"|{'INFORMASI AKADEMIK':<52}|")
print("-" * 54)

baris_kampus = f"Kampus          : {kampus}"
print(f"|{baris_kampus:<52}|")

baris_fakultas = f"Fakultas / Dept : {fakultas_dept}"
print(f"|{baris_fakultas:<52}|")

baris_nrp = f"NRP / Angkatan  : {nrp} / {angkatan}"
print(f"|{baris_nrp:<52}|")

baris_sks = f"SKS & Matkul    : {sks} SKS | {matkul}"
print(f"|{baris_sks:<52}|")

print("=" * 54)
print(f"|{'TARGET KARIER (DREAM JOB)':^52}|")
print(f"|{dream_job.upper():^52}|")

baris_motto = f'"{motto}"'
print(f"|{baris_motto:^52}|")

print("=" * 54)