import pytest
from tests.project_pages.gider_page import Gider_Sayfasi
import logging
from time import sleep
@pytest.mark.usefixtures("setup")
class TestGider:
    BASE_URL='http://127.0.0.1:8000/giderler/ekle'

    @pytest.mark.parametrize(
        'Gider_aciklama,aciklama,DropDown,Hata_Mesajı',[
        ('','baaa','1','Lütfen Gelir Miktarı Mesajı Giriniz'),
        ('aaa','','1','Lütfen Acıklama Giriniz'),
        (' ',' ','1','Lütfen bir değer giriniz'),
        ('1500',' Deneme-test','1',''),
        ('','',0,'Geçerli değerler giriniz lütfen')])
    
    def test_gider_ekleme(self,Gider_aciklama,aciklama,DropDown,Hata_Mesajı):
        Gonderilen_bilgiler={
            'Gelir Miktarı':Gider_aciklama,
            'Aciklama':aciklama,
            'Drop-Down-Secimi':DropDown}
        
        self.driver.get(self.BASE_URL)
        gelir_page_create=Gider_Sayfasi(self.driver)
        gelir_page_create.gelir_ekleme(Gonderilen_bilgiler['Gelir Miktarı'],
                                       Gonderilen_bilgiler['Aciklama'],
                                       Gonderilen_bilgiler['Drop-Down-Secimi'])
        assert gelir_page_create.MesajKontrol(Hata_Mesajı), logging.error(f"🟥 Beklenen hata mesajı '{Hata_Mesajı}' bulunamadı.\n{dict(Gonderilen_bilgiler)}")
        logging.info(f'🟩 Gider ekleme testi başarılı')

    
    def test_gider_guncelleme(self):
        self.driver.get('http://127.0.0.1:8000/giderler')
        giderler_sayfasi=Gider_Sayfasi(self.driver)
        giderler_sayfasi.giderler_toplam_tamamlanamadi()
        giderler_sayfasi.gider_guncelleme()
        logging.info('🟩 Gider güncelleme başarılı')

    @pytest.mark.isim
    def test_badge_kontrol_islemleri(self):
        self.driver.get('http://127.0.0.1:8000/giderler')
        giderler_sayfasi=Gider_Sayfasi(self.driver)
        giderler_tutar=giderler_sayfasi.giderler_toplam_tamamlanamadi()
        Badge_textleri=giderler_sayfasi.toplam_gider_text()
        assert float(giderler_tutar['Tamamlandi_Tutar']) == float(Badge_textleri['toplam_gider_text']),logging.info(f'Beklenen: {float(giderler_tutar["Tamamlandi_Tutar"])} \n| Gelen:{float(Badge_textleri["toplam_gider_text"])}')
        assert giderler_tutar['Tamamlanamadı'] == float(Badge_textleri['bekleyen_textler']),logging.info(f'Beklenen: {float(giderler_tutar["Tamamlanamadı"])} \n| Gelen: {float(Badge_textleri["bekleyen_textler"])}')

        logging.info('🟩 Badge Kontrolleri başarılı')




        
