import string
from operator import itemgetter

def open_file():

    filename = input('Enter filemane: ')

    try:
        file_open = open(filename,'r')
        return file_open

    except FileNotFoundError:
        print("Filename {} not found!".format(filename))

def get_data(file_open, data_list = [], temp_list = []):

        for line in file_open:
            if line == '\n':
                data_list.append(temp_list)
                temp_list = []
            else:
                word_in_line = line.split()
                for word in word_in_line:
                    temp_list.append(word.strip(string.punctuation).lower())
        data_list.append(temp_list)
        file_open.close()

        return data_list

def get_all_words(data_list, words_list = []):

    for paragraph in data_list:
        for word in paragraph:
            if word not in words_list:
                words_list.append(word)
    return words_list

def word_paragraph_location(words_list, data_list, location_dict = {}, temp_str = ''):

    for word in words_list:
        for i in range(len(data_list)):
            if word in data_list[i]:
                temp_str += '{}, '.format(i+1)
        temp_str = temp_str[:-2]
        location_dict[word] = temp_str
        temp_str = ''

    return location_dict

def show_word_location(location_dict):

    for word, location in location_dict.items():
        print('{} {}'.format(word, location))



# --- Main Program ---

file_object = open_file()
file_data = get_data(file_object)
words_list = get_all_words(file_data)
location_dict = word_paragraph_location(words_list, file_data)
show_word_location(location_dict)



