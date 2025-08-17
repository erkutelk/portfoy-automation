from django.shortcuts import render
from django.db.models import Sum
import json
from Muhasebe.models import Gelir, Gider, Fatura_Bilgileri, musteriler
from django.utils import timezone

from django.shortcuts import render
from django.db.models import Sum
import json
from django.utils import timezone
from decimal import Decimal

def anasayfa(request):
    mevcut_yil = timezone.now().year
    mevcut_ay = timezone.now().month

    aylik_gelir__ = Gelir.objects.filter(tarih__year=mevcut_yil, tarih__month=mevcut_ay).aggregate(total=Sum('gelir'))['total'] or 0

    toplam_gelir = Gelir.objects.aggregate(Sum('gelir'))['gelir__sum'] or 0
    toplam_gider = Gider.objects.filter(gider_durum=True).aggregate(Sum('gider_tutar'))['gider_tutar__sum'] or 0
    fatura_gider = Fatura_Bilgileri.objects.filter(durum=True).aggregate(total=Sum('fatura'))['total'] or 0
    en_son_eklenen_musteri = musteriler.objects.all().order_by('eklenme_tarihi')[:6]
    toplam_musteri = musteriler.objects.count()
    bekleyen_faturalar = Fatura_Bilgileri.objects.filter(durum=False).aggregate(Sum('fatura'))['fatura__sum'] or 0

    toplam_gelir = float(toplam_gelir)
    toplam_gider = float(toplam_gider + fatura_gider)

    p1 = Fatura_Bilgileri.objects.filter(durum=False)

    aylik_veriler = []
    mevcut_yil = timezone.now().year
    for ay in range(1, 13):
        aylik_gelir = Gelir.objects.filter(tarih__year=mevcut_yil, tarih__month=ay).aggregate(Sum('gelir'))['gelir__sum'] or 0
        aylik_gider = Gider.objects.filter(tarih__year=mevcut_yil, tarih__month=ay, gider_durum=True).aggregate(Sum('gider_tutar'))['gider_tutar__sum'] or 0
        aylik_gider_fatura=Fatura_Bilgileri.objects.filter(tarih__year=mevcut_yil,tarih__month=ay,durum=True).aggregate(Sum('fatura'))['fatura__sum'] or 0

        aylik_gelir = float(aylik_gelir) if aylik_gelir else 0.0
        aylik_gider = float(aylik_gider)+float(aylik_gider_fatura) if aylik_gider else 0.0

        aylik_veriler.append({
            'ay': ay,
            'gelir': aylik_gelir,
            'gider': aylik_gider,
        })

    aylar = [
        'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
        'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'
    ]
    aylik_gelirler = [veri['gelir'] for veri in aylik_veriler]
    aylik_giderler = [veri['gider'] for veri in aylik_veriler]

    context = {
        'toplam_gelir': aylik_gelir__,
        'toplam_gider': toplam_gider,
        'toplam_musteri': toplam_musteri,
        'bekleyen_faturalar': bekleyen_faturalar,
        'en_son_eklenen_musteri': en_son_eklenen_musteri,
        'Odenmesi_gereken_faturalar': p1,
        'aylar_json': json.dumps(aylar),
        'aylik_gelirler_json': json.dumps(aylik_gelirler),
        'aylik_giderler_json': json.dumps(aylik_giderler),
    }

    return render(request, 'anasayfa.html', context)