from django.shortcuts import render
from . models import Dosen, Staf, Mahasiswa

# Create your views here.
def fh(request):
    arti='Fakultas hukum Universitas Sultan Ageng Tirtayasa sudah berdiri sejak tahun 1981, tepatnya pada tanggal 1 Oktober 1981. Fakultas Hukum Untirta hanya memiliki 1 progran studi, yakni Ilmu Hukum. Fakultas Hukum Universitas Sultan Ageng Tirtayasa berlokasi pada Kampus Utama Untirta Sindangsari.'
    jurusan=['Ilmu Hukum']
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
    return render(request, 'fh.html', konteks)