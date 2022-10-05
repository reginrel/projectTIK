from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa

# Create your views here.
def feb(request):
    arti= 'Fakultas Ekonomi dan Bisnis Universitas Sultan Ageng Tirtayasa sudah berdiri sejak 1 oktober 1980. Fakultas Ekonomi dan Bisnis ini memiliki 8 program studi dengan 4 program sarjana dan 4 program diploma. Fakultas Ekonomi dan Bisnis terletak pada Kampus Utama Untirta Sindangsari.'
    jurusan=['Program Sarjana Managemen', 'Program Sarjana Akuntansi', 'Program Sarjana Ilmu Ekonomi Pembangunan', 'Program Sarjana Ekonomi Syariah', 'Program Diploma III Akuntansi', 'Program Diploma III Marketing', 'Program Diploma III Perpajakan', 'Program Diploma III Keuangan Perbankan']
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
    return render(request, 'feb.html', konteks)