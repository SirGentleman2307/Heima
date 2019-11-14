lst = [[1, 2], [3, 4], [5, 6]]
for i in range(len(lst)):
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(lst[i],1)))

lst2 = lst.copy()

print(lst2)