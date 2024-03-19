from django.urls import path
from . import views

urlpatterns = [
    path('tambah/', views.tambah_barang, name='tambah_barang'),
    path('', views.tampilkan_data_barang, name='tampilkan_data_barang'),
]
