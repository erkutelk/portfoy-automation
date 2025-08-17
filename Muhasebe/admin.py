from django.contrib import admin
from .models import Gelir, GelirKategori, Gider, Gider_Kategori, Fatura_Bilgileri, Fatura_Kategori, musteriler


@admin.register(Gelir)
class GelirAdmin(admin.ModelAdmin):
    list_display = ("id", "gelir", "kategori", "tarih")
    search_fields = ("gelir_aciklama", "kategori__kategori_adi")
    list_filter = ("kategori", "tarih")


@admin.register(Gider)
class GiderAdmin(admin.ModelAdmin):
    list_display = ("id", "gider_tutar", "kategori", "tarih", "gider_durum")
    search_fields = ("gider_aciklama", "kategori__kategori_adi")
    list_filter = ("kategori", "tarih", "gider_durum")
    list_editable = ("gider_durum",) 


@admin.register(Fatura_Bilgileri)
class FaturaBilgileriAdmin(admin.ModelAdmin):
    list_display = ("id", "fatura", "kategori", "tarih", "tarih_son_ödeme", "durum")
    search_fields = ("kategori__kategori_adi",)
    list_filter = ("kategori", "durum")
    list_editable = ("durum",)


@admin.register(musteriler)
class MusteriAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "telefon", "mail", "durum", "eklenme_tarihi")
    search_fields = ("name", "surname", "mail")
    list_filter = ("durum", "eklenme_tarihi")


admin.site.register(GelirKategori)
admin.site.register(Gider_Kategori)
admin.site.register(Fatura_Kategori)
