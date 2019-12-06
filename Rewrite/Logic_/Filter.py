class Filter:

    def __init__(self):
        pass
    
    def filter_staff(self, staff_type, staff_list):
        '''Takes in a list of staff members and what type the users wants,
           sorts the classes by that type and returns them'''
        output_classes = []
        for staff in staff_list:  # iterating through all the staff
            if staff_type == staff.get_type():  # sorting the staff out by desired output
                output_classes.append(staff)
        return output_classes

    def filter_pilot_by_airplane(self, pilot_list, airplane):
        '''Takes in a list of staff and what airplane we are looking for,
           returns the correct staff members'''
        output_list = []
        for pilot in pilot_list:
            if pilot.get_airplane() == airplane:  # checks if the pilot has a licence on the specified airplane
                output_list.append(pilot)
        return output_list

    def filter_staff_by_date(self, date, voyages):
        '''Takes in a list of voyages and a date, filters by date and returns 
            the list of staff members'''
        staff_list = []
        for voyage in voyages:
            if date in voyage.get_date():
                staff_list.append(voyage.get_staff())
        return staff_list
