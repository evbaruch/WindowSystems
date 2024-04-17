from abc import ABC, abstractmethod
from view import Event

class View(ABC):
    def __init__(self):
        self.input = Event.new_data_Event()
        self.display = Event.display_data_Event()
        self.end = Event.end_program_Event()

    @abstractmethod
    def main_loop(self):
        pass

    @abstractmethod
    def display_data(self, data):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def end_program(self, message):
        pass



