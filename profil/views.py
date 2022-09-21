from django.shortcuts import render

# Create your views here.
def profil(request):
    jurusan=['Nama : Regina Citra Nanda', 'NIM : 2225210040', 'Jurusan : Pendidikan Matematika' ,'Fakultas : Keguruan dan Ilmu Pendidikan', 'Instansi : Universitas Sultan Ageng Tirtayasa', 'Email : 2225210040@untirta.ac.id', 'No HP : 085216306732']
    
    konteks={
        'isi': jurusan,
    }
    return render(request, 'profil.html', konteks)