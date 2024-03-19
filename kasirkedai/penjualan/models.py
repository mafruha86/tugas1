from django.db import models
from databarang.models import Barang

class Penjualan(models.Model):
    tanggal = models.DateField(auto_now_add=True)

class ItemPenjualan(models.Model):
    penjualan = models.ForeignKey(Penjualan, related_name='items', on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, related_name='penjualan_items', on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField(default=1)