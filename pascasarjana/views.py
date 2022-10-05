from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa

# Create your views here.
def pascasarjana(request):
    arti='Selain memiliki Program Studi Sarjana dan Program Studi Diploma, Universitas Sultan Ageng Tirtayasa pun memiliki Program Studi Magister dengan berbagai pilihan program studi. Gedung Pascasarajana berlokasi pada Kampus Untirta Pakupatan.'
    jurusan=['Doktor Pendidikan', 'Doktor Ilmu Akuntansi', 'Magister Ilmu Hukum', 'Magister Ilmu Pertanian', 'Magister Administrasi Publik', 'Magister Akuntansi', 'Magister Ilmu Komunikasi', 'Magister Manajemen', 'Magister Teknik Kimia', 'Pendidikan Bahasa Indonesia', 'Pendidikan Bahasa Inggris', 'Pendidikan Matematika', 'Teknologi Pendidikan']
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks={
        'title': arti,
        'isi':jurusan,
        'dataDosen' : dosen,
        'dataStaf': staf,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'pascasarjana.html', konteks)