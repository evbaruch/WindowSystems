from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea


class PopupWindow(QWidget):
    def __init__(self, image, address , item):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # Display the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(image)
        self.layout.addWidget(self.image_label)

        # Display the address
        self.address_label = QLabel(address, self)
        self.layout.addWidget(self.address_label)

        # Display the address
        self.address_label = QLabel(f"Address: {item.get('location').get('address')}", self)
        self.layout.addWidget(self.address_label)
        # Display the latitude
        self.lat_label = QLabel(f"Latitude: {item.get('location').get('latitude')}", self)
        self.layout.addWidget(self.lat_label)
        # Display the longitude
        self.lon_label = QLabel(f"Longitude: {item.get('location').get('longitude')}", self)
        self.layout.addWidget(self.lon_label)
        
        # Display the temp
        self.temp_label = QLabel(f"Weather:\nTemp: {item.get('weather').get('temp')}", self)
        self.layout.addWidget(self.temp_label)
        # Display the visibility
        self.visibility_label = QLabel(f"Visibility: {item.get('weather').get('visibility')}", self)
        self.layout.addWidget(self.visibility_label)
        # Display the humidity
        self.humidity_label = QLabel(f"Humidity: {item.get('weather').get('humidity')}", self)
        self.layout.addWidget(self.humidity_label)

        # 
        self.space_label = QLabel("", self)
        self.layout.addWidget(self.space_label)
        
        # Display the prompt and response
        self.prompt_label = QLabel(f"Prompt: {item.get('chatGpt').get('prompt')}", self)
        self.prompt_label.setWordWrap(True)
        self.prompt_scroll_area = QScrollArea()
        self.prompt_scroll_area.setWidget(self.prompt_label)
        self.layout.addWidget(self.prompt_scroll_area)

        # Display the response
        self.response_label = QLabel(f"Response: {item.get('chatGpt').get('response')}", self)
        self.response_label.setWordWrap(True)
        self.response_scroll_area = QScrollArea()
        self.response_scroll_area.setWidget(self.response_label)
        self.layout.addWidget(self.response_scroll_area)


        # Apply CSS styles for the popup window
        self.setStyleSheet("""
            background-color: #262a2e;
            color: white;
        """)

        self.setWindowTitle("Widget Details")
        self.resize(200, 200)