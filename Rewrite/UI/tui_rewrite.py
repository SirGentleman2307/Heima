# Main Ui class
from main_rewrite import MainMenu

class Tui():

    def __init__(self):
        # self.__Create = Create(('Create Menu', ['Main Menu','Pilot','Flight attendant','Voyage','Destination','Airplane','Flight']))
        # self.__Edit = Edit(('Edit Menu', ['Main Menu','Pilot','Flight attendant','Voyage','Airplane']))
        # self.__View = View(('View Menu', ['Main Menu','Employees working','Employees NOT working','NaN airplanes','Destinations']))
        self.__MainMenu = MainMenu(("Welcome to NaN Air", ["Quit", "Create", "Edit", "View"]))

    def start_up(self):

        user_input_int = True
        while user_input_int:
            self.__MainMenu.display()
            user_input_int = self.get_input()

            if user_input_int == 'Invalid' or user_input_int > 3 or user_input_int < 0:
                print('Please enter a number that coresponds to an option')
                continue
            comand_tui_int = self.__MainMenu.run(user_input_int)
            self.run(comand_tui_int)

    def get_input(self):
        try:
            user_input = int(input("Please choose what you would like to do: "))
        except ValueError:
            user_input = 'Invalid'
        return user_input


NaNAir = Tui()
NaNAir.start_up()