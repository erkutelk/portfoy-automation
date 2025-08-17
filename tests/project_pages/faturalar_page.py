import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.page_object import pom

class Faturalar_Sayfasi(pom):
    INPUT_FATURA_TUTAR = (By.CSS_SELECTOR, '#id_fatura')
    KATEGORI_SECIMI = 'kategori'
    INPUT_SON_ODEME_TARIHI = (By.CSS_SELECTOR, '#id_tarih_son_ödeme')
    BUTTON=(By.CSS_SELECTOR, '.btn-primary')

    DETAY_BUTTON=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:last-child a')


    ODENMEDI_TEXT=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:nth-child(6)>span:nth-child(1)')
    TUTAR_TABLO=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:nth-child(4)')

    def fatura_ekleme(self, Fatura_tutar,son_odeme_tarihi,kategori_value):
        Gider_tutar=self.text_giris_islemleri(self.INPUT_FATURA_TUTAR, Fatura_tutar)
        Kategori=self.select_dropdown_by_value(self.KATEGORI_SECIMI,kategori_value)
        Fatura_son_odeme_tarihi=self.text_giris_islemleri(self.INPUT_SON_ODEME_TARIHI,son_odeme_tarihi)
        self.tıklama(self.BUTTON)


    def fatura_guncelleme(self,Fatura_tutar,son_odeme_tarihi,kategori_value):
        self.tıklama(self.DETAY_BUTTON)
        Gider_tutar=self.text_giris_islemleri(self.INPUT_FATURA_TUTAR, Fatura_tutar)
        Kategori=self.select_dropdown_by_value(self.KATEGORI_SECIMI,kategori_value)
        Fatura_son_odeme_tarihi=self.text_giris_islemleri(self.INPUT_SON_ODEME_TARIHI,son_odeme_tarihi)
        self.tıklama(self.BUTTON)

    def tabloda_eklenen_son_deger(self):
        p1 = self.driver.find_element(By.CSS_SELECTOR, '.table-striped > tbody > tr:first-child>td:nth-child(2)').text
        p2 = self.driver.find_element(By.CSS_SELECTOR, '.table-striped > tbody > tr:first-child>td:nth-child(3)').text
        p3 = float(self.driver.find_element(By.CSS_SELECTOR, '.table-striped > tbody > tr:first-child>td:nth-child(4)').text.replace(',', '.'))
        p4 = self.driver.find_element(By.CSS_SELECTOR, '.table-striped > tbody > tr:first-child>td:nth-child(5)').text
        print('tutar',p3)
        return p3        
    

    def yaklasan_odemeler_adet(self):
        p4 = self.driver.find_elements(By.CSS_SELECTOR, '.list-group-item>.flex-grow-1')
        return len(p4)
    

    def TabloKontrol(self):
        ToplamTamamlandi = 0
        ToplamGelmedi = 0

        tamamlandi_list = self.driver.find_elements(*self.ODENMEDI_TEXT)
        tutar_list = self.driver.find_elements(*self.TUTAR_TABLO)

        for idx, elem in enumerate(tamamlandi_list):
            tutar = float(tutar_list[idx].text.strip().replace(',', '.'))
            if elem.text.strip() == 'Ödenmedi':
                ToplamTamamlandi += tutar
            else:
                ToplamGelmedi += tutar

        print('Ödendi : ',ToplamGelmedi)
        print('Ödenmedi : ',ToplamTamamlandi)
        return {
            "Odenmedi": f"{ToplamTamamlandi:.2f}",
            "Toplam Gelmedi": f"{ToplamGelmedi:.2f}"
        }
    
    def badge_toplam_odenicek(self):
        p4 = self.driver.find_element(By.CSS_SELECTOR, '.justify-content-center>div>div>div>p').text
        print(p4)
        return float(p4)
