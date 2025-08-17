import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.page_object import pom
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Musteriler_Sayfasi(pom):
    musteriler=[]
    INPUT_NAME = (By.CSS_SELECTOR, '#id_name')
    INPUT_SURNAME = (By.CSS_SELECTOR, '#id_surname')
    INPUT_TELEFON = (By.CSS_SELECTOR, '#id_telefon')
    INPUT_MAIL = (By.CSS_SELECTOR, '#id_mail')

    AKTIF_MUSTERI_TEXT=(By.CSS_SELECTOR, '.col-md-4:nth-child(2)>div>div>p')
    TUM_AKTIF_MUSTERILER=(By.CSS_SELECTOR, '.table-striped>tbody>tr>td:nth-child(5)>span')

    PASIF_MUSTERILER_TEXT=(By.CSS_SELECTOR, '.col-md-4:last-child>div>div>p')
    PASIF_MUSTERILER_HEPSI=(By.CSS_SELECTOR, '.bg-danger')

    BUTTON =(By.CSS_SELECTOR,'.btn-primary')

    LISTE_SIL_BUTTON=(By.CSS_SELECTOR,'.table-striped>tbody>tr>td:last-child>span>a')
    SILME_ISLEMI_ONAY=(By.CSS_SELECTOR,'.justify-content-center>button')

    GUNCELLEME_BUTTON=(By.CSS_SELECTOR,'body > div.content > table > tbody > tr:nth-child(1) > td:nth-child(6) > span > a')
    
    TOPLAM_MUSTERI_ADET=(By.CSS_SELECTOR,'.col-md-4:nth-child(1)>div>div>p')

    def MusteriEkle(self, name,surname,telefon,mail):
        try:
            name=self.text_giris_islemleri(self.INPUT_NAME, name)
            surname=self.text_giris_islemleri(self.INPUT_SURNAME,surname)
            telefon=self.text_giris_islemleri(self.INPUT_TELEFON,telefon)
            mail=self.text_giris_islemleri(self.INPUT_MAIL,mail)
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


    def tablo_kontrol(self):
        musteriler = []
        rows = self.driver.find_elements(By.CSS_SELECTOR, '.table-striped>tbody>tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            musteri_bilgiler = {
                'musteri_no': cells[0].text.strip(),
                'ad_soyad': cells[1].text.strip(),
                'telefon': cells[2].text.strip(),
                'email': cells[3].text,
                'durum': cells[4].text,
            }
            musteriler.append(musteri_bilgiler)
        return musteriler

    def musteri_sayfasi_musteri_sayisi_dogru(self):
        aktif_musteri_sayisi = 0
        pasif_musteriler_sayisi = 0

        # Aktif Musteri islemleri
        aktif_musteri_text = self.driver.find_element(*self.AKTIF_MUSTERI_TEXT).text
        tum_aktif_musteriler = self.driver.find_elements(*self.TUM_AKTIF_MUSTERILER)

        # Pasif Musteri islemleri
        pasif_musteriler_text_raw = self.driver.find_element(*self.PASIF_MUSTERILER_TEXT).text
        tum_pasif_musteriler = self.driver.find_elements(*self.PASIF_MUSTERILER_HEPSI)

        for aktif in tum_aktif_musteriler:
            if aktif.text == 'Aktif':
                aktif_musteri_sayisi += 1

        for pasif in tum_pasif_musteriler:
            if pasif.text == 'Pasif':
                pasif_musteriler_sayisi += 1

        import re
        aktif_musteri_text_sayi = int(re.search(r'\d+', aktif_musteri_text).group())
        pasif_musteriler_text_sayi = int(re.search(r'\d+', pasif_musteriler_text_raw).group())

        print("🟩 Aktif text:", aktif_musteri_text_sayi,'\n' 
            "Aktif sayım:", aktif_musteri_sayisi,'\n'
            "Pasif text:", pasif_musteriler_text_sayi,'\n'
            "Pasif sayım:", pasif_musteriler_sayisi)

        return {
            'aktif_musteri_text': aktif_musteri_text_sayi,
            'aktif_musteri_sayisi': aktif_musteri_sayisi,
            'pasif_musteri_sayisi': pasif_musteriler_sayisi,
            'pasif_musteriler_text': pasif_musteriler_text_sayi
        }

    @pytest.mark.sil
    def Musteri_silme(self):
        Silinen_musteri_addet = 0
        wait = WebDriverWait(self.driver, 3)

        while True:
            try:
                elem = wait.until(EC.presence_of_all_elements_located(self.LISTE_SIL_BUTTON))
                if not elem:
                    break
                elem[0].click()
                confirm = wait.until(EC.element_to_be_clickable(self.SILME_ISLEMI_ONAY))
                confirm.click()
                Silinen_musteri_addet += 1

            except:
                break
            
        ToplamMusteri = int(self.driver.find_element(*self.TOPLAM_MUSTERI_ADET).text)
        return {'Silinen_musteri_addet':Silinen_musteri_addet,'aktif_musteri_text':ToplamMusteri+Silinen_musteri_addet}

    def Musteri_Guncelleme(self,name,surname,telefon,mail):
        try:
            self.tıklama(self.GUNCELLEME_BUTTON)
            name=self.text_giris_islemleri(self.INPUT_NAME, name)
            surname=self.text_giris_islemleri(self.INPUT_SURNAME,surname)
            telefon=self.text_giris_islemleri(self.INPUT_TELEFON,telefon)
            mail=self.text_giris_islemleri(self.INPUT_MAIL,mail)
        except Exception as e:
            print('Güncelleme işlemi gerçekleşmedi')
