import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.page_object import pom

class GelirSayfasi(pom):
    INPUT_GELIR_MIKTAR = (By.CSS_SELECTOR, '#id_gelir')
    INPUT_ACIKLAMA = (By.CSS_SELECTOR, '#id_gelir_aciklama')
    DROP_DOWN = 'kategori'
    BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary.w-100')


    ORNEK_HATA_KONTROL='div.error-message'# Bu sınıf projede yok sadece deneme amaçlı açıldı hata tespiti için

    GUNCELLEME_BUTTON=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:last-child>span>a')

    TOPLAM_GELIR_BADGE_TEXT=(By.CSS_SELECTOR,'.text-bg-success>.card-body>p')
    TOPLAM_AYLIK_GELIR_TEXT=(By.CSS_SELECTOR,'.col-md-4:nth-child(2) .card-text')



    TABLO_TAMAMLANDI_TEXT=(By.CSS_SELECTOR,'.bg-success')
    TABLO_GELMEDI_TEXT=(By.CSS_SELECTOR,'.bg-danger')


    LISTE_KATEGORİ=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:nth-child(2)')
    
    LISTE_TUTAR=(By.CSS_SELECTOR,'.table-striped>tbody>tr:last-child>td:nth-child(3)')

    LISTE_DURUM=(By.CSS_SELECTOR,'.table-striped>tbody>tr:last-child>td:nth-child(4)')

    def gelir_ekleme(self, gelir_,aciklama,value):
        try:
            gelir_girme=self.text_giris_islemleri(self.INPUT_GELIR_MIKTAR, gelir_)
            aciklama_girme=self.text_giris_islemleri(self.INPUT_ACIKLAMA,aciklama)
            kategori_secme=self.select_dropdown_by_value(self.DROP_DOWN, value)
            self.tıklama(self.BUTTON)
        except Exception as e:
            print('hata',e)

    def MesajKontrol(self, beklenen_mesaj: str) -> bool:
        try:
            elem = self.driver.find_element_by_css_selector(self.ORNEK_HATA_KONTROL)
            gercek_mesaj = elem.text.strip()
            return beklenen_mesaj in gercek_mesaj
        except Exception:
            return beklenen_mesaj == ""

    def GuncellemeSayfasi(self,gelir_,aciklama,value):
        self.tıklama(self.GUNCELLEME_BUTTON)
        gelir_girme=self.text_giris_islemleri(self.INPUT_GELIR_MIKTAR, gelir_)
        aciklama_girme=self.text_giris_islemleri(self.INPUT_ACIKLAMA,aciklama)
        kategori_secme=self.select_dropdown_by_value(self.DROP_DOWN, value)
        self.tıklama(self.BUTTON)

    def BadgeKontrol(self):
        toplamGelir = self.driver.find_element(*self.TOPLAM_GELIR_BADGE_TEXT)
        toplamGider = self.driver.find_element(*self.TOPLAM_AYLIK_GELIR_TEXT)
        return {
            'Toplam Gelir': toplamGelir.text.replace('.', '').replace(',', '.').replace('₺', '').strip(),
            'Toplam Gider': toplamGider.text.replace('.', '').replace(',', '.').replace('₺', '').strip()
        }
    
    def TabloKontrol(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, '.table-striped>tbody>tr')
        ToplamTamamlandi = 0
        ToplamGelmedi = 0

        for row in rows:
            durum = row.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text.strip()
            tutar = float(row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text.strip().replace(',', '.'))
            if durum == 'Tamamlandı':
                ToplamTamamlandi += tutar
            else:
                ToplamGelmedi += tutar



        return {
            "Toplam Tamamlandı": f"{ToplamTamamlandi:.2f}",
            "Toplam Gelmedi": f"{ToplamGelmedi:.2f}"
        }
    
    def EklenenGelirListedeGozukuyor(self):
        listeKategori = self.driver.find_element(*self.LISTE_KATEGORİ).text
        listeTutar = float(self.driver.find_element(*self.LISTE_TUTAR).text.replace(',','.'))
        listeDurum = self.driver.find_element(*self.LISTE_DURUM).text
        return {'listeKategori':listeKategori,'listeTutar':listeTutar,'listeDurum':listeDurum}
