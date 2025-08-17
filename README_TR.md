
# Otomasyon Testleri
**Bu doküman Türkçe versiyondur. İngilizce için lütfen tıklayın [README.md](README.md).**

Bu proje, Python **pytest** framework kullanılarak geliştirilen bir web otomasyon test projesidir. Testler, gelir, gider, faturalar ve müşteriler sayfalarını kapsayan fonksiyonel testleri içerir.


## Gereksinimler

* Python 3.10+
* Selenium
* Pytest
* WebDriver (ChromeDriver veya tercih edilen tarayıcı)
* Logging modülü



## Test Yapısı

Proje, her bir modül için ayrı test sınıfları ve fonksiyonlar içerir:

### 1. Gelir Testleri

**Dosya:** `tests/test_gelirler.py`

* `test_siteye_bilgi_girme`: Gelir ekleme formundaki validasyon kontrolleri.
* `test_gelir_guncelleme`: Gelir güncelleme işlemi.
* `test_badge_kontrol`: Sayfadaki gelir/gider toplamlarını ve tablo değerlerini kontrol eder.
* `test_eklenen_gelir_listede_gozukmesi_kontrolu`: Eklenen gelirin listede doğru şekilde göründüğünü kontrol eder.

**Parametrized Test Örneği:**

```python
@pytest.mark.parametrize(
    'GelirMiktarı,aciklama,DropDown,Hata_Mesajı', [
        ('','baaa','1','Lütfen Gelir Miktarı Mesajı Giriniz'),
        ('aaa','','1','Lütfen Acıklama Giriniz'),
        (' ',' ','1','Lütfen bir değer giriniz'),
        ('1500',' Deneme-test','1',''),
        ('','',0,'Geçerli değerler giriniz lütfen')
    ]
)
```

---

### 2. Gider Testleri

**Dosya:** `tests/test_giderler.py`

* `test_gider_ekleme`: Gider ekleme formu validasyonları.
* `test_gider_guncelleme`: Gider güncelleme işlemleri.
* `test_badge_kontrol_islemleri`: Sayfa üzerindeki toplam gider ve bekleyen giderlerin kontrolü.

---

### 3. Faturalar Testleri

**Dosya:** `tests/test_faturalar.py`

* `test_fatura_bilgileri_girme`: Fatura ekleme işlemlerini test eder.
* `test_fatura_guncelleme`: Eklenen faturanın doğru şekilde güncellenip güncellenmediğini kontrol eder.
* `test_yaklasan_odemeler_dogru_calisiyor_mu`: Yaklaşan ödemelerin doğru sayıda listelendiğini kontrol eder.
* `test_tutar_dogru_mu`: Toplam ödenecek tutarın tablo ile uyumunu kontrol eder.

---

### 4. Müşteri Testleri

**Dosya:** `tests/test_musteriler.py`

* `test_kullanici_olusturma`: Yeni kullanıcı ekleme ve validasyon testleri.
* `test_eklenen_urun_listede_gozukuyor_mu`: Eklenen müşterinin listede doğru görünüp görünmediği.
* `test_musteri_sayilari_dogurmu_konttrol_ediliyor`: Aktif ve pasif müşteri sayılarının kontrolü.
* `test_musteri_silme`: Müşteri silme işleminin doğruluğu.
* `test_musteri_guncelleme`: Müşteri bilgilerini güncelleme testi.

---

### 5. Raporlar Testleri

**Dosya:** `tests/test_raporlar.py`

* `test_gelir_gider_raporlar_sayfasi_ile_ayni_mi`: Gelir ve gider raporlarının aylık rapor sayfasındaki değerlerle eşleşip eşleşmediğini kontrol eder.

---

## Kullanım


1. Testler çalıştırılır:

```bash
pytest -v --html=rapor.html
```

2. Belirli marker ile test çalıştırma:

```bash
pytest -m guncelleme
pytest -m isim
pytest -m sil
```

---

## Logging

Testler sırasında tüm başarılı ve başarısız işlemler loglanır. Örnek:

```
🟩 Bilgileri girildi : dict_items([('Gelir Miktarı', '1500'), ('Aciklama', 'Deneme-test'), ('Drop-Down-Secimi', '1')])
🟩 Gider ekleme testi başarılı
```

---

## Notlar

* Her test, bağımsız çalışabilir ve lokal sunucu adresi `http://127.0.0.1:8000` kullanılarak çalıştırılır.
* Test verileri **parametrize** dekoratörü ile sağlanır, böylece farklı senaryolar kolayca test edilebilir.

---
