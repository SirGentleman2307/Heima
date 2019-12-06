import string

class Destination:

    def __init__(self, country=None, airport=None, distance=None, contact=None, contact_phone=None): # Setting everything to none, so it is empty 
        self.__country = country
        self.__airport = airport
        self.__distance = distance
        self.__contact = contact
        self.__contact_phone = contact_phone

    def __str__(self): # Function to changes everything to a string so we can print it 
        str_to_return = "Country: {}\nAirport: {}\nDistance: {}\nContact: {}\nContact phone: {}".format(self.__country, self.__airport, \
             self.__distance,self.__contact, self.__contact_phone)
        return str_to_return


    def edit_country(self, country):  
        for letter in country: # Makes sure that country names only include letters
            if letter in string.punctuation:   # Country doesn't include punctuation
                return False
            elif letter in string.digits:      # Country doesn't include numbers
                return False
        self.__country = country  # If the country input is acceptable set the country and return True
        return True

    def edit_airport(self, airport):  
        for letter in airport: # Makes sure that airport names don't include any invalid characters
            if letter in string.punctuation:    # Makes sure airport's don't include punctuation
                return False
            elif letter in string.digits:       # Makes sure airport's don't include numbers
                return False
        self.__airport = airport # If the airpot input is acceptable set the airport and return True 
        return True

    def edit_distance(self, distance):      # Makes sure that distances are only written with numbers
        self.__distance = distance 
        return distance.isalnum()           

    def edit_contact(self, contact):        # Makes sure the contact's name only includes letters
        for letter in contact:
            if letter in string.punctuation:   # Check if the contact has no punctuations
                return False
            elif letter in string.digits:      # Check if the contact has no numbers
                return False
        self.__contact = contact               # If the contact input is acceptable set the contact and return True 
        return True

    def edit_contact_phone(self, contact_phone):   # Contact's emergency phone number only includes numbers
        if len(contact_phone) != 7 or contact_phone.isalnum() == False:    # And is only 7 digits long
            return False
        else:
             self.__contact_phone = contact_phone     # If the contact's phone input is acceptable set the contact's phone and return True 
             return True



    

   