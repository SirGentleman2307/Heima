num = int(input("Enter radius of the diamond: "))

world_temp = ''

for i in range(1,num+1):
    world_temp += ' '*(num-i) + '*'*((i*2)-1)
    print(world_temp)
    world_temp = ''

for j in range(num-1,0,-1):
    world_temp += ' '*-(j-num) + '*'*((j*2)-1)
    print(world_temp)
    world_temp = ''