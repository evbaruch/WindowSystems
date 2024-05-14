from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QScrollArea
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class PopupWindow(QWidget):
    def __init__(self, image, address , item):
        super().__init__()

        self.layout = QGridLayout(self)
        
        # set name of the name of the window
        self.setWindowTitle("Details")
        
        # set the size of the window
        self.resize(500, 500)
        
        # set the Icon of the window
        self.setWindowIcon(QIcon("view/Skull-Icon.svg.png"))
        

        # Display the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(image.scaled(300, 300, Qt.KeepAspectRatio))
        self.layout.addWidget(self.image_label, 0, 0, 5, 1)  # Span the image over 5 rows

        # Display the address
        self.address_label = QLabel(address, self)
        self.layout.addWidget(self.address_label, 0, 1)

        # Display the address
        self.address_label = QLabel(f"Address: {item.get('location').get('address')}", self)
        self.layout.addWidget(self.address_label, 1, 1)
        # Display the latitude
        self.lat_label = QLabel(f"Latitude: {item.get('location').get('latitude')}", self)
        self.layout.addWidget(self.lat_label, 2, 1)
        # Display the longitude
        self.lon_label = QLabel(f"Longitude: {item.get('location').get('longitude')}", self)
        self.layout.addWidget(self.lon_label, 3, 1)
        
        # Display the temp
        self.temp_label = QLabel(f"Weather:\nTemp: {item.get('weather').get('temp')}", self)
        self.layout.addWidget(self.temp_label, 4, 1)
        # Display the visibility
        self.visibility_label = QLabel(f"Visibility: {item.get('weather').get('visibility')}", self)
        self.layout.addWidget(self.visibility_label, 5, 1)
        # Display the humidity
        self.humidity_label = QLabel(f"Humidity: {item.get('weather').get('humidity')}", self)
        self.layout.addWidget(self.humidity_label, 6, 1)

        # Display the prompt and response
        self.head_prompt_lable = QLabel("ChatGPT\nPrompt:", self)
        self.layout.addWidget(self.head_prompt_lable, 7, 0)
        self.prompt_label = QLabel(f"{item.get('chatGpt').get('prompt')}", self)
        self.prompt_label.setWordWrap(True)
        self.prompt_label.setStyleSheet("background-color: #444; padding: 10px;")
        self.prompt_scroll_area = QScrollArea()
        self.prompt_scroll_area.setWidget(self.prompt_label)
        self.layout.addWidget(self.prompt_scroll_area, 8, 0)

        # Display the response
        self.head_response_lable = QLabel("Response:", self)
        self.layout.addWidget(self.head_response_lable, 7, 1)
        self.response_label = QLabel(f"{item.get('chatGpt').get('responde')}", self)
        self.response_label.setWordWrap(True)
        self.response_label.setStyleSheet("background-color: #444; padding: 10px;")
        self.response_scroll_area = QScrollArea()
        self.response_scroll_area.setWidget(self.response_label)
        self.layout.addWidget(self.response_scroll_area, 8, 1)

        # Apply CSS styles for the popup window
        self.setStyleSheet("""
            background-color: #262a2e;
            color: white;
        """)