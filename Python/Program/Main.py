# import class dari file
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from ProgramStudi import ProgramStudi
from Course import Course

# deklarasi array
mhs = []
dosen = []
prodi = []
matkul = []

#  Setiap index dari array akan diisi oleh attribut dari class Human,
#  SivitasAkademik, Mahasiswa, Dosen, MataKuliah, Program Studi
#  yang akan menggunakan method setter  lalu di add ke array
temp = Mahasiswa()
temp.set_nik("3001323007020001")
temp.set_nama("Farhan")
temp.set_jenis_kelamin("L")
temp.set_asal_universitas("UPI")
temp.set_email_edu("farhan@upi.edu")
temp.set_nim("2105879")
temp.set_fakultas("FPMIPA")
mhs.append(temp)

temp = Dosen()
temp.set_nik("3121323012020002")
temp.set_nama("Farah")
temp.set_jenis_kelamin("P")
temp.set_asal_universitas("UPI")
temp.set_email_edu("farah@upi.edu")
temp.set_fakultas("FPBS")
temp.set_nip("39847463782")
temp.set_pend_terakhir("S3")
temp.set_keahlian("AI")
dosen.append(temp)


temp = ProgramStudi()
temp.set_nama_prodi("ILMU KOMPUTER")
temp.set_kode("IK23")
temp1 = Course()
temp1.set_nama_matakuliah("ALPRO")
temp.set_course(temp1)
temp2 = Course()
temp2.set_nama_matakuliah("STRUKDAT")
temp.set_course(temp2)
temp3 = Course()
temp3.set_nama_matakuliah("DPBO")
temp.set_course(temp3)
prodi.append(temp)

#  menampilkan isi dari list dengan looping for dan setiap attributnya ditampilkan dengan memanggil getter masing-masing attribut
if not mhs:
    print("DATA MAHASISWA KOSONG!")
else:
    n = 1
    print("Data Lengkap Mahasiswa: ")
    for Mhs in mhs:
        print(n, end=". ")
        print("NIK                   :", Mhs.get_nik())
        print("   Nama                  :", Mhs.get_nama())
        print("   Jenis Kelamin         :", Mhs.get_jenis_kelamin())
        print("   NIM                   :", Mhs.get_nim())
        print("   Asal Universitas      :", Mhs.get_asal_universitas())
        print("   Email Edu             :", Mhs.get_email_edu())
        print("   Fakultas              :", Mhs.get_fakultas())
        print("")
        n += 1

if not dosen:
    print("DATA Dosen KOSONG!")
else:
    n = 1
    print("Data Lengkap Dosen: ")
    for dosen in dosen:
        print(n, end=". ")
        print("NIK                   :", dosen.get_nik())
        print("   Nama                  :", dosen.get_nama())
        print("   Jenis Kelamin         :", dosen.get_jenis_kelamin())
        print("   NIM                   :", dosen.get_nip())
        print("   Asal Universitas      :", dosen.get_asal_universitas())
        print("   Email Edu             :", dosen.get_email_edu())
        print("   Fakultas              :", dosen.get_fakultas())
        print("   Pendidikan Terakhir   :", dosen.get_pend_terakhir())
        print("   Keahlian              :", dosen.get_keahlian())
        print("")
        n += 1

if not prodi:
    print("DATA PRODI KOSONG!")
else:
    n = 1
    i = 1
    print("Data Lengkap Prodi: ")
    for prodi in prodi:
        print(n, end=". ")
        print("Nama Prodi            :", prodi.get_nama_prodi())
        print("   Kode                  :", prodi.get_kode())
        print("   Mata Kuliah           :")
        for matkul in prodi.get_course():
            print("                         ", i, end=". ")
            print(matkul.get_nama_matakuliah())
            i += 1
        print("")
        n += 1
