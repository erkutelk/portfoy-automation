from django.urls import path
from .views_page.page_home import anasayfa
from .views_page import page_musteriler
from .views_page import pages_gelirler
from .views_page import pages_giderler
from .views_page.pages_raporlar import raporlar
from .views_page import pages_faturalar
from .views_page.pages_ayarlar import ayarlar

urlpatterns = [
    path('',anasayfa,name='anasayfa'),
    path('anasayfa',anasayfa,name='anasayfa'),

    path('musteriler/tum-musteriler',page_musteriler.musteriler_,name='musteriler'),
    path('musteriler/musteri-ekle',page_musteriler.musteriler_ekle,name='musteri_ekle'),
    path('musteriler/musteri-detay/<int:id>',page_musteriler.musteriler_detay,name='musteri_detay'),
    path('musteriler/musteri-sil/<int:id>',page_musteriler.musteri_sil,name='musteri-sil'),

    path('gelirler/tum-gelirler',pages_gelirler.gelirler,name='gelirler'),
    path('gelirler/gelir-ekle',pages_gelirler.gelir_create,name='gelir_ekle'),
    path('gelirler/detay/<int:id>',pages_gelirler.gelir_detay,name='gelirler_detail'),

    path('giderler',pages_giderler.giderler,name='giderler'),
    path('giderler/ekle',pages_giderler.Gider_Create,name='gider_ekle'),
    path('giderler/detay/<int:id>',pages_giderler.gider_detay,name='gider_detay'),

    path('raporlar',raporlar,name='raporlar'),

    path('faturalar/tum-faturalar',pages_faturalar.faturalar,name='faturalar'),
    path('faturalar/fatura-ekle',pages_faturalar.view_fatura_create,name='fatura_ekle'),
    path('faturalar/fatura-detay/<int:id>',pages_faturalar.fatura_detay,name='fatura_detay'),

    path('ayarlar',ayarlar,name='ayarlar'),
]