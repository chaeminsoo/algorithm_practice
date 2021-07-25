n =input()

ref = int(len(n)/2)
front =n[:ref]
back =n[ref:]

l_front = list(map(int,front))
l_back = list(map(int,back))

if sum(l_front) == sum(l_back):
    print('LUCKY')
else:
    print('READY')