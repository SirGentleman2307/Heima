import string


class Staff: 

    def __init__(self, ssn=None, name=None, job_title=None, email=None, mobile=None, landline=None, address=None, airplane=None): # Setting everything to none, so it is empty 
        self.__job_title = job_title
        self.__name = name
        self.__ssn = ssn
        self.__address = address
        self.__email = email
        self.__mobile = mobile
        self.__landline = landline
        self.__airplane = airplane


    def __str__(self): # Function to changes everything to a string so the program can print it 
        return ("Name: {}\nSSN: {}\nJob title:{} \nAddress: {}\nEmail: {}\nMobile: {}\nLandline: {}\nAirplane: {}".format(self.__name,self.__ssn,self.__job_title,self.__address,self.__email,self.__mobile,self.__landline,self.__airplane))

    def display_str(self):
        return ("{:20}{:15}{:<10}{:<10}{:<25}{:<10}{:10}{:5}".format(self.__name,self.__ssn,self.__job_title,self.__address,self.__email,self.__mobile,self.__landline,self.__airplane))

    def edit_name(self, name):
        '''Takes in a name, error checks it, if the name is acceptable
        return True, else return False '''
        for letter in name:  # Irretates through the name
            if letter in string.punctuation or letter in string.digits:  # Checks if the name has any punctuation or numbers
                return False  # Return false, because the input is wrong and it has either punctuatuins or digits 
        self.__name = name  # If the name input is acceptable, set the name and return True
        return True
    
    def edit_ssn(self, ssn):
        '''Takes in a ssn, error checks it, if the ssn
        is written in the correct format, save it, else return False '''
        ssn_list = ssn.split("-")  # Splits the SSN on dash
        if len(ssn_list) != 2:  # Makes sure that the SSN had a dash
            return False
        if len(ssn_list[0]) != 6 or ssn_list[0].isalnum() == False:  # Make sure that the first part of the ssn has 6 numbers
            return False
        if len(ssn_list[1]) != 4 or ssn_list[0].isalnum() == False:  # Make sure that the second part of the ssn has 4 numbers
            return False
        self.__ssn = ssn # If the SSN input is acceptable set the SSN and return True
        return True

    def edit_email(self, email):
        '''Takes in an email, error checks if @nanair.is is missing, return False,
        else save the email and return True'''
        if "@nanair.is" not in email.lower():  # Checks if @nanair.is is in the email
            return False        
        else:
            self.__email = email # If the email input is acceptable set the email and return True
            return True       

    def edit_mobile(self, mobile):
        '''Takes in mobile and error checks if the number's lenght is 7 digits and if it only contains numbers,
        return False, else save the mobile number and return True'''
        if len(mobile) != 7 or mobile.isalnum() == False: # Checks if lenght is 7 and only contains numbers
            return False
        else:
            self.__mobile = mobile # If the mobile input is acceptable set the mobile and return True 
            return True

    def edit_landline(self, landline):
        '''Takes in landline and error checks if the number's lenght is 7 digits and if it only contains numbers,
        return False, else save the landline number and return True '''
        if len(landline) != 7 or landline.isalnum() == False: # Checks if lenght is 7 and only contains numbers
            return False
        else:
            self.__landline = landline # If the landline input is acceptable set the landline and return True 
            return True

    def ssn_check(self): # Function to check if the SSN is correctly input
        ssn_list = self.__ssn.split("-") # Here we split the list in to two lists on the "-"
        if len(ssn_list) != 2: # If the list is not equal to 2, we know the user did not enter the correct amount of "-", throw error
            return True
        if len(ssn_list[0]) != 6: # If the list is not equal to 6, throw error
            return True
        if len(ssn_list[1]) != 4: # If the list is not equal to 4, throw error
            return True
        return False # If the SSN input is acceptable, let him out of the loop

    def email_check(self, email): # Function to check if the email is correctly input
        if "@nanair.is" not in self.__email: # The email needs to have "@nanair.is"
            return True # If the email has "nanair.is", let him out if the loop 
    
    def edit_address(self,address): # Function to check if the address is correctly input
        if len(address) <= 100: # The length of the input can not be longer than 100 
            self.__address = address # If the address input is acceptable, set the address and return True 
            return True 

    def edit_airplane(self, airplane): # Function to check if the airplane is correctly input 
        self.__airplane = airplane #If the airplane is acceptable, set the airplane and retunr True 
        return True

    def get_type(self): # Function to get the jobtitle 
        return self.__job_title

    def get_airplane(self): # Funtrion to get the airplane 
        return self.__airplane
    
    def save(self): # Function to save the, SSN, name, job title, email, mobile, landline, address, and airplane 
        return "{},{},{},{},{},{},{},{}".format(self.__ssn,self.__name,self.__job_title,self.__email,self.__mobile,self.__landline,self.__address,self.__airplane)
