from django.contrib import admin
from django.urls import path, include
from databarang import views as databarang_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('databarang/', include('databarang.urls')),
    path('penjualan/', include('penjualan.urls')), 
]
