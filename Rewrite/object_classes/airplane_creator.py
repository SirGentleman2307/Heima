import os
import string

class Airplane:

    NAME_LENGTH = 6    # We only want the airplane's name to be 6 letters of lenght in the format xx-xxx

    def __init__(self, name=None, plane_type=None, manufacturer=None): # Setting everything to none, so it is empty 
        self.__name = name
        self.__plane_type = plane_type
        self.__manufacturer = manufacturer

        

    def __str__(self): # Function to changes everything to a string so the program can print it 
        str_to_return = "Name: {}\nPlane type: {}\nManufacturer: {}".format(self.__name, self.__plane_type, self.__manufacturer)
        return str_to_return

   
    def edit_name(self, name):
        name_list = name.split("-") # Splits the list into two lists on the dash
        if len(name_list) != 2:  # Makes sure that the name had a dash
            return False
        if len(name_list[0]) != 2 == False:  # Make sure that the first part of the name has 2 letters
            return False
        if len(name_list[1]) != 3 == False:  # Make sure that the second part of the ssn has 4 numbers
            return False
        self.__name = name # If the name input is acceptable, set the name and return True 
        return True

    
    def edit_plane_type(self, plane_type):
        for letter in plane_type:  
            if letter in string.punctuation:  # Makes sure that the plane type doesn't include punctuation
                return False
        self.__plane_type = plane_type # If the plane type input is acceptable, set the plane type and return True 
        return True

    
    def edit_manufacturer(self, manufacturer):
        for letter in manufacturer:
            if letter in string.punctuation or letter in string.digits:  # Checks if the input has punctuation or digits 
                return False            # Makes sure the manufacture name doesn't include punctuation nor digits
        self.__manufacturer = manufacturer # If the manufacturer input is acceptable, set the manufacturer and return True 
        return True
   

        self.save_instance()

    def save_instance(self): # Function to save the name, plane type and manufacturer
        return("{},{},{}\n".format(self.__name, self.__plane_type, self.__manufacturer))



# Main program starts here 

if __name__ == "__main__":
    Wow = Airplane()
