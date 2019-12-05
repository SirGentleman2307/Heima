# Main Menu


class MainMenu():

    def __init__(self, input_tuple):
        self.__header_str, self.__optinons_list = input_tuple

    def display(self):

        font_str = '='*len(self.__header_str)
        print('{0}\n{1}\n{0}'.format(font_str,self.__header_str))
        for number, option in enumerate(self.__optinons_list):
            print('{}. {}'.format(number, option))

    def run(self, input_int):

        if input_int == 0:
            print('You picked Quit')
            return 0

        if input_int == 1:
            print('You picked Create')
            return 1

        if input_int == 2:
            print('You picked Edit')
            return 2

        if input_int == 3:
            print('You picked View')
            return 3