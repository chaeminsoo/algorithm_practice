n = int(input())
series = list(map(int,input().split()))
ops = list(map(int,input().split()))

min_value = 1e9
max_value = -1e9

def calcul(now,cnt):
    global series, ops, n, min_value, max_value
    
    if cnt == n:
        min_value = min(now,min_value)
        max_value = max(now,max_value)
        return

    for i in range(4):
        if ops[i] != 0:
            ops[i] -= 1

            if i == 0:
                calcul(now + series[cnt],cnt + 1)
            elif i == 1:
                calcul(now - series[cnt],cnt + 1)
            elif i == 2:
                calcul(now * series[cnt],cnt + 1)
            elif i == 3:
                calcul(int(now / series[cnt]),cnt + 1)

            ops[i] += 1
        
calcul(series[0],1)

print(max_value)
print(min_value)