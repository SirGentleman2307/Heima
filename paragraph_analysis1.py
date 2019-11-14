import string
from operator import itemgetter

def get_data(file_open, set_list = [], temp_list = []):

    for line in file_open:
        if line == '\n':
            set_list.append(temp_list)
            temp_list = []
        else:
            temp = line.split()
            for word in temp:
                temp_list.append(word.strip(string.punctuation).lower())
    set_list.append(temp_list)
    return set_list

def make_sets(the_data, sets_list = [], temp_list = []):

    for element in the_data:
        for word in element:
            if word not in temp_list:
                temp_list.append(word)
        sets_list.append(temp_list)
        temp_list = []
    return sets_list

def get_words(the_data, word_list = []):

    for element in the_data:
        for word in element:
            if word not in word_list:
                word_list.append(word)
    return word_list

def analysis(word_list, sets_list, analysis_list = [], temp_str = ''):

    for word in word_list:
        for i in range(len(sets_list)):
            if word in sets_list[i]:
                temp_str += '{} '.format(i+1)
        analysis_list.append(temp_str)
        temp_str = ''
    return analysis_list

def analysis_print(word_list, analysis_list):

    for i in range(len(word_list)):
        print(word_list[i], end=' ')

        temp_list = analysis_list[i].split()
        for element in temp_list:
            if element == temp_list[-1]:
                print(element)
            else:
                print(element, end=', ')

def count_words(the_data, the_dict = {}):

    for i in range(len(the_data)):
        for word in the_data[i]:
            if word not in the_dict:
                the_dict[word] = 1
            else:
                the_dict[word] += 1
    return the_dict

def tuple_print(tuple_list):
    for i in range(len(tuple_list)):
        print('{}: {}'.format(tuple_list[i][0], tuple_list[i][1]))

def highest_print(highest_list_sorted):
    for number in [10, 20]:
        print('\nThe highest {} counts:'.format(number))
        highest_list = sorted(highest_list_sorted, key=itemgetter(1),reverse=True)[:number]
        tuple_print(highest_list)
        print()

# --- Main Program ---

filename = input("Enter filename: ")

try:
    file_open = open(filename,'r')
    the_data = get_data(file_open)
    file_open.close()
except FileNotFoundError:
    print("Filename {} not found!".format(filename))

word_list = sorted(get_words(the_data))
sets_list = make_sets(the_data)
analysis_list = analysis(word_list, sets_list)
analysis_print(word_list, analysis_list)
the_dict = count_words(the_data)
highest_list_sorted = sorted(the_dict.items())
highest_print(highest_list_sorted)