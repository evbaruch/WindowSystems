from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from view.View import View
from view import Event

class QtView(View):
    def __init__(self):
        super().__init__()

        # Initialize Qt application
        self.app = QApplication([])

        # Create main window
        self.window = QMainWindow()
        self.window.setWindowTitle("Qt View Example")

        # Create central widget and layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Add components to layout
        self.label = QLabel("Enter your input:")
        self.layout.addWidget(self.label)

        self.input_line_edit = QLineEdit()
        self.layout.addWidget(self.input_line_edit)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.handle_submit)
        self.layout.addWidget(self.submit_button)

        self.display_label = QLabel()
        self.layout.addWidget(self.display_label)

        # Set central widget
        self.window.setCentralWidget(self.central_widget)

    def main_loop(self):
        self.window.show()
        self.app.exec_()

    def display_data(self, data):
        self.display_label.setText("Displaying Data:\n" + "\n".join(data))

    def get_user_input(self):
        return self.input_line_edit.text()

    def show_message(self, message):
        self.display_label.setText(message)

    def end_program(self, message):
        self.show_message(message)
        self.window.close()

    def handle_submit(self):
        self.input.fire()
        self.display.fire()
        if self.input_line_edit.text() == "end":
            self.end.fire("Thank you")

