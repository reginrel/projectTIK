from django.shortcuts import render

# Create your views here.
def faperta(request):
    arti= 'Fakultas Pertanian Universitas Sultan Ageng Tirtayasa berlokasi pada Kampus Utama Untirta Sindangsari. Pada saat ini, fakultas pertanian memiliki 2526 mahasiswa aktif dan 102 dosen. Fakultas Pertanian memiliki 4 Program Studi.'
    jurusan= ['Program Studi Agribisnis', 'Program Studi Agroekoteknologi', 'Program Studi Perikanan', 'Program Studi Teknologi Pangan']

    konteks={
        'title': arti,
        'isi': jurusan,
    }
    return render(request, 'faperta.html', konteks)