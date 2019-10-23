class Item():

    def __init__(self, name = '', category = ''):
        self.name = name
        self.category = category

    def set_name(self, name = ''):
        self.name = name

    def set_category(self, category = ''):
        self.category = category

    def __str__(self):
        return 'Name: {}, Category: {}'.format(self.name, self.category)

class Catalog():

    def __init__(self, name = ''):
        self.name = name
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
            STR = 'Catalog {}: '.format(self.name)
        else:
            STR = 'Catalog {}: '.format(self.name) + '\n\t'+ '\n\t'.join(self.list)
        return STR

# ---Main Program ---

item1 = Item("Green Book", "Biography")
print(item1)

item2 = Item("The God", "Crime")
print(item2)

item2.set_name("The Godfather")
print(item2)

item3 = Item("Schindler's List", "Biography")
print(item3)
item3.set_category("Drama")
print(item3)

catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
print(catalog)

catalog.remove(item2)
print(catalog)

catalog.set_name("Favorite Movies")
print(catalog)

print(catalog.find_item_by_name("Green Book"))
print(catalog.find_item_by_name("The Godfather"))

catalog.clear()
print(catalog)