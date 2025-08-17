import pytest
from tests.project_pages.gelir_page import GelirSayfasi
import logging
from time import sleep
from random import randint,uniform

@pytest.mark.usefixtures("setup")
class TestGelirPage:
    BASE_URL='http://127.0.0.1:8000/gelirler/gelir-ekle'
    TUM_GELIRLER='http://127.0.0.1:8000/gelirler/tum-gelirler'

    @pytest.mark.parametrize(
        'GelirMiktarı,aciklama,DropDown,Hata_Mesajı',[
        ('','baaa','1','Lütfen Gelir Miktarı Mesajı Giriniz'),
        ('aaa','','1','Lütfen Acıklama Giriniz'),
        (' ',' ','1','Lütfen bir değer giriniz'),
        ('1500',' Deneme-test','1',''),
        ('','',0,'Geçerli değerler giriniz lütfen')])
    def test_siteye_bilgi_girme(self,GelirMiktarı,aciklama,DropDown,Hata_Mesajı):
        Gonderilen_bilgiler={
            'Gelir Miktarı':GelirMiktarı,
            'Aciklama':aciklama,
            'Drop-Down-Secimi':DropDown}
        
        self.driver.get(self.BASE_URL)
        gelir_page_create=GelirSayfasi(self.driver)
        gelir_page_create.gelir_ekleme(Gonderilen_bilgiler['Gelir Miktarı'],
                                       Gonderilen_bilgiler['Aciklama'],
                                       Gonderilen_bilgiler['Drop-Down-Secimi'])
        assert gelir_page_create.MesajKontrol(Hata_Mesajı)
        
        try:
            logging.info(f'🟩 Bilgileri girildi : {Gonderilen_bilgiler.items()}')
        except Exception as e:
            print(logging.error(f'Hata:{e}'))
            raise

    def test_gelir_guncelleme(self):
        guncellemeEkleme={
            'Gelir':randint(1,100),
            'Aciklama':randint(1,100),
            'Value':'1'
        }

        self.driver.get('http://127.0.0.1:8000/gelirler/tum-gelirler')
        Gelir_sayfasi=GelirSayfasi(self.driver)
        Gelir_sayfasi.GuncellemeSayfasi(
            guncellemeEkleme['Gelir'],
            guncellemeEkleme['Aciklama'],
            guncellemeEkleme['Value'])
    
    def test_badge_kontrol(self):
        self.driver.get('http://127.0.0.1:8000/gelirler/tum-gelirler')
        gelirSayfasi=GelirSayfasi(self.driver)
        toplamGelir=gelirSayfasi.BadgeKontrol()
        test1=toplamGelir['Toplam Gelir']
        test2=toplamGelir['Toplam Gider']
        Tablo_TUTARLAR=gelirSayfasi.TabloKontrol()

        ToplamTamamlandı=Tablo_TUTARLAR['Toplam Tamamlandı']
        ToplamGelmedi=Tablo_TUTARLAR['Toplam Gelmedi']

        print(f'Toplam Gelir : {test1} | Toplam Gider : {test2} ')
        print(f'ToplamTamamlandı : {ToplamTamamlandı} | ToplamGelmedi : {ToplamGelmedi}')
        
    @pytest.mark.isim
    def test_eklenen_gelir_listede_gozukmesi_kontrolu(self):
        tutar=randint(1,1000)
        aciklama=f'isim{randint(1,100)}'
        Dropdown='1'

        
        self.driver.get(self.BASE_URL)
        gelir_sayfasi_ekleme=GelirSayfasi(self.driver)
        gelir_sayfasi_ekleme.gelir_ekleme(tutar,aciklama,Dropdown)
        self.driver.get(self.TUM_GELIRLER)
        gelir_tutar = gelir_sayfasi_ekleme.EklenenGelirListedeGozukuyor()

        assert float(tutar) == gelir_tutar['listeTutar'], 'Tutar doğru değil'
        assert aciklama == gelir_tutar['listeDurum'], 'Açıklama doğru değil'
        assert 'Gelen Borçlar' == gelir_tutar['listeKategori'], 'Dropdown doğru değil'


