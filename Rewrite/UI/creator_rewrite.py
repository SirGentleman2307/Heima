# Creator makes stuff


class Creator():

    def __init__(self, command_str):
        self.__command = command_str

    def run(self):
        name_str = 'new_{}'.format(self.__command)
        return self.create_staff(name_str, self.__command)

    def create_staff(self, staff, staff_type):

        name_ch, ssn_ch, email_ch, mobile_ch, landline_ch = False, False, False, False, False
        while name_ch == False:
            name = input("Please enter the {}'s name: ".format(staff_type))
            name_ch = staff.edit_name(name)
            if name_ch == False:
                print("Please use only letters and spaces in the name")

        while ssn_ch == False:
            ssn = input("Please enter the {}'s ssn: ".format(staff_type))
            ssn_ch = staff.edit_ssn(ssn)
            if ssn_ch == False:
                print("Please enter the ssn in the following format: xxxxxx-xxxx")

        while email_ch == False:
            email = input("Please enter the {}'s email: ".format(staff_type))
            email_ch = staff.edit_email(email)
            if email_ch == False:
                print("Please enter the email in the following format: name@nanair.is")

        while mobile_ch == False:        
            mobile = input("Please enter the {}'s mobile: ".format(staff_type))
            mobile_ch = staff.edit_mobile(mobile)
            if mobile_ch == False:
                print("Please enter the mobile in the following format: 1234567")

        while landline_ch == False:    
            landline = input("Please enter the {}'s landline: ".format(staff_type))
            landline_ch = staff.edit_landline(landline)
            if landline_ch == False:
                print("Please enther the landline in the following format: 1234567")

        if staff_type == "Pilot":
            Airplane = input("Please enter the {}'s Airplane: ".format(staff_type))
            staff.edit_airplane(Airplane)

        return staff
