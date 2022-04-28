#2258
n,m = map(int,input().split())
meat = []
total = 0
for _ in range(n):
    w,c = map(int,input().split())
    total += w
    meat.append([w,c])

meat.sort(key=lambda x: (-x[1], -x[0]))
ans = 0

pre_cost = -1

for i in meat:
    weight, cost = i
    if pre_cost != cost:
        pre_cost = cost
        total += weight
        ans = cost
        if total >= m:
            break
        else:
            continue
    else:
        total += weight
        ans += cost
        if total >= m:
            break
        else:
            continue

print(meat)
print(ans)