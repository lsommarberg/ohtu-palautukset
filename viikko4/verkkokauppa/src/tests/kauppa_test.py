import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

    def varasto_saldo(self, tuote_id):
        if tuote_id == 1:
            return 10
        if tuote_id == 2:
            return 20
        if tuote_id == 3:
            return 0

    def varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        if tuote_id == 2:
            return Tuote(2, "kahvi", 6)
        if tuote_id == 3:
            return Tuote(3, "leipä", 2)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

 
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_kutsutaan_tilisiirto_oikeilla_parametreilla(self):


        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote


        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 5)

    def test_kahden_ostoksen_jalkeen_kutsutaan_tilisiirto_oikeilla_parametreilla(self):

            
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)

        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 11)

    def test_kahden_saman_ostoksen_jalkeen_kutsutaan_tilisiirto_oikeilla_parametreilla(self):

        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(2)
        

        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 12)

    def test_kahden_eri_ostoksen_jalkeen_kutsutaan_tilisiirto_oikeilla_parametreilla(self):

        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 5)
    
    def test_kahden_ostoksen_ja_poiston_jalkeen_kutsutaan_tilisiirto_oikeilla_parametreilla(self):

        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", kauppa._kaupan_tili, 0)
 