import string
from operator import itemgetter

def open_file():
    '''Input: Filename
    Output: Open file ready to read'''

    filename = input('Enter filename: ')

    try:
        file_open = open(filename,'r')
        return file_open

    except FileNotFoundError:
        print("Filename {} not found!".format(filename))

def get_data(file_open, data_list = [], CPD = []):
    '''Input: Open file
    Output: Reads file, saves file data in a list'''
    
    for line in file_open:                  # Iterate through all lines in file
        if line == '\n':                    # Splits the data in to paragraphs
            data_list.append(CPD)           # Add current paragraph data
            CPD = []                        # Reset CPD (C.urrent P.aragraph D.ata)
        else:
            word_in_line = line.split()
            for word in word_in_line:       # Iterate through each word in line
                CPD.append(word.strip(string.punctuation).lower())

    data_list.append(CPD)                   # Last paragraph is not splited on a '\n'
    file_open.close()

    return data_list

def get_all_words(data_list, words_list = []):
    '''Input: List of data
    Output: List of all words in data'''

    for paragraph in data_list:         # Iterate through each paragraph
        for word in paragraph:          # Iterate through each word in paragraph

            if word not in words_list:
                words_list.append(word)

    return words_list

def word_paragraph_location(words_list, data_list, location_dict = {}, temp_str = ''):
    '''Input: List of data and all words in data
    Output: Dict (key = word) (value = string with location)'''

    for word in words_list:                     # Iterate through each word in the list of words
        for i in range(len(data_list)):         # Iterate through each paragraph in data
            if word in data_list[i]:            # If word in paragrahp save the i value
                temp_str += '{}, '.format(i+1)

        temp_str = temp_str[:-2]                # Need to remove ', '
        location_dict[word] = temp_str          # Add to dict
        temp_str = ''                           # Reset temp_str

    return location_dict

def show_word_location(location_dict):
    '''Input: Dict of words and locations
    Output: Prints out word and its' location'''

    location_keys_sort = sorted(location_dict.keys())       # Sort dict alphabetically
    print('The paragraph index: ')
    for word in location_keys_sort:                         # Iterate through each word
        print('{} {}'.format(word, location_dict[word]))    # Print out word and its' value in location_dict

def count_word(data_list, word_count_dict = {}):
    '''Input: List of data
    Output: Dict (key = word) (value = word count)'''

    for i in range(len(data_list)):         # Iterate through each paragraph in data list
        for word in data_list[i]:           # Iterate through each word in paragraph

            if word not in word_count_dict: # If not in dict add it/ else plus 1
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

    return word_count_dict

def show_highest_count(word_count_dict):
    '''Input: Dict of words and count
    Output: Print out all words and its' count'''

    count_keys_sort = sorted(word_count_dict.items())                               # Sort alphabetically
    highest_word_count = sorted(count_keys_sort, key=itemgetter(1), reverse=True)   # Sort by highest value

    for number in [10, 20]:                                 # Iterate though list [10, 20]
        print('\nThe highest {} counts: '.format(number))

        for i in range(number):                             # Iterate though range of number
            WORD = highest_word_count[i][0]
            VALUE = highest_word_count[i][1]
            print('{}: {}'.format(WORD, VALUE))

def main():
    '''Input: None
    Output: Runs all functions'''

    file_object = open_file()           # Get file name
    file_data = get_data(file_object)   # Read all data and save it

    words_list = get_all_words(file_data)   # Make a list of words in file data

    location_dict = word_paragraph_location(words_list, file_data)  # Make a dict with word loctions
    show_word_location(location_dict)                               # Print out locations

    word_count_dict = count_word(file_data) # Make dict with word count
    show_highest_count(word_count_dict)     # Print out highest word count


# --- Main Program ---

main()

