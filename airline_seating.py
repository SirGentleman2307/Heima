def make_seats_list(letters_list = []):
    '''Input: number of rows and seats
    Output: A list containing letters'''

    ROWS = int(input('Enter number of rows: '))
    N_SEATS = int(input('Enter number of seats in each row: '))

    for i in range(N_SEATS):
        letters_list.append(chr(i + 65))

    return [letters_list] * ROWS

def show_seats(seat_list, FIRST_STR = '', SECOND_STR = ''):
    '''Input: list of seats
    Output: prints out all seat'''

    MID = int(len(seat_list[0])/2)
    for i in range(len(seat_list)):
        ROW = seat_list[i]

        for letter in ROW[:MID]:                # First half of letters
            FIRST_STR += letter + ' '

        for letter in ROW[MID:]:                # Scond half of letters
            SECOND_STR += letter + ' '

        print('{0:2}   {1}   {2}'.format(i + 1,
         FIRST_STR, SECOND_STR))

        FIRST_STR, SECOND_STR = '', ''

def mark_seat_taken(row, seat, seat_list):
    '''Input: row number, seat letter and list of seats
    Output: replace the seat letter with an X'''

    CURRENT_ROW = row - 1
    row_list = seat_list[CURRENT_ROW].copy()    # Make a copy to edit

    INDEX_SEAT = row_list.index(seat)

    row_list.remove(seat)                       # Replace seat letter with an X
    row_list.insert(INDEX_SEAT, 'X')

    seat_list.pop(CURRENT_ROW)                  # Replace old row with new row
    seat_list.insert(CURRENT_ROW, row_list)

def get_seat_info():
    '''Input: gets row number and seat letter from user
    Output: tuple containing the row number and seat letter'''

    number_letter = input("Input seat number (row seat): ").split()

    row_number = number_letter[0]
    seat_letter = number_letter[1]

    return row_number, seat_letter

def check_seat(row, seat, seat_list):
    '''Input: row number, seat letter and list of seats
    Output: True if user inputs a seat that can be taken,
     else Fales and prints out a error'''

    status = False
    try:                                                    # Test: If seat is a int that is an error
        int(seat)
        print("Seat number is invalid!")
    except ValueError:
        try:                                                # Test: If row is an int, continue testing
            row = int(row)

            if row > len(seat_list) or row == 0:            # Test: If row is bigger then ROWS in list or row = 0, error
                print("Seat number is invalid!")
            elif len(seat) > 1:                             # Test: If seat is more then 2 letters, error
                print("Seat number is invalid!")
            elif ord(seat) - 64 > len(seat_list[row - 1]):  # Test: See if seat letter is in range of letters used in list, error
                print("Seat number is invalid!")
            elif seat not in seat_list[row - 1]:            # Test: If seat is not in row, then we know it is taken
                print("That seat is taken!")
            else:                                           # If seat and row are valid return True
                status = True

        except ValueError:
            print("Seat number is invalid!")

    return status

def main_function(seat_list):
    '''Input: list of seats
    Output: Marks a seat as taken and shows all seats'''

    while True:
        row_number, seat_letter = get_seat_info()                       # Function call: get_seat_info
        if check_seat(row_number, seat_letter, seat_list):              # Function call: check_seat
            mark_seat_taken(int(row_number), seat_letter, seat_list)    # Function call: mark_seat_taken
            show_seats(seat_list)                                       # Function call: show_seats
            break

def check_if_full(seat_list):
    '''Input: list of seats
    Output: if list is all X return True, else False'''

    for i in range(len(seat_list)):
        for j in seat_list[i]:
            if j != 'X':
                return False
    return True

# Main Program

SEAT_LIST = make_seats_list()               # Make list of seats
show_seats(SEAT_LIST)                       # Print list

main_function(SEAT_LIST)

while True:

    if check_if_full(SEAT_LIST):
        break

    answer = input("More seats (y/n)? ")
    if answer == 'y':
        main_function(SEAT_LIST)
    else:
        break