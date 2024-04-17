# Define events class
class Event:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def fire(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)



class display_data_Event(Event):
    pass

class new_data_Event(Event):
    pass

class end_program_Event(Event):
    pass

class Data_update_Event(Event):
    pass