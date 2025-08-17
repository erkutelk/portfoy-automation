import pytest
from tests.project_pages.faturalar_page import Faturalar_Sayfasi
import logging
from time import sleep
from datetime import datetime,timedelta

@pytest.mark.usefixtures("setup")
class TestFaturalar:
    BASE_URL = 'http://127.0.0.1:8000/faturalar/fatura-ekle'
    TUM_FATURALAR_LIST = 'http://127.0.0.1:8000/faturalar/tum-faturalar'

    @pytest.mark.parametrize(
        'tutar,tarih,DropDown', [
            ('1231', '2025-12-01', '2'),
            ('aaa', '', '1'),
            (' ', ' ', '1'),
            ('1500', '2025-10-05', '1'),
            ('', '', 0)
        ]
    )
    def test_fatura_bilgileri_girme(self, tutar, tarih, DropDown):
        """Fatura ekleme işlemi testleri"""
        Gonderilen_bilgiler = {
            'Fatura_Tarihi': tutar,
            'DropDown_Secimi': DropDown,
            'tarih': tarih,
        }
        
        self.driver.get(self.BASE_URL)

        faturalar_page = Faturalar_Sayfasi(self.driver)
        faturalar_page.fatura_ekleme(
            Gonderilen_bilgiler['Fatura_Tarihi'],
            Gonderilen_bilgiler['tarih'],
            Gonderilen_bilgiler['DropDown_Secimi']
        )
        faturalar_page.button_click()

    def test_fatura_guncelleme(self):
        """Fatura güncelleme ve fatura listede gözüküyor mu """
        from random import randint
        from datetime import datetime
        # Fatura Ekleme işlemleri
        randomFiyatGuncelleme=randint(1,1000)
        self.driver.get(self.BASE_URL)
        faturalar = Faturalar_Sayfasi(self.driver)
        tarih = datetime.now().strftime('%Y-%m-%d')
        faturalar.fatura_ekleme('150', tarih, '1')

        print(f"🟩Eklenen Fatura\nTutar : 150\nTarih : {tarih}\nKategori':1\n")

        # Fatura güncelleme sayfası
        self.driver.get(self.TUM_FATURALAR_LIST)
        faturalar.fatura_guncelleme(randomFiyatGuncelleme, tarih, '1')
        eklenenSonDeger=faturalar.tabloda_eklenen_son_deger()
        print(f'{eklenenSonDeger}=={float(randomFiyatGuncelleme)}')
        assert float(randomFiyatGuncelleme) == eklenenSonDeger, 'Eklenen değer güncellenmedi'

    @pytest.mark.guncelleme
    def test_yaklasan_odemeler_dogru_calisiyor_mu(self):
        """Yaklaşan ödeme tarihi 3 gün kalan ödemeler"""
        tarih = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        Fatura=Faturalar_Sayfasi(self.driver)
        self.driver.get(self.TUM_FATURALAR_LIST)
        adet=Fatura.yaklasan_odemeler_adet()+1


        sleep(1)
        self.driver.get(self.BASE_URL)
        Fatura.fatura_ekleme('1231',f'{tarih}','1')

        self.driver.get(self.TUM_FATURALAR_LIST)
        adet2=Fatura.yaklasan_odemeler_adet()

        assert adet==adet2

    @pytest.mark.tablo_kontrol
    def test_tutar_dogru_mu(self):
        self.driver.get(self.TUM_FATURALAR_LIST)
        fatura=Faturalar_Sayfasi(self.driver)
        assert fatura.badge_toplam_odenicek()==float(fatura.TabloKontrol()['Odenmedi'])

