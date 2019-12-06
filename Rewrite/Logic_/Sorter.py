
class Sorter:

    def __init__(self):
        self.me = "me"

    def sort_by_job(self, crew_list):
        ''' Takes in a list of all crew members, sorts them by their job title and returns them'''
        pilots = []
        crew = []
        for person in crew_list:  # itterates through the crew list
            if person.get_type() == "Pilot":  # places pilots in one list
                pilots.append(person)
            else:
                crew.append(person)  # places crewmembers in another
        master_list = pilots + crew  # adds the lists together
        return master_list 
    

    def sort_into_dates(self, voyages):
        ''' Takes in a list of voyages and sorts them by when they are flying '''
        ret_dict = {}
        for voyage in voyages:  # Goes through all voyages
            time = voyage.get_date()  # saves the date of flight and the staff in the flight
            staff = voyage.get_staff()
            if not ret_dict[time]:  # if the time is not already in the dict add it
                ret_dict[time] = staff 
            else:  # else if it exists add staff members to it
                ret_dict[time] += staff
        return ret_dict


