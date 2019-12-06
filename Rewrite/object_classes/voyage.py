
class Voyage():
    def __init__(self, pilots, crew, destination, departure_date, departure_time, arrival_date, arrival_time, flight_num, valid):
        self.__pilots = pilots
        self.__crew_members = crew
        self.__destination = destination
        self.__departure_date = departure_date
        self.__departure_time = departure_time
        self.__arrival_date = arrival_date
        self.__arrival_time = arrival_time
        self.__flight_num = flight_num
        self.__valid = valid

    def __str__ (self): # Function to change every thing to a string so the program can print it 
        pass

    def edit_departure(self, departure):
        self.__departure = departure


    def edit_date(self, date):
        date_check = self.check_date(date)
        if date_check:
            self.__departure_date = date
            return True
        else:
            return False


    def edit_time(self, time):
        time_check = self.check_time(time)
        if time_check:
            self.__departure_time = time
            return True
        else:
            return False
       

    def add_pilot(self, pilot):
        self.__pilots.append(pilot)


    def check_date(self, date):     # Maybe add to check if numbers are valid later
        """
        Input: date
        Output: True if date is NOT on format YEAR-MM-DD, else False
        """
        date_list = date.split("-") # Split the list in to three lists on the dash 
        for number in date_list:
            if not number.isalnum():
                return False 
        if len(date_list) != 3: # If the date is not equal to 3 and return True
            return False
        elif len(date_list[0]) != 4 or date_list[0].isalnum() == False: # If the first list is not equal to 4 and return True 
            return False
        elif (len(date_list[1]) != 2) and (len(date_list[2]) != 2): # If the second and third lists are not equal to 2 and then return True 
            return False 
        else:
            return True

    def check_time(self, time):     # Maybe add to check if numbers are valid later
         """
        Input: clock time
        Output: True if clock is NOT on format HH:MM:SS, else False
         """
         time_list = time.split(":") # Split the list on the colon 
         if len(time_list) != 3:
             return False
         for item in time_list:
             if len(item) != 2 or time_list[1].isalnum() == False:
                 return False
         return True

         


        #  is_fail = True
        #  while is_fail:      # While user input is wrong
        #      print("List of pilots:")
        #      for number, pilot in enumerate(self.pilot_list):
        #          print("{}. {}".format(number + 1, pilot))
      
        #      try:
        #          pilot_choice_inp = int(input("Input number of pilot to add to flight: "))
               
        #      except ValueError:
        #          print("")
        #          print("Invalid input, please enter a number:")      # If user did not input a number throw error
        #          continue
        #      if pilot_choice_inp != 0:       # Fix out of bounds
        #          try:
        #              self.crew_list.append(self.pilot_list[pilot_choice_inp - 1])
                   
        #          except IndexError:
        #              print("")
        #              print("Invalid input, valid pilot numbers range from {} to {}".format(1, len(self.pilot_list)))
        #              continue
        #      wrong_inp = True
        #      while wrong_inp:        # While user inputs neither y or n
        #          more_inp = input("Do you want to add more pilots to the list? (y/n): ").lower()
        #          if (more_inp == "y") or more_inp == "n":
        #              wrong_inp = False       # If user input either "y" or "n" he did not input wrong
        #              #Print("")
        #              if more_inp == "n":
        #                  is_fail = False     # If user inputs "n" make the main loop variable false and end the loop
        #          else:
        #              print("Please enter y (yes) or n (no)")
         # Print(self.crew_list)
