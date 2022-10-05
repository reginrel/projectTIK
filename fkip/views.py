from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa


# Create your views here.
def fkip(request):
    arti='Fakultas Keguruan dan Ilmu Pendidikan Universitas Sultan Aheng Tirtayasa menjadi fakultas dengan jumlah program studi terbanyak, yakni dengan 18 program studi. Fakultas Keguruan dan Ilmu Pendidikan ini sudah berdiri sejak 1 Oktober 1982 dengan memiliki 2 program studi, yakni prodi IPPS-Pls dan Administrasi Pendidikan. Namun, seiring berjalannya waktu, jumlah program studi di fakultas ini terus bertambah. Fakultas Keguruan dan ilmu Pendidikan berlokasi pada kampus Untirta Ciwaru.'
    jurusan=['Jurusan Pendidikan Nonformal', 'Jurusan Pendidikan Bahasa Indonesia', 'jurusan Pendidikan Bahasa Inggris', 'Jurusan Pendidikan Biologi', 'Jurusan Pendidikan Matematika', 'Jurusan Pendidikan Guru Sekolah Dasar', 'Jurusan Pendidikan Guru PAUD', 'Jurusan Bimbingan dan Konseling', 'Jurusan Pendidikan Fisika', 'Jurusan Pendidikan Ilmu Pengetahuan Alam', 'Jurusan Pendidikan Kimia', 'Jurusan Pendidikan Khusus', 'Jurusan Pendidikan Pancasila dan Kewarganegaraan', 'Jurusan Pendidikan Sejarah', 'Jurusan Pendidikan Seni dan Pertunjukan', 'Jurusan Pendidikan Sosiologi', 'Jurusan Pendidikan Vokasional Teknik Elektro', 'Jurusan Pendidikan Vokasional Teknik Mesin']
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks={
        'title':arti,
        'isi':jurusan,
        'dataDosen' : dosen,
        'dataStaf': staf,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip.html', konteks)