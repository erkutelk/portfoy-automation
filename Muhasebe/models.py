from django.db import models

class GelirKategori(models.Model):
    kategori_adi = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.kategori_adi

class Gelir(models.Model):
    gelir = models.DecimalField(max_digits=10, decimal_places=2)
    gelir_aciklama = models.CharField(max_length=150, blank=True, null=True)
    kategori = models.ForeignKey(GelirKategori, on_delete=models.CASCADE, related_name="gelirler")  
    tarih = models.DateField(auto_now_add=True)
    Durum=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.gelir} TL"
    

class Gider_Kategori(models.Model):
    kategori_adi = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.kategori_adi


class Gider(models.Model):
    gider_tutar=models.DecimalField(max_digits=10,decimal_places=2)
    gider_aciklama=models.CharField(max_length=150, blank=True, null=True)
    kategori=models.ForeignKey(Gider_Kategori,on_delete=models.CASCADE,related_name="giderler")
    tarih=models.DateField(auto_now=True)
    gider_durum=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.gider_tutar} {self.gider_aciklama} {self.kategori} {self.tarih} {self.gider_durum}'

class Fatura_Kategori(models.Model):
    kategori_adi = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.kategori_adi


class Fatura_Bilgileri(models.Model):
    fatura = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Fatura_Kategori, on_delete=models.CASCADE, related_name="fatura_bilgileri")
    tarih = models.DateField(auto_now=True)
    tarih_son_ödeme = models.DateField()
    durum=models.BooleanField(default=False)  

    def __str__(self):
        return f"Fatura: {self.fatura} - Son Ödeme: {self.tarih_son_ödeme}"

class musteriler(models.Model):
    name=models.CharField(max_length=10)
    surname=models.CharField(max_length=10)
    telefon=models.CharField(max_length=11)
    mail=models.EmailField(unique=True)
    durum=models.BooleanField(default=True)
    eklenme_tarihi = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.name},{self.surname},{self.telefon},{self.mail},{self.durum},{self.eklenme_tarihi}'
    
