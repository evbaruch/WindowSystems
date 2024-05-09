from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QSplitter, QTabWidget, QFormLayout, QDateEdit, QScrollArea ,QHBoxLayout,QMessageBox , QGridLayout ,QSlider
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtCore import QEvent 
import json
import requests

from qt_material import apply_stylesheet
from view.View import View
#from view import Event
from view.Event import Event

class ClickableWidget(QWidget):
    def __init__(self, image_path, address):
        super().__init__()

        self.setAttribute(Qt.WA_Hover, True)
        self.layout = QVBoxLayout(self)
        pixmap = QPixmap()
        self.image_label = QLabel(self)
        pixmap.loadFromData(requests.get(image_path).content)
        self.image_label.setPixmap(pixmap.scaled(143, 143, Qt.KeepAspectRatio))
        self.image_label.setStyleSheet("""
            border: 10px solid black;
            border-radius: 20px;
        """)  # Add a rounded border around the image
        self.layout.addWidget(self.image_label)

        self.address_label = QLabel(address, self)
        self.layout.addWidget(self.address_label)

        # Apply CSS styles for normal state
        self.setStyleSheet("""
            background-color: #262a2e;
            color: white;
        """)

        # Install event filter
        self.installEventFilter(self)

    # def eventFilter(self, obj, event):
    #     # Change the style when a hover event is detected
    #     if event.type() == QEvent.HoverEnter:
    #         self.setStyleSheet("""
    #             background-color: #448aff;
    #         """)
    #     elif event.type() == QEvent.HoverLeave:
    #         self.setStyleSheet("""
    #             background-color: #2E2E2E;
    #         """)
    #     return super().eventFilter(obj, event)
    
    def eventFilter(self, obj, event):
        # Change the style when a hover event is detected
        if event.type() == QEvent.HoverEnter:
            self.setStyleSheet("""
                background-color: #262a2e;
            """)
            self.address_label.setStyleSheet("""
                color: #448aff;
                text-decoration: underline;
            """)
        elif event.type() == QEvent.HoverLeave:
            self.setStyleSheet("""
                background-color: #262a2e;
            """)
            self.address_label.setStyleSheet("""
                color: white;
                text-decoration: none;
            """)
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        QMessageBox.information(self, "Clicked", "You clicked on " + self.address_label.text())
        # Change the style when clicked
        self.setStyleSheet("""
            background-color: gray;
        """)

class QtView(View):
    def __init__(self):
        super().__init__()
        
        # Initialize Qt application
        self.app = QApplication([])

        # Create main window
        self.window = QMainWindow()
        
        # set the window title
        self.window.setWindowTitle("Qt View")
        
        # set window size
        self.window.resize(1000, 600)
        
        # Initialize addresses as an empty JSON array
        self.history = json.loads('[]')  # Initialize as an empty JSON array
        
        # Create a central widget for the main window
        self.central_widget = QWidget()
        self.window.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Create a tab widget
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.currentChanged.connect(self.tab_changed)
        self.layout.addWidget(self.tab_widget)
        # First tab
        self.first_tab = QWidget()
        self.first_layout = QFormLayout(self.first_tab)

        self.address_label = QLabel("Enter Address:")
        self.isAddressValid = False
        self.address_line_edit = QLineEdit(self.first_tab)
        self.address_line_edit.setStyleSheet("color: white;")
        self.first_layout.addRow(self.address_label, self.address_line_edit)

        self.zoom_label = QLabel("Enter Zoom Level:")
        self.zoom_slider = QSlider(Qt.Horizontal, self.first_tab)
        self.zoom_slider.setStyleSheet("color: white;")
        self.zoom_slider.setMinimum(1)  # Set the minimum value
        self.zoom_slider.setMaximum(20)  # Set the maximum value
        self.zoom_value_label = QLabel()  # Create a label to display the slider's value
        self.zoom_slider.valueChanged.connect(lambda: self.zoom_value_label.setText(str(self.zoom_slider.value())))  # Update the label's text when the slider's value changes

        zoom_layout = QHBoxLayout()  # Create a horizontal layout
        zoom_layout.addWidget(self.zoom_slider)  # Add the slider to the layout
        zoom_layout.addWidget(self.zoom_value_label)  # Add the value label to the layout

        self.first_layout.addRow(self.zoom_label, zoom_layout)  # Add the label and the layout (containing the slider and the value label) to the row

        self.submit_button = QPushButton("Submit", self.first_tab)
        self.submit_button.clicked.connect(self.handle_submit_first_tab)
        self.submit_button.setEnabled(True) 
        self.first_layout.addRow(self.submit_button)
        
        #the hidden message will be hidden and when shown the text will be error's red
        self.hidden_message = QLabel("")
        self.hidden_message.setStyleSheet("color: red;")
        self.first_layout.addRow(self.hidden_message)
        
        self.tab_widget.addTab(self.first_tab, "Address and Date")
        self.input
        # Second tab
        self.second_tab = QWidget()
        self.second_layout = QHBoxLayout(self.second_tab)  # Change to QHBoxLayout

        self.splitter = QSplitter(Qt.Orientation.Horizontal, self.second_tab)  # Change to Horizontal
        self.second_layout.addWidget(self.splitter)

        # Left widget with image holder
        self.left_widget = QWidget(self.second_tab)
        self.left_layout = QVBoxLayout(self.left_widget)
        self.left_layout.setAlignment(Qt.AlignCenter)  # Align the layout to the center

        self.image_label = QLabel(self.left_widget)
        self.pixmap = QPixmap()

        self.image_label.setScaledContents(True)  # Add this line
        self.image_label.setAlignment(Qt.AlignCenter)  # Align the image label to the center
        self.left_layout.addWidget(self.image_label)

        self.splitter.addWidget(self.left_widget)

        # Right widget with text presenter, text input, and send button
        self.right_widget = QWidget(self.second_tab)
        self.right_layout = QVBoxLayout(self.right_widget)

        self.input_label = QLabel("Input:", self.right_widget)  # Rename the header for the input
        self.right_layout.addWidget(self.input_label)

        self.input_line_edit = QLineEdit(self.right_widget)
        self.input_line_edit.setStyleSheet("color: white;")
        self.right_layout.addWidget(self.input_line_edit)

        self.send_button = QPushButton("Send", self.right_widget)
        self.send_button.clicked.connect(self.handle_submit_second_tab)
        self.right_layout.addWidget(self.send_button)

        # Create a scroll area for the display label
        self.scroll_area = QScrollArea(self.right_widget)
        self.scroll_area.setWidgetResizable(True)  # Allow the widget to resize

        # Create a widget for the scroll area
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        self.display_label = QLabel(self.scroll_widget)  # Define the display_label here
        self.scroll_layout.addWidget(self.display_label)

        # Set the scroll widget as the widget for the scroll area
        self.scroll_area.setWidget(self.scroll_widget)

        self.right_layout.addWidget(self.scroll_area)  # Add the scroll area to the layout right after the send button

        self.splitter.addWidget(self.right_widget)

        # Set the stretch factors of the widgets in the splitter
        self.splitter.setStretchFactor(0, 0)  # Set the stretch factor of the left widget to 0
        self.splitter.setStretchFactor(1, 1)  # Set the stretch factor of the right widget to 1

        # Make the splitter handle not movable
        self.splitter.setHandleWidth(0)

        self.tab_widget.addTab(self.second_tab, "Map and Response")

        # Third tab (history of requests)
        self.third_tab = QWidget()
        self.third_layout = QVBoxLayout(self.third_tab)

        self.history_label = QLabel("History of Requests:", self.third_tab)
        self.third_layout.addWidget(self.history_label)

        self.tab_widget.addTab(self.third_tab, "History")
        
        # Apply a theme to the application
        apply_stylesheet(self.app, theme='dark_blue.xml')

        # Add a flag to track whether the submit button has been clicked
        self.submit_clicked = False

    def display_data(self, data):
        self.display_label.setText(data.get("response"))  # Replace with the key for the response in your JSON object
        url = data.get("id")
        self.image_label.setPixmap(self.pixmap.loadFromData(requests.get(url)).content)  # Replace with the key for the image in your JSON object
        # Set a fixed size for the image label
        self.image_label.setFixedSize(self.image_label.pixmap().width(), self.image_label.pixmap().height())
        

    def get_user_input(self):
        return self.input_line_edit.text()

    def show_message(self, message):
        self.display_label.setText(message)

    def end_program(self, message):
        self.show_message(message)
        self.window.close()

    def handle_submit_first_tab(self):
        if(self.isAddressValid):
            self.submit_clicked = True  # Set the flag to True when the submit button is clicked
            self.tab_widget.setCurrentIndex(1)  # Move to the second tab
            self.input.fire()
            self.display.fire()
    
    def handle_submit_second_tab(self):
        self.input.fire()
        self.display.fire()
    
    """
            Display a message box with the given message.
    """ 
    def show_message(self, message):
        msgBox = QMessageBox()
        msgBox.setText(message)
        msgBox.exec()

    def tab_changed(self, index):
        if not hasattr(self, 'submit_clicked'):
            self.submit_clicked = False

        
        if index == 2:  # If the current tab is the "History" tab
            return  # Do nothing and allow the user to access the tab
        elif not self.submit_clicked and index != 0:
            self.tab_widget.setCurrentIndex(0)  # Force stay on the first tab
        elif self.submit_clicked and not (self.address_line_edit):
            self.submit_clicked = False  # Reset the flag when moving back to the first tab
            self.tab_widget.setCurrentIndex(0)  # Force stay on the first tab
                 
    def history_init(self):
            self.scroll_area = QScrollArea(self.third_tab)
            # give the Scroll Area a different color
            self.scroll_area.setStyleSheet("background-color: #262a2e;")
            self.scroll_widget = QWidget()
            self.history_list_widget = QGridLayout(self.scroll_widget)

            for i, address in enumerate(self.history):
                widget = ClickableWidget(address.get("path"), address.get("address"))
                row = i // 7  # change the number to set number of rows
                column = i % 5  # change the number to set number of columns
                self.history_list_widget.addWidget(widget, row, column)

            self.scroll_area.setWidget(self.scroll_widget)
            self.third_layout.addWidget(self.scroll_area)       
    
    def startView(self):
        self.history_init()
        self.window.show()
        self.app.exec_()