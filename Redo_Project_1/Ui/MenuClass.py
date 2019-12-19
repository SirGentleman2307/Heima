

class Menu():

    def __init__(self, name_str = ' Name Missing ', options_list = [], last_op_str = 'Back'):
        self.__name = name_str
        self.__header = self.header_maker()
        self.__list = options_list
        self.__last_op = last_op_str
        self.__options = self.list_options()

    def header_maker(self):
        '''Makes a String that is the Header for the menu (tui)'''
        LEN_int = len(self.__name)
        LEN_str = '=' * LEN_int
        return '\n{0}\n{1}\n{0}\n'.format(LEN_str, self.__name)

    def list_options(self):
        '''Makes a String that is all options for the menu (tui)'''
        OUT_str = ''
        for number, option in enumerate(self.__list, 1):
            OUT_str += '\n{:3}. {}'.format(number, option)
        OUT_str += '\n  0. {}'.format(self.__last_op)
        return OUT_str

    def display(self):
        '''Used by the tui to display a menu'''
        print(self.__header + self.__options)

    def give_input(self, input_int):

        return self.__list[input_int]

# Thing = Menu(' Welcome to NaN-Air ', ['Create', 'Edit', 'View', 'Remove'], 'Quit')
# Thing.display()
Thing2 = Menu()
Thing2.display()