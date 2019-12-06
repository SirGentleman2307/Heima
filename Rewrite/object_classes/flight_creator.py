

class Flight():
    def __init__(self, departure = None, arrival = None, pilot_list = [], \
         crew_list = [], time_list = [], airplane = None, flight_num = None):

        self.departure = departure      # Input
        self.arrival = arrival          # Input
        self.pilot_list = pilot_list    # Get from data, input
        self.crew_list = crew_list      # Create from inputs
        self.time_list = time_list      # 
        self.airplane = airplane        # Input?
        self.flight_num = flight_num    # Creat

        self.departure_date = None      # Input
        self.departure_clock = None     # Input
        self.arrival_date = None        # Input
        self.arrival_clock = None       # Input

    def create_instance(self):
        time_check = True
        date_check = True
        while True:
            self.departure_date = input("Input departure date (YEAR-MM-DD): ")
            date_check = self.check_date(self.departure_date)
            if date_check:
                print("Date input wrong")
                continue
            else:
                break

        while True:
            self.departure_clock = input("Input departure time: (HH:MM:SS): ")
            time_check = self.check_time(self.departure_clock)
            if time_check:
                print("Time input wrong")
                continue
            else:
                break

        self.departure = [self.departure_date, self.departure_clock]    # Save departure date and time as 

        while True:
            self.arrival_date = input("Input arrival date (YEAR-MM-DD): ")
            date_check = self.check_date(self.arrival_date)
            if date_check:
                print("Date input wrong")
                continue
            else:
                break

        while True:
            self.arrival_clock = input("Input arrival time (HH:MM:SS): ")
            time_check = self.check_time(self.departure_clock)
            if time_check:
                print("Time input wrong")
                continue
            else:
                break

        

        print("")
        
        is_fail = True
        while is_fail:      # While user input is wrong
            print("List of pilots:")
            for number, pilot in enumerate(self.pilot_list):
                print("{}. {}".format(number + 1, pilot))
       
            try:
                pilot_choice_inp = int(input("Input number of pilot to add to flight: "))
                
            except ValueError:
                print("")
                print("Invalid input, please enter a number:")      # If user did not input a number throw error
                continue

            if pilot_choice_inp != 0:       # Fix out of bounds
                try:
                    self.crew_list.append(self.pilot_list[pilot_choice_inp - 1])
                    
                except IndexError:
                    print("")
                    print("Invalid input, valid pilot numbers range from {} to {}".format(1, len(self.pilot_list)))
                    continue

            wrong_inp = True
            while wrong_inp:        # While user inputs neither y or n
                more_inp = input("Do you want to add more pilots to the list? (y/n): ").lower()
                if (more_inp == "y") or more_inp == "n":
                    wrong_inp = False       # If user input either "y" or "n" he did not input wrong
                    #Print("")
                    if more_inp == "n":
                        is_fail = False     # If user inputs "n" make the main loop variable false and end the loop
                else:
                    print("Please enter y (yes) or n (no)")

        # Print(self.crew_list)



    def save_instance(self):
        pass

    def update_instance(self):
        pass

    def check_date(self, date):     # Maybe add to check if numbers are valid later
        """
        Input: date
        Output: True if date is NOT on format YEAR-MM-DD, else False
        """
        date_list = date.split("-")
        if len(date_list) != 3:
            return True
        elif len(date_list[0]) != 4:
            return True
        elif (len(date_list[1]) != 2) and (len(date_list[2]) != 2):
            return True
        else:
            return False

    def check_time(self, time):     # Maybe add to check if numbers are valid later
        """
        Input: clock time
        Output: True if clock is NOT on format HH:MM:SS, else False
        """
        time_list = time.split(":")
        if len(time_list) != 3:
            return True
        for item in time_list:
            if len(item) != 2:
                return True
        return False


#### Main ####

test = Flight()

test.create_instance()