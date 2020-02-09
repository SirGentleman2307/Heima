import time
import os
Number = int(input('Enter in a nuber '))

while Number < 10:
    Number += 1
    print(Number)
    time.sleep(1)

time.sleep(1)
os.system('cls')
input('Nice')