from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMenu
from PySide6.QtGui import QPixmap ,QAction
from PySide6.QtCore import Qt
from view.popup import PopupWindow
from PySide6.QtCore import QEvent
import requests



class ClickableWidget(QWidget):
    def __init__(self, image_path, address ,item , parent):
        super().__init__()
        self.delete_action = QAction("Delete", self)
        self.resend_action = QAction("Resend", self)
        self.Qparent = parent
        self.item_data = item
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
        if event.button() == Qt.LeftButton:
            self.popup = PopupWindow(self.image_label.pixmap(), self.address_label.text(),self.item_data)
            self.popup.show()
            self.setStyleSheet("""
                background-color: gray;
            """)
        
    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        self.delete_action.triggered.connect(lambda: self.Qparent.delete_clicked(self.item_data.get('id')))
        context_menu.addAction(self.delete_action)

        self.resend_action.triggered.connect(lambda: self.Qparent.resend_clicked(self.item_data.get('id')))
        context_menu.addAction(self.resend_action)

        context_menu.exec_(event.globalPos())