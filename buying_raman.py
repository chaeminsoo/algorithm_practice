n = int(input())
factories = list(map(int,input().split()))

cursor_ = 0
cost = 0

while cursor_<n:
    ref = 0
    if factories[cursor_] == 0:
        cursor_ += 1

    for _ in range(3):
        try:
            if factories[cursor_+ref] != 0:
                ref += 1
        except IndexError:
            break
        else:
            break
    
    lowest = min(factories[cursor_:cursor_+ref])
    
    if ref ==1:
        cost += lowest*3
        factories[cursor_+ref-1] -= 1
    elif ref == 2:
        cost += lowest*5
    elif ref == 3:
        cost += lowest*7