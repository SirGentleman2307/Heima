


class Display:

    def __init__(self, bord, x_list, y_list):
        self.main = bord
        self.size = len(bord)
        self.X = x_list, len(max(x_list, key=len))
        self.Y = y_list, len(max(y_list, key=len))

        self.main_b = self.main_body()
        self.X_b = self.add_x_body()
        self.Y_b = self.add_y_body()


    def main_body(self):
        ''''''
        output_list = []
        output_list.append('╔═══' + '╦═══' * (self.size - 1) + '╗')     # Start

        for element in self.main:
            output_list.append('║ ' + ' ║ '.join([str(int) for int in element]) + ' ║')       # First line to add
            output_list.append('╠═══' + '╬═══' * (self.size - 1) + '╣') # Second line to add

        output_list.pop()                                               # Remove extra
        output_list.append('╚═══' + '╩═══' * (self.size - 1) + '╝')     # Stop

        return output_list

    def add_x_body(self):
        ''''''
        X_numbers, x_max = self.X

        output_list = ['┌───'+ '┬───' * (self.size - 1) + '┐' ] # First line

        for number_list in X_numbers:       # Resize all
            while len(number_list) != x_max:
                number_list.insert(0, ' ')

        for i in range(x_max):
            output_list.append('│ ' + ' │ '.join([number[i] for number in X_numbers]) + ' │')
        output_list.append('└───' + '┴───' * (self.size - 1) + '┘')
        return output_list

    def add_y_body(self):
        ''''''
        y_numbers, y_max = self.Y

        output_list = ['┌──' + '──' * (y_max - 1) + '─┐']

        for number_list in y_numbers:
            while len(number_list) != y_max:
                number_list.insert(0, ' ')

        for element in y_numbers:
            output_list.append('│ ' + ' '.join(element) + ' │')
            output_list.append('├──' + '──' * (y_max - 1) + '─┤')

        output_list.pop()
        output_list.append('└──' + '──' * (y_max - 1) + '─┘')
        return output_list

    def edit_main_body(self, new_bord):
        ''''''
        self.main = new_bord
        self.main_b = self.main_body()


    def __str__(self):
        ''''''
        output_list = [] 
        # '          ' 10

        for element in self.X_b:
            output_list.append(' ' * (len(self.Y_b[0]) + 1) + str(element))

        for i in range(len(self.main_b)):
            output_list.append(str(self.Y_b[i]) + ' ' + str(self.main_b[i]))

        return '\n'.join(output_list)

#-----------------------------------

if __name__ == "__main__":

    Body = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    x_hint = [['1','1','1'], ['1','1'], ['3'], ['1','1'], ['1','1']]
    y_hint = [['1','1','1'], ['3'], ['1','1'], ['1','1'], ['1','1']]

    C = Display(Body, x_hint, y_hint)

    print(C)
    input()
