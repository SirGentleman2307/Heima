from Ui.MenuClass import Menu


class System():

    def __init__(self):
        self.__MainMenu = Menu(' Welcome to NaN-Air ', ['Create', 'Edit', 'View'], 'Quit')
        self.__CreateMenu = Menu(' Create Menu ', ['Airplane', 'Crew Member', 'Destination', 'Pilot', 'Voyage'])
        self.__EditMenu = Menu(' Edit Menu ', ['Airplane', 'Crew Member', 'Destination', 'Pilot', 'Voyage'])
        self.__ViewMenu = Menu(' View Menu ', ['Airplane', 'Crew Member', 'Destination', 'Pilot', 'Voyage'])

    def start_up(self):
        '''Starts up the system'''
        self.__MainMenu.display()
        User_Input_int = self.get_input_int('Enter in a number', self.__MainMenu.tuple)
        Command_str = self.__MainMenu.give_input(User_Input_int)
        self.run(Command_str)

    def run(self, Command_str):

        if Command_str == 'Create':
            self.__CreateMenu.display()
            User_Input_int = self.get_input_int('Enter in a number',self.__CreateMenu.tuple)

    def get_input_int(self, question_str, range_tup):
        '''Gets a INT input from user and tests it to see if it is valid'''
        while True:
            USER_INPUT = input('{}: '.format(question_str))
            try:
                USER_INPUT = int(USER_INPUT)    # Test 1, try to int the input str

                if USER_INPUT < range_tup[0] or USER_INPUT > range_tup[1]:      # Test 2, is the number in range
                    print('\n-----Out of range !!!-----')
                    input('Press enter to continue: ')
                    continue
                return USER_INPUT

            except ValueError:
                print('\n-----That was not a number !!!-----')
                input('Press enter to continue: ')
                continue