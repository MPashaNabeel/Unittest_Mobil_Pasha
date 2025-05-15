from abc import ABC, abstractmethod

class MobilRepository(ABC):
    @abstractmethod
    def add(self, mobil): pass

    @abstractmethod
    def browse(self): pass

    @abstractmethod
    def read(self, mobil_id): pass

    @abstractmethod
    def edit(self, mobil_id, mobil): pass

    @abstractmethod
    def delete(self, mobil_id): pass