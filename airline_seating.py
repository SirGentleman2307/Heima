
def make_airline_seats(rows, n_seats, letters_list = [], seats_list = []):

    for i in range(n_seats):
        letters_list.append(chr(i+65))

    for j in range(rows):
        seats_list.append(letters_list)

    return seats_list

def print_airline_seats(seats_list):

    LENGTH = len(seats_list[0])

    for i in range(len(seats_list)):
        print("{0:2}".format(i + 1), end='   ')
        for j in range(len(seats_list[i])):
            if j < LENGTH/2:
                print("{}".format(seats_list[i][j]),end=" ")
            elif j == LENGTH/2:
                print("  {}".format(seats_list[i][j]), end=" ")
            elif j == LENGTH - 1:
                print("{}".format(seats_list[i][j]))
            else:
                print("{}".format(seats_list[i][j]), end=" ")

def take_seat(row, seat, seats_list):
    row_list = seats_list[row - 1].copy()
    if seat in row_list:
        index_seat = row_list.index(seat)
        row_list.remove(seat)
        row_list.insert(index_seat, 'X')
        seats_list.pop(row - 1)
        seats_list.insert(row - 1, row_list)

def get_seat_info():
    seat = input("Input seat number (row seat): ")
    temp = seat.split()
    temp_row = int(temp[0])
    temp_seat = temp[1]
    return temp_row, temp_seat

def cheek_seat(row, seat, seats_list):

    x = False
    if row > len(seats_list):
        print("Seat number is invalid!")
    elif ord(seat) - 64 > len(seats_list[row - 1]):
        print("Seat number is invalid!")
    elif seat not in seats_list[row - 1]:
        print("That seat is taken!")
    else:
        x = True
    return x 

def get_seat_taken(SEATS_LIST):
    while True:
        row_number, seat_letter = get_seat_info()
        if cheek_seat(row_number, seat_letter, SEATS_LIST):
            take_seat(row_number, seat_letter, SEATS_LIST)
            print_airline_seats(SEATS_LIST)
            break

# Main Program

ROWS = int(input("Enter number of rows: "))
N_SEATS = int(input("Enter number of seats in each row: "))

SEATS_LIST = make_airline_seats(ROWS, N_SEATS)

print_airline_seats(SEATS_LIST)

get_seat_taken(SEATS_LIST)

while True:
    x = input("More sets (y/n)? ")
    if x == 'y':
        get_seat_taken(SEATS_LIST)
    else:
        break
