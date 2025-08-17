from django.shortcuts import get_object_or_404, render,redirect
from Muhasebe.models import Gider
from django.shortcuts import render
from django.utils.timezone import now
from Muhasebe.forms import gider_form

def gider_detay(request,id):
    models = get_object_or_404(Gider, pk=id)
    if request.method == 'POST':
        form = gider_form(request.POST, instance=models)
        if form.is_valid():
            form.save() 
            return redirect('gelirler')  

    else:
        form = gider_form(instance=models)
    
    return render(request, 'gider_detay.html', {'form': form, 'models': models})


def Gider_Create(request):
    if request.method=="POST":
        form_ekle=gider_form(request.POST)
        if form_ekle.is_valid():
            form_ekle.save()
            return redirect('giderler')
    else:
        form_ekle=gider_form()
    return render(request,"Admin_page/admin_gider_ekleme.html",{'form':form_ekle})

def giderler(request):
    mevcut_tarih = now()

    giderler_obj=Gider.objects.all().order_by('gider_durum')
    toplam_gider=0
    for a in giderler_obj.filter(gider_durum=True):
        toplam_gider+=a.gider_tutar

    tarih_listesi = list(giderler_obj.filter(tarih__year=mevcut_tarih.year, tarih__month=mevcut_tarih.month,gider_durum=True))
    aylık_gider=0
    for a in tarih_listesi:
        aylık_gider+=a.gider_tutar

    bekleyen_odemeler=0
    for a in giderler_obj.filter(gider_durum=False):
        bekleyen_odemeler+=a.gider_tutar


    return render(request,'giderler.html',{'isim':giderler_obj,'toplam_gider':toplam_gider,'aylık_gider':aylık_gider,'bekleyen_odemeler':bekleyen_odemeler})

