import unittest
from domain.models import Mobil
from infrastructure.in_memory_repo import InMemoryMobilRepository

class TestInMemoryMobilRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryMobilRepository()

    # ADD
    def test_add_mobil_success(self):
        mobil = Mobil(0, "Toyota", 2020, "Putih")
        result = self.repo.add(mobil)
        self.assertEqual(result.id, 1)

    def test_add_multiple_mobil(self):
        m1 = self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        m2 = self.repo.add(Mobil(0, "Honda", 2021, "Merah"))
        self.assertNotEqual(m1.id, m2.id)

    def test_add_mobil_empty_fields(self):
        mobil = Mobil(0, "", 0, "")
        result = self.repo.add(mobil)
        self.assertEqual(result.merk, "")

    # BROWSE
    def test_browse_mobil_empty(self):
        self.assertEqual(self.repo.browse(), [])

    def test_browse_mobil_after_add(self):
        self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        self.assertEqual(len(self.repo.browse()), 1)

    def test_browse_mobil_multiple(self):
        self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        self.repo.add(Mobil(0, "Honda", 2021, "Merah"))
        self.assertEqual(len(self.repo.browse()), 2)

    # READ
    def test_read_mobil_success(self):
        m = self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        result = self.repo.read(m.id)
        self.assertIsNotNone(result)

    def test_read_mobil_not_found(self):
        self.assertIsNone(self.repo.read(999))

    def test_read_mobil_after_delete(self):
        m = self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        self.repo.delete(m.id)
        self.assertIsNone(self.repo.read(m.id))

    # EDIT
    def test_edit_mobil_success(self):
        m = self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        baru = Mobil(0, "Honda", 2022, "Merah")
        result = self.repo.edit(m.id, baru)
        self.assertEqual(result.merk, "Honda")

    def test_edit_mobil_not_found(self):
        baru = Mobil(0, "Honda", 2022, "Merah")
        self.assertIsNone(self.repo.edit(999, baru))

    def test_edit_mobil_partial(self):
        m = self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        baru = Mobil(0, "", 0, "")
        result = self.repo.edit(m.id, baru)
        self.assertEqual(result.merk, "")

    # DELETE
    def test_delete_mobil_success(self):
        m = self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        result = self.repo.delete(m.id)
        self.assertIsNotNone(result)

    def test_delete_mobil_not_found(self):
        self.assertIsNone(self.repo.delete(999))

    def test_delete_mobil_twice(self):
        m = self.repo.add(Mobil(0, "Toyota", 2020, "Putih"))
        self.repo.delete(m.id)
        self.assertIsNone(self.repo.delete(m.id))