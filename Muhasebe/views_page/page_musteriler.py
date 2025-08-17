from Muhasebe.models import musteriler
from django.shortcuts import get_object_or_404, redirect, render
from Muhasebe.forms import Musteriler_form
def musteriler_ekle(request):
    if request.method=='POST':
        form_musteri_ekle=Musteriler_form(request.POST)
        if form_musteri_ekle.is_valid():
            form_musteri_ekle.save()
    else:
        form_musteri_ekle=Musteriler_form()
    
    return render(request,'Admin_page/admin_musteri_ekleme.html',{'form':form_musteri_ekle})
def musteriler_(request):
    deger=musteriler.objects.all()
    Musteri_adet=deger.count()
    Musteri_aktif=musteriler.objects.filter(durum=True).count()
    pasif_musteri=musteriler.objects.filter(durum=False).count() or 0

    return render(request,'musteriler.html',{'deger':deger,'musteri_adet':Musteri_adet,'Aktif_musteri':Musteri_aktif,'pasif_musteri':pasif_musteri})


def musteriler_detay(request,id):
    models = get_object_or_404(musteriler, pk=id)
    if request.method=='POST':
        deger=Musteriler_form(request.POST,instance=models)
        if deger.is_valid():
            deger.save()
            return redirect('musteriler')  
    else:
        form = Musteriler_form(instance=models)
    
    return render(request, 'musteriler_detay.html', {'form': form, 'models': models})


def musteri_sil(request,id):
        musteri_object = get_object_or_404(musteriler, pk=id)
        if request.method == 'POST':
            musteri_object.delete()
            return redirect('musteriler')
        
        return render(request, 'musteri_sil.html', {'musteri': musteri_object})



