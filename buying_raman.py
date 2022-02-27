n = int(input())
factories = list(map(int,input().split()))

cursor_ = 0
answer = 0

for _ in range(2):
    factories.append(0)

while cursor_ < n:
    i1, i2, i3 = factories[cursor_], factories[cursor_+1], factories[cursor_+2]

    if i1 == 0:
        cursor_ += 1
        continue
    
    if i2 == 0:
        answer += 3*i1
        factories[cursor_] -= i1
        continue

    if i3 == 0:
        ref = min(i1,i2)
        answer += 5*ref
        factories[cursor_] -= ref
        factories[cursor_+1] -= ref
        continue

    if i2 > i3:
        ref = min(i1, i2 - i3)
        answer += 5*ref
        factories[cursor_] -= ref
        factories[cursor_+1] -= ref
        continue

    ref = min(i1,i2,i3)
    answer += 7*ref
    factories[cursor_] -= ref
    factories[cursor_+1] -= ref
    factories[cursor_+2] -= ref

print(answer)