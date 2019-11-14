# -----File of things I know-----

# -----Get input(string, number, float)-----
GetInputString = input('Input string: ')
GetInputNumber = int(input('Input number: '))
GetInputFloat = float(input('Input float: '))

# -----Format string-----
String = '{}'.format('Hello World')
# Moded spaceing
StringSpaceing = '{:-^10}{:_>10},{:3<8}'.format('Hello','World','Again')
print('Formating = ' + StringSpaceing)
# Selct part of a string (.5)
StringPart = '{:_>10.5}'.format('Hello World')
print('Part = ' + StringPart)
# Moded number .2f
StringNumberF = '{:.2f}'.format(1.2345)
print('F = ' + StringNumberF)
# Modede number +4d
StringNumberD = '{:+4d}'.format(250)
print('D = ' + StringNumberD)

# -----Math things-----
# // How maney times Number2 gose up to Number 1
print('100//9 = {}'.format(100//9))