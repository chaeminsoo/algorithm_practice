n = int(input())
factories = list(map(int,input().split()))

cursor_ = 0
cost = 0

while cursor_ < n:
    if factories[cursor_] == 0:
        cursor_ +=1
        continue
    ref = cursor_
    while factories[ref] != 0:
        ref += 1
        if ref == cursor_ + 2:
            break

    if ref == cursor_:
        cost += 3*factories[cursor_]
        factories[cursor_] = 0
    elif ref == cursor_+1:
        stand = min(factories[cursor_],factories[cursor_+1])
        cost += 5*stand
        for i in range(2):
            factories[cursor_+i] -= stand
    elif ref == cursor_+2:
        if factories[cursor_+1] > factories[cursor_+2]:
            stand = min(factories[cursor_],factories[cursor_+1])
            cost += 5*stand
            for i in range(2):
                factories[cursor_+i] -= stand
        else:
            stand = min(factories[cursor_],factories[cursor_+1],factories[cursor_+2])
            cost += 7*stand
            for i in range(3):
                factories[cursor_+i] -= stand

print(cost)