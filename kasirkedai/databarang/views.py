from django.shortcuts import render, redirect
from .forms import BarangForm
from .models import Barang

def tambah_barang(request):
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tampilkan_data_barang')
    else:
        form = BarangForm()
    return render(request, 'databarang/tambah_barang.html', {'form': form})

def tampilkan_data_barang(request):
    daftar_barang = Barang.objects.all()
    return render(request, 'databarang/tampilan_barang.html', {'daftar_barang': daftar_barang})
