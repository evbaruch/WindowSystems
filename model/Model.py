import requests

class Model:
    """
    Model class in mvp architecture.
    
    functions:
        validateAddress(address)-> bool:(True if the address is valid, False otherwise)
        getData(address, zoom)-> json:(weather and map data)
        getResponse(map, prompt)-> json:(updated item is included by checking the id_map and prompt)
        delete(map)-> bool:(True if the item is deleted, False otherwise)
        getAllItems()-> json:(all items from the SQL database)
    """

    def __init__(self):
        """
        Initialize the Model.
        """
        pass

    def validateAddress(self, address):
        url = "https://localhost:7216/api/Data/IsALocation"
        params = {"address": address}
        response = requests.get(url, params=params, verify=False)
        return response.json().get("isValid")

    def getData(self, address, zoom):
        url = "https://localhost:7216/api/Data/GetData"
        params = {"address": address, "zoom": zoom}
        response = requests.get(url, params=params, verify=False)
        return response.json()

    def getResponse(self, id, prompt):
        url = "https://localhost:7216/api/Data/GetResponse"
        params = {"id_map": id, "Prompt": prompt}
        response = requests.get(url, params=params)
        return response.json()

    def delete(self, id_map):
        url = "https://localhost:7216/api/Data/Delete"
        params = {"id_map": id_map}
        response = requests.get(url, params=params)
        return response.status_code == 200

    # def getAllItems(self):        
    #     url = "https://localhost:7216/api/Data/GetAllItems"
    #     response = requests.get(url)
    #     return response.json()