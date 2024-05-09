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
        # self.view.history_created_event.add_handler(self.get_all_items)
        # self.view.address_line_edit.textChanged.connect(self.check_address) # the user types in the input line edit - the address is validated or not
        self.view.submit_button.clicked.connect(self.handle_submit) # the user clicks the submit button - a request is sent to the model to get the data
        # self.view.send_button.clicked.connect(self.handle_send) # the user clicks the send button - a request is sent to the model to send the message
        # self.view.delete_button.clicked.connect(self.handle_delete) # the user clicks the delete button - a request is sent to the model to delete the item
        
    def show(self):
        # self.get_all_items()
        # self.view.input.add_handler(self.new_input)
        # self.view.display.add_handler(self.display_data)
        self.view.end.add_handler(self.end_program)
        self.view.startView()

    # """
    #     requests chat
    # """
    # def display_data(self):
    #     processed_data = self.model.getResponse(id ,prompt)
    #     self.view.display_data(processed_data)

    # """
    # ?
    # """
    # def new_input(self):
    #     input = self.view.get_user_input()
    #     self.model.getResponse(id ,prompt)

    def end_program(self , message):
        self.view.show_message(message)
        self.view.end_program(message)
        
    """
    requests validation of the address
    """
    def check_address(self,address):
        is_valid = self.model.validateAddress(address)
        self.view.submit_button.setEnabled(is_valid)
        
    """
        requests data (map , weather)
    """    
    def handle_submit(self):
        address = self.view.address_line_edit.text()
        zoom = self.view.zoom_slider.value()
        if(self.model.validateAddress(address)):
            data = self.model.getData(address,zoom)
            self.view.display_data(data)
        else:
            self.hidden_message("Invalid address.")
        
    # """
    #     requests chat
    # """    
    # def handle_send(self):
    #     prompt = self.view.get_user_input() # TODO: get prompt from qtview
    #     id = self.view.get_id() # TODO: get id from qtview
    #     response = self.model.getResponse(id , prompt)
    #     self.view.display_data(response)
        
    # """
    #     requests deletion of the item
    # """    
    # def handle_delete(self):
    #     id_map = self.view.get_user_input() # TODO: get id_map from qtview
    #     is_deleted = self.model.delete(id_map)
    #     if is_deleted:
    #         self.view.show_message("Item deleted successfully.")
    #     else:
    #         self.view.show_message("Item not found.")
    
    # """
    #     requests all items
    # """
    # def get_all_items(self):
    #     self.view.history = self.model.getAllItems()
        
    





# Example usage:
def start_application():
    # Instantiate Model and Presenter
    model = Model()
    #view = ConsoleView()
    view = QtView()
    presenter = Presenter(model, view)

    presenter.show()

    #presenter.handle_user_input()
    #presenter.process_and_display_data()
