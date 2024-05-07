from model.DataSource import DataSource
import copy
import requests

class Model:
    def __init__(self, repository: DataSource):
        self.repository = repository

    def process_data(self):
        processed_data = self.repository.read()
        processed_data = [item.upper() for item in processed_data]  # Example logic
        return processed_data
    
    def update_data(self, data):

        if isinstance(data, str):
            self.repository.create(data.lower())
        elif isinstance(data, (int, float)):
            self.repository.create(str(data).lower())
        else:
            return data
        
    def create_item(self, item):
        return self.repository.create(item)

    def read_item(self, index=None):
        data = self.repository.read(index)
        return copy.deepcopy(data) if data is not None else None

    def update_item(self, index, new_item):
        return self.repository.update(index, new_item)

    def delete_item(self, index):
        return self.repository.delete(index)
    
    def validate_address(self, address):
        url = "https://localhost:7216/api/Data/IsALocation"
        params = {"address": address}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return True
        else:
            return False
        
    def get_data(self):
        return self.repository.read()
        # send request to controller to get data
        
    
