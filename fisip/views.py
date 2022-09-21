from django.shortcuts import render

# Create your views here.
def fisip(request):
    arti='Fakultas Ilmu Sosial dan Politik Universitas Sultan Ageng Tirtayasa Banten memiliki 4 program studi. Lokasi Fakultas ini terletak pada Kampus Utama Untirta Sindangsari.'
    jurusan=['Program Studi Administrasi Publik', 'Program Studi Ilmu Komunikasi', 'Program Studi Ilmu Pemerintahan']

    konteks={
        'title': arti,
        'isi': jurusan,
    }
    return render(request, 'fisip.html', konteks)