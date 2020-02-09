import DisplayClass



class Game:

    def __init__(self, X_hint, Y_hint, input_int):
        self.X_hint = X_hint
        self.Y_hint = Y_hint
        self.Bord = self.staring_bord(input_int)
        self.Display = DisplayClass.Display(self.Bord, X_hint, Y_hint)

    def staring_bord(self, input_int):
        ''''''
        return [['0'] * input_int for _ in range(input_int)]

    def play(self):
        ''''''
        print(self.Display)
        while C.get_input('Enter in a X,Y to change'):
            print(self.Display)

    def get_input(self,q_str = ''):
        ''''''
        try:
            X, Y = input('{}: '.format(q_str)).split(',')
            if X == 'q' or Y == 'q':
                return False

        except ValueError:
            print('Index out of range !!!')
            return True

        X, Y = int(X), int(Y)
        if X > len(self.Bord[0]) - 1 or Y > len(self.Bord[0]) - 1:
            print('Index out of range !!!')
            return True

        if self.Bord[Y][X] == '0':
            self.Bord[Y][X] = '1'
            self.Display.edit_main_body(self.Bord)
            return True

        else:
            self.Bord[Y][X] = '0'
            self.Display.edit_main_body(self.Bord)
            return True

    def __str__(self):
        ''''''
        return str(self.Bord)

x_hint = [['1','1','1'], ['1','1'], ['3'], ['1','1'], ['1','1']]
y_hint = [['1','1','1'], ['3'], ['1','1'], ['1','1'], ['1','1']]
C = Game(x_hint, y_hint, 5)

C.play()