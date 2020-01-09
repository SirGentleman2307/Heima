x = 'Kek;Lol;YOLO'

y = len([i for i in range(len(x)) if x.startswith(';', i)])
print(y)
print(x.count(';'))