from django.shortcuts import render

# Create your views here.
def ft(request):
    arti='Fakultas Teknik Universitas Sultan Ageng Tirtayasa berlokasi di Kampus Untirta kota Cilegon. Fakultas ini memiliki 6 program studi. Fakultas Teknik sudah menjadi bagian dari Universitas Sultan Ageng Tirtayasa sejak tahun 2001.'
    jurusan=['Jurusan Teknik Elektro', 'Jurusan Teknik Industri', 'Jurusan Teknik Kimia', 'Jurusan Teknik Mesin', 'Jurusan Teknik Metalurgi', 'Jurusan Teknik Sipil']

    konteks={
        'title':arti,
        'isi':jurusan,
    }
    return render(request, 'ft.html', konteks)