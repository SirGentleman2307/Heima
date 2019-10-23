class Item():

    def __init__(self, __name = '', __category = ''):
        self.name = __name
        self.category = __category

    def set_name(self, name = ''):
        self.name = name

    def set_category(self, category = ''):
        self.category = category

    def __str__(self):
        return 'Name: {}, Category: {}'.format(self.name, self.category)

class Catalog():

    def __init__(self, __name = ''):
        self.name = __name
        self.list = list()

    def set_name(self, name = ''):
        self.name = name

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
            STR = 'Catalog {}:'.format(self.name)
        else:
            STR = 'Catalog {}:'.format(self.name) + '\n\t' + '\n\t'.join(self.list)
        return STR
