# This file is the Presenter module of the MVP pattern. It is responsible for handling user input and updating the model and view accordingly. It is the middleman between the model and the view. It is also responsible for processing the data and displaying it to the user.
# The Presenter module is the only module that should import both the Model and View modules. It should not import any other modules.
from model.DataSource import DataSource
from model.ListDataSource import ListDataSource
from model.Model import Model

from view.View import View
from view.QtView import QtView
from view.ConsoleView import ConsoleView
from view.Event import *


class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Connect view signals to presenter methods
        self.view.submit_button.clicked.connect(self.handle_submit)
        self.view.input_line_edit.textChanged.connect(self.check_address)


    def show(self):
        self.view.input.add_handler(self.new_input)
        self.view.display.add_handler(self.display_data)
        self.view.end.add_handler(self.end_program)
        self.view.startView()

    def display_data(self):
        processed_data = self.model.process_data()
        self.view.display_data(processed_data)

    def new_input(self):
        input = self.view.get_user_input()
        self.model.update_data(input)

    def end_program(self, message):
        self.view.show_message(message)
        self.view.end_program(message)
        
    def check_address(self, address):
        is_valid = self.model.validate_address(address)
        self.view.submit_button.setEnabled(is_valid)
        
    def handle_submit(self):
        data = self.model.get_data()
        self.view.display_data(data)





# Example usage:
def start_application():
    # Instantiate Model and Presenter
    repository = ListDataSource(10)
    model = Model(repository)
    #view = ConsoleView()
    view = QtView()
    presenter = Presenter(model, view)


    presenter.show()

    #presenter.handle_user_input()
    #presenter.process_and_display_data()
