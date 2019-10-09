
def make_airline_seats(rows, n_seats, letters_list = [], seats_list = []):

    for i in range(n_seats):
        letters_list.append(chr(i+65))

    for j in range(rows):
        seats_list.append(letters_list)

    return seats_list

def print_airline_seats(seats_list):

    LENGTH = len(seats_list[0])

    for i in range(len(seats_list)):
        print(" {}".format(i + 1), end='   ')
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

def cheek_seat():
    pass

# Main Program

ROWS = int(input("Enter number of rows: "))
N_SEATS = int(input("Enter number of seats in each row: "))

SEATS_LIST = make_airline_seats(ROWS, N_SEATS)

print_airline_seats(SEATS_LIST)

seat = input("Input seat number (row seat): ")
temp = seat.split()
temp_row = int(temp[0])
temp_seat = temp[1]

take_seat(temp_row, temp_seat, SEATS_LIST)

print_airline_seats(SEATS_LIST)