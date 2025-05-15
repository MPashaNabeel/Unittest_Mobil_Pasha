class MobilService:
    def __init__(self, repository):
        self.repo = repository

    def add_mobil(self, mobil):
        return self.repo.add(mobil)

    def browse_mobil(self):
        return self.repo.browse()

    def read_mobil(self, mobil_id):
        return self.repo.read(mobil_id)

    def edit_mobil(self, mobil_id, data_baru):
        return self.repo.edit(mobil_id, data_baru)

    def delete_mobil(self, mobil_id):
        return self.repo.delete(mobil_id)