from django.utils.timezone import now
from Muhasebe.models import Fatura_Bilgileri
from django.shortcuts import render
from django.db.models import Sum
from Muhasebe.forms import Form_Fatura
from django.shortcuts import get_object_or_404,redirect

def view_fatura_create(request):
    if request.method=='POST':
        form_fatura=Form_Fatura(request.POST)
        if form_fatura.is_valid():
            form_fatura.save()
    else:
        form_fatura=Form_Fatura()

    return render(request,'Admin_page/admin_fatura_ekleme.html',{'form':form_fatura})



def faturalar(request):
    mevcut_tarih = now().date()
    yaklasan_son_odemeler = Fatura_Bilgileri.objects.filter(tarih_son_ödeme__gte=mevcut_tarih,durum=False)

    hesap_tarih = [] 
    gecikmis_faturaların_tutarlari=0
    for fatura in yaklasan_son_odemeler:
        fark = (fatura.tarih_son_ödeme - mevcut_tarih).days
        if fark <= 3:
            hesap_tarih.append(f"Fatura: {fatura.id} {fark} gün kaldı.")
            gecikmis_faturaların_tutarlari += fatura.fatura

    if not hesap_tarih:
        hesap_tarih.append("Yaklaşan bir fatura yok.")

    toplam_odenicek = Fatura_Bilgileri.objects.filter(durum=False).aggregate(total=Sum('fatura'))['total'] or 0
    deger = Fatura_Bilgileri.objects.all().order_by('durum', '-tarih_son_ödeme')

    return render(request, 'faturalar.html', {'deger': deger, 'toplam_odenicek': toplam_odenicek, 'hesap_tarih': hesap_tarih,'gecikmis_faturaların_tutarlari':gecikmis_faturaların_tutarlari})

def fatura_detay(request,id):
    models =get_object_or_404(Fatura_Bilgileri,pk=id)

    if request.method=='POST':
        form = Form_Fatura(request.POST, instance=models)
        if form.is_valid():
            form.save() 
            return redirect('faturalar')  

    else:
        form = Form_Fatura(instance=models)
    
    return render(request, 'fatura_detay.html', {'form': form, 'models': models})