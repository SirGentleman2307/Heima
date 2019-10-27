class Item():

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

    def __init__(self, name = ''):
        self.__name = name
        self.list = list()

    def set_name(self, name = ''):
        self.__name = name

    def add(self, item = ''):
        self.list.append(item.__str__())

    def remove(self, item = ''):
        self.list.remove(item.__str__())

    def find_item_by_name(self, string = ''):
        STR = 'None'
        for element in self.list:
            if element.find(string) > 0:
                STR = element
        return STR

    def clear(self):
        self.list = []

    def __str__(self):
        if len(self.list) == 0:
            STR = 'Catalog {}:'.format(self.__name)
        else:
            STR = 'Catalog {}:'.format(self.__name) + '\n\t' + '\n\t'.join(self.list)
        return STR

item1 = Item("12 Angry Men", "Drama")
item2 = Item("The Godfather", "Crime")
item3 = Item("Schindler's List", "Biography")
item4 = Item("Pulp Fiction", "Crime")
catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
catalog.add(item4)
print(catalog)