from django.shortcuts import render
from .models import Penjualan

def daftar_penjualan(request):
    daftar_penjualan = Penjualan.objects.all()
    return render(request, 'penjualan/daftar_penjualan.html', {'daftar_penjualan': daftar_penjualan})
