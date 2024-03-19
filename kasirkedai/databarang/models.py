from django.db import models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama
    