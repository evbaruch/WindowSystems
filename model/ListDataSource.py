from model.DataSource import DataSource
import random

class ListDataSource(DataSource):
    def __init__(self):
        self.data = []

    def __init__(self, num: int):
        self.data = []
        self.random_initialize_names(num)

    def create(self, item):
        self.data.append(item)

    def read(self, index=None):
        if index is None:
            return self.data
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return "Index out of range."

    def update(self, index, new_item):
        if 0 <= index < len(self.data):
            self.data[index] = new_item
        else:
            return "Index out of range."

    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
            return "Item deleted successfully."
        else:
            return "Index out of range."

    def random_initialize_names(self, num_names):
        # List of random names
        names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Amelia", "Benjamin", "Isabella"]
        # Randomly select names and add to data
        for _ in range(num_names):
            random_name = random.choice(names)
            self.create(random_name)