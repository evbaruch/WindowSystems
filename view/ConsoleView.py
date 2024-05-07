from view.View import View

class ConsoleView(View):

    def startView(self):
        print("Starting Main Loop")
        while True:
            self.input.fire()
            self.display.fire()
            str = input("Enter 'end' to end the program: ")
            if str == "end":
                self.end.fire("Thank you")

    def display_data(self, data):
        print("Displaying Data:")
        for item in data:
            print(item)
    
    def get_user_input(self):
        return input("Enter your input: ")
    
    def show_message(self, message):
        print(message)

    def end_program(self):
        exit()
