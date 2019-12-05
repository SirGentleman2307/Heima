# Main Ui class
from main_rewrite import MainMenu
from create_rewrite import CreateMenu
from edit_rewrite import EditMenu
from view_rewrite import ViewMenu

class Tui():

    def __init__(self):
        self.__CreateMenu = CreateMenu(('Create Menu', ['Main Menu','Pilot','Flight Attendant','Voyage','Destination','Airplane','Flight']))
        self.__EditMenu = EditMenu(('Edit Menu', ['Main Menu','Pilot','Flight attendant','Voyage','Airplane']))
        self.__ViewMenu = ViewMenu(('View Menu', ['Main Menu','Employees working','Employees NOT working','NaN airplanes','Destinations']))
        self.__MainMenu = MainMenu(("Welcome to NaN Air", ["Quit", "Create", "Edit", "View"]))

    def start_up(self):

        while True:
            command_str = self.__MainMenu.start_up()

            if command_str == 'Quit':
                print('---Program Closed---')
                break

            if command_str == 'Create':
                self.__CreateMenu.start_up()

            if command_str == 'Edit':
                self.__EditMenu.start_up()

            if command_str == 'View':
                self.__ViewMenu.start_up()


NaNAir = Tui()
NaNAir.start_up()