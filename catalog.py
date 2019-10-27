class Item():
    '''Input: film's name and its' category

    -----Class attributes-----
    __init__: Saves private instance variables name and category
    set_name: Renames an instance variables' name
    set_category: Renames an instance varibles' category
    __str__: Returns a string with the instance varibles' name and category'''

    def __init__(self, name = '', category = ''):
        self.__name = name
        self.__category = category

    def set_name(self, name = ''):
        self.__name = name

    def set_category(self, category = ''):
        self.__category = category

    def __str__(self):
        return 'Name: {}, Category: {}'.format(self.__name, self.__category)

class Catalog():
    '''Input: catalog name and collection of variables of type Item

    -----Class attributes-----
    __init__: Saves private instance variables name and collection
    add: Adds a veriable of type Item to instance variables' collection
    remove: Removes a veriable of type Item from instance variables' collection
    set_name: Renames an instance variables' name
    find_item_by_name: Finds the inputed string in instance variables' collection and retruns string
    clear: Clears every thing in instance variables' collection
    __str__: Returns a string with the instance varibles' name and every thing in its' collection'''

    def __init__(self, name = '', collection = []):
        self.__name = name
        self.__collection = collection

    def add(self, item = ''):
        self.__collection.append(item.__str__())

    def remove(self, item = ''):
        self.__collection.remove(item.__str__())

    def set_name(self, name = ''):
        self.__name = name

    def find_item_by_name(self, string):
        STR = 'None'
        for element in self.__collection:
            if string in element:
                STR = element
        return STR

    def clear(self):
        self.__collection = []

    def __str__(self):
        if self.__collection:
            STR = 'Catalog {}:\n\t'.format(self.__name) + '\n\t'.join(self.__collection)
        else:
            STR = 'Catalog {}:'.format(self.__name)
        return STR