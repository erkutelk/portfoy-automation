
from .models import Gider,Gelir,Fatura_Bilgileri,musteriler
from django import forms
from django.forms import TextInput,Textarea,Select,CheckboxInput,DateInput,SelectDateWidget

class gider_form(forms.ModelForm):
    class Meta:
        model=Gider
        fields=('gider_tutar','gider_aciklama','kategori','gider_durum')
        labels={'gider_tutar':'Gider Tutarı',
                'gider_aciklama':'Açıklama',
                'kategori':'kategori',
                'gider_durum':'Ödendi'},
        widgets={
            "gider_tutar":TextInput(attrs={"class":"form-control"}),
            "gider_aciklama":Textarea(attrs={"class":"form-control"}),
            "kategori":Select(attrs={"class":"form-control"}),
            'gider_durum': CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class gelir_ekleme_form(forms.ModelForm):
    class Meta:
        model=Gelir
        fields=('__all__')
        labels={
            'gelir':'Gelir Miktarı(TL)',
            'gelir_aciklama':'Açıklama',
            'kategori':'Lütfen kategori seçiniz'
        }
        widgets={
            'gelir':TextInput(attrs={'class':'form-control'}),
            'gelir_aciklama':TextInput(attrs={'class':'form-control'}),
            'kategori':Select(attrs={'class':'form-control'})

        }

class Form_Fatura(forms.ModelForm):
    class Meta:
        model = Fatura_Bilgileri
        fields = ("__all__")
        labels={'fatura':'Lütfen Fatura Tutarınızı Giriniz(TL)',
                'kategori':'Lütfen faturanın kategorisini seçiniz',
                'tarih_son_ödeme':'Faturanın son ödeme tarihini seçiniz',
                'durum':'Durum'}
        widgets = {
            'fatura': TextInput(attrs={'class': 'form-control'}),
            'kategori': Select(attrs={'class': 'form-control'}),
            'tarih_son_ödeme' : TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'YYYY-MM-DD'}),
            'durum': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class Musteriler_form(forms.ModelForm):
    class Meta:
        model = musteriler
        fields = ("__all__")
        labels={'name':'İsim Giriniz',
                'surname':'Soyisim giriniz',
                'telefon':'Telefon numarası giriniz',
                'mail':'Mail adresi Giriniz',
        },
        widgets={
            'name':TextInput(attrs={'class':'form-control'}),
            'surname':TextInput(attrs={'class':'form-control'}),
            'telefon':TextInput(attrs={'class':'form-control'}),
            'mail':TextInput(attrs={'class':'form-control'}),
        }
