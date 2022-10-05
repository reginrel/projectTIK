from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa

# Create your views here.
def fisip(request):
    arti='Fakultas Ilmu Sosial dan Politik Universitas Sultan Ageng Tirtayasa Banten memiliki 4 program studi. Lokasi Fakultas ini terletak pada Kampus Utama Untirta Sindangsari.'
    jurusan=['Program Studi Administrasi Publik', 'Program Studi Ilmu Komunikasi', 'Program Studi Ilmu Pemerintahan']
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks={
        'title': arti,
        'isi': jurusan,
        'dataDosen' : dosen,
        'dataStaf': staf,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fisip.html', konteks)