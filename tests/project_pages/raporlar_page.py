import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.page_object import pom
from tests.project_pages.gelir_page import GelirSayfasi
from tests.project_pages.gider_page import Gider_Sayfasi

class Raporlar(pom):
    def AylikGelir(self):
        p4 = self.driver.find_element(By.CSS_SELECTOR, '.bg-primary>div>p').text
        return self.fiyat_guncelleme(p4)
    
    def AylikKar(self):
        p4 = self.driver.find_element(By.CSS_SELECTOR, '.bg-success>div>p').text
        return self.fiyat_guncelleme(p4)

    def AylikGider(self):
        p4 = self.driver.find_element(By.CSS_SELECTOR, '.bg-danger>div>p').text
        return self.fiyat_guncelleme(p4)
    
    def GelirSayfasi(self):
        naber=GelirSayfasi(self.driver)
        deger=naber.BadgeKontrol()
        return float(deger['Toplam Gelir'])
    
    def GiderSayfasi(self):
        naber=Gider_Sayfasi(self.driver)
        deger=naber.toplam_gider_text()['toplam_gider_text']
        return float(deger)
    

    def fiyat_guncelleme(self,selector):
        deneme=float(selector.replace('.', '').replace(',', '.').replace('₺', '').strip())
        return deneme
