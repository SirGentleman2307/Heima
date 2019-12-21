from Ui.MenuClass import Menu


class System():

    def __init__(self):
        self.__MainMenu = Menu(' Welcome to NaN-Air ', ['Create', 'Edit', 'View'], 'Quit')
        self.__CreateMenu = Menu(' Create Menu ', ['Airplane', 'Crew Member', 'Destination', 'Pilot', 'Voyage'])
        self.__EditMenu = Menu(' Edit Menu ', ['Airplane', 'Crew Member', 'Destination', 'Pilot', 'Voyage'])
        self.__ViewMenu = Menu(' View Menu ', ['Airplane', 'Crew Member', 'Destination', 'Pilot', 'Voyage'])


    def start_up(self):

        self.__MainMenu.display()
