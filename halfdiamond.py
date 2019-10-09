num = int(input("Number of stars: "))

for i in range(num+1):
    print("*"*i)

for j in range(1,num):
    print("*"*(num-j))