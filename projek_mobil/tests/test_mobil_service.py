import unittest
from domain.models import Mobil
from usecases.mobil_service import MobilService
from infrastructure.in_memory_repo import InMemoryMobilRepository

class TestMobilService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryMobilRepository()
        self.service = MobilService(self.repo)

    # ADD
    def test_add_mobil_success(self):
        mobil = Mobil(0, "Toyota", 2020, "Putih")
        result = self.service.add_mobil(mobil)
        self.assertEqual(result.id, 1)

    def test_add_multiple_mobil(self):
        m1 = self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        m2 = self.service.add_mobil(Mobil(0, "Honda", 2021, "Merah"))
        self.assertNotEqual(m1.id, m2.id)

    def test_add_mobil_empty_fields(self):
        mobil = Mobil(0, "", 0, "")
        result = self.service.add_mobil(mobil)
        self.assertEqual(result.merk, "")

    # BROWSE
    def test_browse_mobil_empty(self):
        self.assertEqual(self.service.browse_mobil(), [])

    def test_browse_mobil_after_add(self):
        self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        self.assertEqual(len(self.service.browse_mobil()), 1)

    def test_browse_mobil_multiple(self):
        self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        self.service.add_mobil(Mobil(0, "Honda", 2021, "Merah"))
        self.assertEqual(len(self.service.browse_mobil()), 2)

    # READ
    def test_read_mobil_success(self):
        m = self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        result = self.service.read_mobil(m.id)
        self.assertIsNotNone(result)

    def test_read_mobil_not_found(self):
        self.assertIsNone(self.service.read_mobil(999))

    def test_read_mobil_after_delete(self):
        m = self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        self.service.delete_mobil(m.id)
        self.assertIsNone(self.service.read_mobil(m.id))

    # EDIT
    def test_edit_mobil_success(self):
        m = self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        baru = Mobil(0, "Honda", 2022, "Merah")
        result = self.service.edit_mobil(m.id, baru)
        self.assertEqual(result.merk, "Honda")

    def test_edit_mobil_not_found(self):
        baru = Mobil(0, "Honda", 2022, "Merah")
        self.assertIsNone(self.service.edit_mobil(999, baru))

    def test_edit_mobil_partial(self):
        m = self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        baru = Mobil(0, "", 0, "")
        result = self.service.edit_mobil(m.id, baru)
        self.assertEqual(result.merk, "")

    # DELETE
    def test_delete_mobil_success(self):
        m = self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        result = self.service.delete_mobil(m.id)
        self.assertIsNotNone(result)

    def test_delete_mobil_not_found(self):
        self.assertIsNone(self.service.delete_mobil(999))

    def test_delete_mobil_twice(self):
        m = self.service.add_mobil(Mobil(0, "Toyota", 2020, "Putih"))
        self.service.delete_mobil(m.id)
        self.assertIsNone(self.service.delete_mobil(m.id))