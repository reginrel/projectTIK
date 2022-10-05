from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa

# Create your views here.
def faperta(request):
    arti= 'Fakultas Pertanian Universitas Sultan Ageng Tirtayasa berlokasi pada Kampus Utama Untirta Sindangsari. Pada saat ini, fakultas pertanian memiliki 2526 mahasiswa aktif dan 102 dosen. Fakultas Pertanian memiliki 4 Program Studi.'
    jurusan= ['Program Studi Agribisnis', 'Program Studi Agroekoteknologi', 'Program Studi Perikanan', 'Program Studi Teknologi Pangan']
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
    return render(request, 'faperta.html', konteks)