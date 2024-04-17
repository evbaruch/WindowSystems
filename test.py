import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


class CounterModel(QObject):
    counter_changed = Signal(int)

    def __init__(self):
        super().__init__()
        self._counter = 0

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value
        self.counter_changed.emit(self._counter)


class CounterPresenter(QObject):
    def __init__(self, model, view):
        super().__init__()
        self._model = model
        self._view = view

        self._view.counter_updated.connect(self.increment_counter)
        self._model.counter_changed.connect(self._view.update_counter_label)

    @Slot()
    def increment_counter(self):
        self._model.counter += 1


class CounterView(QMainWindow):
    counter_updated = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MVP Counter Example")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.counter_label = QPushButton("Counter: 0")
        self.layout.addWidget(self.counter_label)

        self.increment_button = QPushButton("Increment")
        self.layout.addWidget(self.increment_button)

        self.increment_button.clicked.connect(self.counter_updated.emit)

    @Slot(int)
    def update_counter_label(self, counter):
        self.counter_label.setText(f"Counter: {counter}")


def main():
    app = QApplication(sys.argv)

    model = CounterModel()
    view = CounterView()
    presenter = CounterPresenter(model, view)

    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
