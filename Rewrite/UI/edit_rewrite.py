# Edit Menu


class EditMenu():

    def __init__(self, input_tuple):
        self.__header_str, self.__optinons_list = input_tuple

    def display(self):

        font_str = '='*len(self.__header_str)
        print('{0}\n{1}\n{0}'.format(font_str,self.__header_str))
        for number, option in enumerate(self.__optinons_list):
            print('{}. {}'.format(number, option))

    def get_input(self):
        try:
            user_input = int(input("Please choose what you would like to do: "))
        except ValueError:
            user_input = 'Invalid'
        return user_input

    def start_up(self):

        user_input_int = True
        while user_input_int:
            self.display()
            user_input_int = self.get_input()

            if user_input_int == 'Invalid':
                print('Please enter a number that coresponds to an option')
                continue

            return self.run(user_input_int)

    def run(self, command_int):

        if command_int == 0:
            print('You picked Main Menu')

        if command_int == 1:
            print('You picked Pilot')

        if command_int == 2:
            print('You picked Flight Attendant')

        if command_int == 3:
            print('You picked Voyage')

        if command_int == 4:
            print('You picked Airplane')
