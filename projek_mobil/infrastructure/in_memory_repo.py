from interface.mobil_repository import MobilRepository

class InMemoryMobilRepository(MobilRepository):
    def __init__(self):
        self._data = {}
        self._counter = 1

    def add(self, mobil):
        mobil.id = self._counter
        self._data[self._counter] = mobil
        self._counter += 1
        return mobil

    def browse(self):
        return list(self._data.values())

    def read(self, mobil_id):
        return self._data.get(mobil_id)

    def edit(self, mobil_id, data_baru):
        if mobil_id in self._data:
            mobil = self._data[mobil_id]
            mobil.merk = data_baru.merk
            mobil.tahun = data_baru.tahun
            mobil.warna = data_baru.warna
            return mobil
        return None

    def delete(self, mobil_id):
        return self._data.pop(mobil_id, None)
