from django.shortcuts import render

# Create your views here.
def fh(request):
    arti='Fakultas hukum Universitas Sultan Ageng Tirtayasa sudah berdiri sejak tahun 1981, tepatnya pada tanggal 1 Oktober 1981. Fakultas Hukum Untirta hanya memiliki 1 progran studi, yakni Ilmu Hukum. Fakultas Hukum Universitas Sultan Ageng Tirtayasa berlokasi pada Kampus Utama Untirta Sindangsari.'
    jurusan=['Ilmu Hukum']

    konteks={
        'title': arti,
        'isi': jurusan,
    }
    return render(request, 'fh.html', konteks)