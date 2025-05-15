import unittest
from domain.models import Mobil

def mobil_to_str(mobil):
    return f"ID: {mobil.id} | Merk: {mobil.merk} | Tahun: {mobil.tahun} | Warna: {mobil.warna}"

class TestMainUI(unittest.TestCase):
    def test_mobil_to_str_format(self):
        m = Mobil(1, "Toyota", 2020, "Putih")
        s = mobil_to_str(m)
        self.assertIn("Toyota", s)
        self.assertIn("2020", s)

    def test_mobil_to_str_id(self):
        m = Mobil(5, "Honda", 2021, "Merah")
        s = mobil_to_str(m)
        self.assertTrue(s.startswith("ID: 5"))

    def test_mobil_to_str_warna(self):
        m = Mobil(2, "Suzuki", 2022, "Hitam")
        s = mobil_to_str(m)
        self.assertIn("Hitam", s)