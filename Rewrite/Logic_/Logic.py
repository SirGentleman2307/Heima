from Data.data_class import Data
from object_classes.staff_creator import Staff
from Logic_.Sorter import Sorter
from Logic_.Filter import Filter

class Main_logic:

    def __init__(self):
        '''Initializing the data layer and all extra logical layers'''
        self.__Data = Data()
        self.__Sorter = Sorter() 
        self.__Filter = Filter()
    
    def save_instance(self, instance):
        '''Takes in a class instance and passes it on to the data layer'''
        saved = self.__Data.get_class_to_save(instance)
        return saved  # returns a boolean letting the user know if the class was saved sucsessfully

    def get(self, get_type):
        '''Gets the specified item from the data layer, if it needs to be filtered, calls the filter class'''
        type_list = self.__Data.get(get_type)  # saves the instances from the data layer

        if get_type == "Pilot" or get_type == "Crew":  # if the user wants either the pilot or crew then we need to filter for him
            output_list = self.__Filter.filter_staff(get_type, type_list)
        
        elif get_type == "Airplane":
            output_list = self.__Data.get("Airplane")
        
        elif get_type == "Destinations":
            output_list = self.__Data.get("Destinations")
        
        return output_list

    def get_pilot_by_airplane(self, airplane):
        '''Takes in an airplane type, sorts staffmembers by the specified ariplane and returns it'''
        output_list = self.__Data.get("Pilot")  # gets all staff members
        output_list = self.__Filter.filter_pilot_by_airplane(output_list ,airplane)  # filters by user specified airplane
        return output_list
    
    def get_sorted_staff(self):
        '''Gets all staff member sorted by their jobs'''
        staff_list = self.__Data.get("Crew")  # gets all staff members
        staff_list = self.__Sorter.sort_by_job(staff_list)  # sorts them all
        return staff_list

    def get_sorted_staff_by_date(self):
        '''Get's all staff members and places them in to a dictionary by date'''
        voyage_list = self.__Data.get("voyage")
        voyage_dict = self.__Sorter.sort_into_dates(voyage_list)
        return voyage_dict

    def get_filtered_staff_by_date(self, date):
        '''Gets a specific date by the user and pulls all staff members working that date'''
        voyage_list = self.__Data.get("voyage")
        staff_list = self.__Filter.filter_staff_by_date(date, voyage_list)
        return staff_list
        
