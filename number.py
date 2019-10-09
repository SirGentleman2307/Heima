
for i in range(10,100):
    num1 = i // 10
    num2 = i % 10
    if (num1 + num2)**2 == i:
        print(i)
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 10:
        print(i)