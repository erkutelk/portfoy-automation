from django.shortcuts import get_object_or_404, redirect, render
from Muhasebe.models import Gelir,Gider
from django.shortcuts import render
from django.utils.timezone import now
from Muhasebe.forms import gelir_ekleme_form


def gelir_create(request):
    if request.method=='POST':
        form_gelir_ekleme=gelir_ekleme_form(request.POST)
        if form_gelir_ekleme.is_valid():
            form_gelir_ekleme.save()
            return redirect('gelirler')
    
    else:
        form_gelir_ekleme=gelir_ekleme_form()
    
    return render(request,'Admin_page/admin_gelir_ekleme.html',{'form':form_gelir_ekleme})



def gelir_detay(request, id):
    models = get_object_or_404(Gelir, pk=id)
    
    if request.method == 'POST':
        form = gelir_ekleme_form(request.POST, instance=models)
        
        if form.is_valid():
            form.save() 
            # return redirect('gelirler_detail', id=models.pk)  
            return redirect('gelirler')  

    else:
        form = gelir_ekleme_form(instance=models)
    
    return render(request, 'gelir_detay.html', {'form': form, 'models': models})


def gelirler(request):
    deger=Gelir.objects.all().order_by('Durum')

    toplam=0
    for a in deger:
        toplam+=a.gelir

    mevcut_tarih = now()

    tarih_listesi = list(Gelir.objects.filter(tarih__year=mevcut_tarih.year, tarih__month=mevcut_tarih.month,Durum=True))
    aylık_gelir=0
    for a in tarih_listesi:
        aylık_gelir+=a.gelir


    bekleyen_odemeler=0
    for a in Gider.objects.filter(gider_durum=False):
        bekleyen_odemeler+=a.gider_tutar

    return render(request,'gelirler.html',{'isim':deger,'toplam':toplam,'tarih':aylık_gelir,'bekleyen_odemeler':bekleyen_odemeler})
