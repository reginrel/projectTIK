from django.shortcuts import render

# Create your views here.
def fk(request):
    arti='Fakultas Kedokteran merupakan fakultas yang paling baru di antara semua fakultas yang terdapat pada Universitas Sultan Ageng Tirtayasa. Walaupun Fakultas ini masih baru, akan tetapi sudah memiliki 5 program studi, yakni 4 program studi sarjana, dan 1 program diploma. Fakultas ini berlokasi pada Kampus Utama Untirta Sindangsari'
    jurusan= ['Prodi Kedokteran', 'Prodi Keperawatan S1', 'Prodi Keperawatan D3', 'Prodi S1 Gizi', 'Prodi Ilmu Keolahragaan']

    konteks={
        'title': arti,
        'isi': jurusan,
    }
    return render(request, 'fk.html', konteks)