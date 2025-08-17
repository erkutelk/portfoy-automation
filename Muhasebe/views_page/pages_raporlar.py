from django.shortcuts import render
from django.db.models import Sum
from django.utils.timezone import now
from Muhasebe.models import Gelir, Gider, Fatura_Bilgileri

def aylik_verileri_getir(yil):
    aylik_veriler = []
    
    for ay in range(1, 13):
        gelir = Gelir.objects.filter(tarih__year=yil, tarih__month=ay,Durum=True).aggregate(total=Sum('gelir'))['total'] or 0
        gider = Gider.objects.filter(tarih__year=yil, tarih__month=ay, gider_durum=True).aggregate(total=Sum('gider_tutar'))['total'] or 0
        fatura_gider = Fatura_Bilgileri.objects.filter(durum=True, tarih__year=yil, tarih__month=ay).aggregate(total=Sum('fatura'))['total'] or 0
        
        toplam_gider = gider + fatura_gider
        kar = gelir - toplam_gider
        
        aylik_veriler.append({
            'ay': f"{ay}/{yil}",
            'gelir': gelir,
            'gider': toplam_gider,
            'kar': kar,
        })
    
    return aylik_veriler

def raporlar(request):
    mevcut_tarih = now()
    yil = mevcut_tarih.year
    ay = mevcut_tarih.month
    
    aylik_veriler = aylik_verileri_getir(yil)
    
    # Genel toplamlar
    toplam_gelir = sum(item['gelir'] for item in aylik_veriler)
    toplam_gider = sum(item['gider'] for item in aylik_veriler)
    toplam_kar = toplam_gelir - toplam_gider 

    aylik_gelir = Gelir.objects.filter(tarih__year=yil, tarih__month=ay,Durum=True).aggregate(total=Sum('gelir'))['total'] or 0
    aylik_gider = Gider.objects.filter(tarih__year=yil, tarih__month=ay, gider_durum=True).aggregate(total=Sum('gider_tutar'))['total'] or 0
    fatura_aylik_gider = Fatura_Bilgileri.objects.filter(tarih__year=yil, tarih__month=ay, durum=True).aggregate(total=Sum('fatura'))['total'] or 0
    
    toplam_aylik_gider = (aylik_gider or 0) + (fatura_aylik_gider or 0)
    aylik_kar = aylik_gelir - toplam_aylik_gider  

    context = {
        'mevcut_tarih': mevcut_tarih.strftime("%m/%Y"),
        'aylik_veriler': aylik_veriler,
        'toplam_gelir': toplam_gelir,
        'toplam_gider': toplam_gider,
        'toplam_kar': toplam_kar, 
        'aylik_gelir': aylik_gelir,
        'aylik_gider': toplam_aylik_gider,
        'aylik_kar': aylik_kar,
    }
    
    return render(request, 'raporlar.html', context)
