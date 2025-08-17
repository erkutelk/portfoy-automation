import pytest
from tests.project_pages.musteriler_page import Musteriler_Sayfasi
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from time import time

@pytest.mark.usefixtures("setup")
class TestFaturalar:
    BASE_URL = 'http://127.0.0.1:8000/musteriler/musteri-ekle'
    MUSTERI_EKLEME_SAYFASI='http://127.0.0.1:8000/musteriler/tum-musteriler'

    @pytest.mark.parametrize(
        'name,surname,telefon,mail,hata_mesaji', [
            ('erkut', 'elik', '11111111111', 'erkutelik@gmail.com', ''),
            ('Ali', 'Veli', '11111111111', 'erkutcelik@gmail.com', ''), 
            ('erkut', 'elik', '111111111', 'erkutelik@gmail.com', 'Telefon numarasını doğru giriniz'),
            ('erkut', '', '11111111111', 'erkutelik@gmail.com', 'Soyisim alanı doğru değil'),
            ('erkut', 'elik', '', 'erkutelik@gmail.com', 'Telefon numarasını lütfen giriniz'),
            ('erkut', 'elik', '11111111111', '', 'Lütfen mail adresinizi giriniz'),
            ('', '', '', '', 'Lütfen bir değer giriniz'),
            (' ', ' ', ' ', ' ', 'lütfen bir değer giriniz'),
            ('-', '-', '-', '-', 'Lütfen bir değer giriniz'),
            ('😎', '😎', '😎', '😎', 'Lütfen emoji kullanmayınız'),
            ('1111111111111111111111111111111111111111', '1111111111111111111111111111111111111111', '1111111111111111111111111111111111111111','1111111111111111111111111111111111111111','Lütfen karekter uzunluğunu kısaltın'),
        ]
    )
    def test_kullanici_olusturma(self, name, surname, telefon, mail, hata_mesaji):
        """Yeni bir kullanıcı ekleme işlemi"""
        logging.info('--TEST-YENI-KULLANICI-OLUSTURMA--\n')
        self.driver.get(self.BASE_URL)
        musteriler_sayfasi = Musteriler_Sayfasi(self.driver)
        musteriler_sayfasi.MusteriEkle(name, surname, telefon, mail)
        logging.info(f'🟩name : {name}surname : {surname}telefon : {telefon}mail : {mail}')
        if hata_mesaji == '':
            assert "musteriler" in self.driver.current_url
        else:
                hata_element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(("css selector", ".error-message"))
                )
                assert hata_mesaji in hata_element.text



    bilgiler={'isim':f'{int(time())}',
              'soyisim':'test',
              'telefon':'11111111111',
              'email':f'erkutelik@gmail{int(time())}.com',}

    def test_eklenen_urun_listede_gozukuyor_mu(self):
        """ Eklenen müşteri listede gözüküyor mu"""
        logging.info('EKLENEN-MUSTERI-LISTEDE-GOZUKMESI-TESTI\n')
        self.driver.get(self.BASE_URL)
        sayfa = Musteriler_Sayfasi(self.driver)
        sayfa.MusteriEkle(f"{self.bilgiler['isim']}", self.bilgiler['soyisim'], 
                           self.bilgiler['telefon'], self.bilgiler['email'])
        logging.info(f"Kullanıcısı Ekleniyor:\n{self.bilgiler['isim']},{self.bilgiler['soyisim']},{self.bilgiler['telefon']},{self.bilgiler['email']}")
        self.driver.get(self.MUSTERI_EKLEME_SAYFASI)

        deger = sayfa.tablo_kontrol()
        son_musteri = deger[-1]
        print(f'{son_musteri['ad_soyad']}')
        print(f'{self.bilgiler['isim']}')
        logging.info(f'Listede gözüken son müşteriler:\n{son_musteri['ad_soyad']}{self.bilgiler['isim']}')

        assert son_musteri['ad_soyad'] == f"{self.bilgiler['isim']}"
        assert son_musteri['telefon'] == f"{self.bilgiler['telefon']}"

    def test_musteri_sayilari_dogurmu_konttrol_ediliyor(self):
        self.driver.get(self.MUSTERI_EKLEME_SAYFASI)
        sayfa = Musteriler_Sayfasi(self.driver)

        musteriler_adet_text=sayfa.musteri_sayfasi_musteri_sayisi_dogru()
        aktif_musteri_text_degeri=musteriler_adet_text['aktif_musteri_text']
        aktif_musteri_text_sayisi=musteriler_adet_text['aktif_musteri_sayisi']
        Pasif_musteri_text=musteriler_adet_text['pasif_musteri_sayisi']
        Pasif_musteri_degeri=musteriler_adet_text['pasif_musteriler_text']
        print('🟩Aktif_musteri_text_degeri : ',aktif_musteri_text_degeri,'aktif_musteri_text_sayisi : ',aktif_musteri_text_sayisi,'Pasif Müşteri Sayısı',Pasif_musteri_text,'Pasif_musteri_degeri',Pasif_musteri_degeri)
        assert aktif_musteri_text_degeri==aktif_musteri_text_sayisi,'Musteri sayfaları ile birbirlerinden farklı'
        print(f'Pasif durumda olan kullanıcı sayısı{Pasif_musteri_degeri} Sitede yazana kullanıcı sayısı: {Pasif_musteri_text}')
        assert Pasif_musteri_degeri==Pasif_musteri_text
    
    @pytest.mark.sil
    def test_musteri_silme(self):
        self.driver.get(self.BASE_URL)
        musteriler_sayfasi = Musteriler_Sayfasi(self.driver)
        for a in range(0,3):
            musteriler_sayfasi.MusteriEkle(f'erkut{int(time())}','elik','11111111111',f'erkutelik@gmail.com{int(time())}')
            
        self.driver.get(self.MUSTERI_EKLEME_SAYFASI)
        sonuc = musteriler_sayfasi.Musteri_silme()
        assert sonuc['Silinen_musteri_addet'] == sonuc['aktif_musteri_text']

        
    def test_musteri_guncelleme(self):
        self.driver.get(self.BASE_URL)
        musteriler_sayfasi = Musteriler_Sayfasi(self.driver)
        musteriler_sayfasi.MusteriEkle(f'Guncel{int(time())}','elik','11111111111',f'erkutelik@gmail.com{int(time())}')
        self.driver.get(self.MUSTERI_EKLEME_SAYFASI)
        musteriler_sayfasi.Musteri_Guncelleme(f'Guncel{int(time())}','elik','11111111111',f'erkutelik@gmail.com{int(time())}')
