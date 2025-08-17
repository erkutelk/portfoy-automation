import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.page_object import pom

class Gider_Sayfasi(pom):
    INPUT_GIDER_TUTAR = (By.CSS_SELECTOR, '#id_gider_tutar')
    INPUT_GIDER_ACIKLAMA = (By.CSS_SELECTOR, '#id_gider_aciklama')
    KATEGORI_SECIMI = 'kategori'

    GIDER_INCELLEME = (By.CSS_SELECTOR, '.table-striped>tbody>tr>td:nth-last-child(1)>span>a')

    BUTTON=(By.CSS_SELECTOR,'.btn-primary')

    TOPLAM_GIDER_TEXT_TOPLAM=(By.CSS_SELECTOR,'.card-text')
    TOPLAM_BEKLEYEN_ODEMELER_TEXT=(By.CSS_SELECTOR,'.col-md-4:nth-child(3)>div>div>p')
    TAMAMLANAN_ODEMELER=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:nth-child(5)>span')
    TAMAMLANAN_TUTAR=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:nth-child(3)')

    def gelir_ekleme(self, gelir_,aciklama,value):
        try:
            Gider_tutar=self.text_giris_islemleri(self.INPUT_GIDER_TUTAR, gelir_)
            Gider_aciklama=self.text_giris_islemleri(self.INPUT_GIDER_ACIKLAMA,aciklama)
            Kategori=self.select_dropdown_by_value(self.KATEGORI_SECIMI,value)
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


    def gider_guncelleme(self):
        self.driver.find_element(*self.GIDER_INCELLEME).click()
        Gider_tutar=self.text_giris_islemleri(self.INPUT_GIDER_TUTAR, '500')
        Gider_aciklama=self.text_giris_islemleri(self.INPUT_GIDER_ACIKLAMA,'Bir acıklamaa')
        Kategori=self.select_dropdown_by_value(self.KATEGORI_SECIMI,'1')
        self.tıklama(self.BUTTON)
        print('Gider güncelleme işlemleri yapııldı')
        

    def toplam_gider_text(self):
        toplam_gider_text=self.driver.find_element(*self.TOPLAM_GIDER_TEXT_TOPLAM).text.replace(',','.').replace(',','.')
        bekleyen_textler=self.driver.find_element(*self.TOPLAM_BEKLEYEN_ODEMELER_TEXT).text.replace(',','.').replace(',','.')

        return {'toplam_gider_text':toplam_gider_text,'bekleyen_textler':bekleyen_textler}

    def giderler_toplam_tamamlanamadi(self):
        Tamamlandi_Tutar = 0
        Tamamlanamadı_tutar = 0
        durumlar = self.driver.find_elements(*self.TAMAMLANAN_ODEMELER)
        tutarlar = self.driver.find_elements(*self.TAMAMLANAN_TUTAR)

        for i, durum in enumerate(durumlar):
            if durum.text.strip() == 'Tamamlandı':
                try:
                    tutar = float(tutarlar[i].text.strip().replace(',', '.'))
                    Tamamlandi_Tutar += tutar
                except ValueError:
                    print(f"Tutar dönüştürülemedi: {tutarlar[i].text}")

            else:
                tutar = float(tutarlar[i].text.strip().replace(',', '.'))
                Tamamlanamadı_tutar += tutar

        return {'Tamamlandi_Tutar':Tamamlandi_Tutar,'Tamamlanamadı':Tamamlanamadı_tutar}

