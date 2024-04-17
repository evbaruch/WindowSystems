from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def create(self, item):
        pass

    @abstractmethod
    def read(self, index=None):
        pass

    @abstractmethod
    def update(self, index, new_item):
        pass

    @abstractmethod
    def delete(self, index):
        pass