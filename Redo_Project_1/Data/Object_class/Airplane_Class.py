

class Airplane():

    def __init__(self, plane_ID = '', plane_type = '', manufacturer = ''):

        self.__plane_ID = plane_ID
        self.__plane_type = plane_type
        self.__manufacturer = manufacturer

    def edit_plane_ID(self, new_ID_str):

        Status, Error_msg = self.test_ID(new_ID_str)
        if  Status:
            self.__plane_ID = new_ID_str
        else:
            return Error_msg

    def edit_plane_type(self, new_type_str):

        self.__plane_type = new_type_str

    def edit_manufacturer(self, new_manufacturer_str):

        self.__manufacturer = new_manufacturer_str


    def test_ID(self, User_Input_Str):
        '''Formant TF-xxx'''
        if len(User_Input_Str) != 6 or User_Input_Str[2] != '-' or User_Input_Str[0:1] != 'TF':
            return False, 'Invalid Format'
