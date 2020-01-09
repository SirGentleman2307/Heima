import csv
import os
import datetime

class Data():

    def __init__(self):

        self.__path = os.getcwd() + '/Data/Repo'

    def read_file(self, filename):
        '''Input: Filename to read
        Output: List of all lines in the file'''

        file_exists = self.__path + '/' + filename
        if file_exists:
            output_data_list = []
            with open(file_exists, 'r', encoding= 'utf-8') as file_obj:
                for line in file_obj:
                    line = line.strip().split(';')
                    output_data_list.append(line)
            return output_data_list
        else:
            return 'File Not Found'

    def save_on_file(self, data_input_str, filename):
        '''Input: String that is saved on the inputed filename'''

        if type(data_input_str) != str:
            return 'Input not a string'

        if data_input_str[-1] != '\n':
            data_input_str += '\n'

        file_exists = self.__path + "/" + filename
        if file_exists:
            with open(file_exists, 'a+', encoding= 'utf-8') as file_obj:
                file_obj.write(data_input_str)

if __name__ == "__main__":

    Worker = Data()
    Worker.save_on_file('1;2;3;4;5;6;7;8;9;10;11','AircraftType.csv')
    data_list = Worker.read_file('AircraftType.csv')
    print(data_list)
