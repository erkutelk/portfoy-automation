import pytest
from tests.project_pages.raporlar_page import Raporlar
import logging
from time import sleep
from datetime import datetime,timedelta

@pytest.mark.usefixtures("setup")
class TestRaporlar:
    def test_gelir_gider_raporlar_sayfasi_ile_ayni_mi(self):
        self.driver.get('http://127.0.0.1:8000/gelirler/tum-gelirler')
        value=Raporlar(self.driver)
        gelirSayfasi=value.GelirSayfasi()


        self.driver.get('http://127.0.0.1:8000/giderler')
        gider_sayfasi_giderler=value.GiderSayfasi()

        self.driver.get('http://127.0.0.1:8000/raporlar')

        raporlarAylikGelir=value.AylikGelir()
        aylil_kar=value.AylikKar()
        Aylık_Gider=value.AylikGider()

        assert gelirSayfasi==raporlarAylikGelir
        assert gider_sayfasi_giderler==Aylık_Gider

        kar=gelirSayfasi-gider_sayfasi_giderler
        print(kar)
        assert float(kar)==float(aylil_kar)


