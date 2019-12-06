import csv
import os
from object_classes.staff_creator import Staff


class Data():
    def __init__(self):
        ############# Read all files #################
        self.__path = os.getcwd() + "/Data/Repo"
        self.__crew_data = self.read_file(( self.__path + "/Crew.csv"))
        self.__airplane_data = self.read_file((self.__path + "/Airplane.csv"))
        self.__aircraft_type_data = self.read_file((self.__path + "/AircraftType.csv"))
        self.__destination_data = self.read_file((self.__path + "/Destinations.csv"))
        self.__past_flight_data = self.read_file((self.__path + "/PastFlights.csv"))
        self.__upcoming_flight_data = self.read_file((self.__path + "/UpcomingFlights.csv"))


    def get(self, query):
        """
        Input: Search term for what info logic wants
        Output: File contents initialized as its model class in list
        """
        query = query.lower()
        if query == "crew" or query == "pilot":
            initialized_list = self.initialize_object(query, self.__crew_data)              # initialize all the info in the corresponding csv file as its model class
        elif query == "airplane":
            initialized_list = self.initialize_object(query, self.__airplane_data)          # -||- (same as above)
        # elif query == "aircrafttype":
        #     initialized_list = self.initialize_object(query, self.__aircraft_type_data)   # -||- (same as above)    not neccessary atm
        elif query == "destinations":
            initialized_list = self.initialize_object(query, self.__destination_data)       # -||- (same as above)
        elif query == "voyage":
            initialized_list = self.initialize_object(query, self.__past_flight_data, self.__upcoming_flight_data)       # -||- (same as above except this time it sends 2 file lists to the function)

        return initialized_list

    def get_class_to_save(self, class_object):
        """
        Input: Class object
        Calls the objects save function
        Output: True if type is found False otherwise
        """
        the_type = class_object.get_type()                          # Get class type (string)
        the_type = the_type.lower()                                 # lowercase the string to make sure 
        if the_type == "pilot"or the_type == "flight attendant" \
             or the_type == "crew":                                 # check if type matches 
            filename = "Crew.csv"                                   # save its corresponding filename
            self.save_to_disk(class_object.save(), filename)        # call the class' save string and call function to save 
            return True                                             # return True to indicate that save was successful

        elif the_type == "airplane" or the_type == "aircraft":      # check if type matches 
            filename = "Airplane.csv"                               # save its corresponding filename
            self.save_to_disk(class_object.save(), filename)        # call the class' save string and call function to save
            return True                                             # return True to indicate that save was successful

        elif the_type == "destination":                             # check if type matches
            filename = "Destinations.csv"                           # save its corresponding filename
            self.save_to_disk(class_object.save(), filename)        # call the class' save string and call function to save
            return True                                             # return True to indicate that save was successful

        elif the_type == "voyage":
            pass                            #TODO this needs to save in 2 seperate files

        else:
            return False                                            # else return False to indicate save was not executed
        

    def initialize_object(self, a_query, a_list, b_list = None):
        """
        Input: query (string), at least 1 file contents list can be 2
        Takes the file contents list and initiates in its rightful class
        Output: List of class initiated content
        """
        class_object_list = []
        if a_query == "crew" or "pilot" or "flight a":
            for item in a_list[1:]:
                class_object_list.append(Staff(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))

        elif a_query == "airplane":
            for item in a_list[1:]:
                class_object_list.append(Staff(item[0], item[1], item[2]))

        # elif a_query == "aircrafttype":               # this will not be necessary atm
        #     for item in a_list[1:]:   
        #         class_object_list.append(Staff())

        elif a_query == "destinations":
            for item in a_list[1:]:
                class_object_list.append(Staff(item[0], item[1], item[3], item[4], item[5]))

        elif a_query == "voyage":
            for item in a_list[1:]:
                class_object_list.append(Staff())       #TODO needs finishing


        return class_object_list

    def save_to_disk(self, a_string, filename):
        #TODO needs edit implementation
        
        if a_string[-1] != "\n":        # if newline is not at the end of string add it.
            a_string += "\n"

        with open(self.__path + "/" + filename, "a+", encoding= "utf-8") as result_file:
            result_file.write(a_string)


    def read_file(self, what):
        file_list = []
        with open(what, "r+", encoding= "utf-8") as file_obj:
            for line in file_obj:
                line = line.strip().split(",")
                file_list.append(line)
        return file_list


################## MAIN IDGAF
if __name__ == "__main__":
    test = Data()


    #test.save_to_disk("Captain,NAFOKKER,20:30:00,00:20:00\n \
       # Flight attendant,N/A,20:30:00,00:20:00")

    #print(test.read_file("OutputTest.csv"))