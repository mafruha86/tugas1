from django.urls import path
from . import views

urlpatterns = [
    path('daftar-penjualan/', views.daftar_penjualan, name='daftar_penjualan'),
]
