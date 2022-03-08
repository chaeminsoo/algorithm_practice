#1781
n = int(input())
data = []
last_day = 0
for _ in range(n):
    d,p = map(int,input().split())
    last_day = max(last_day,d)
    data.append((d,p))

data.sort()
today = 1
ans = 0
ref = 0
while today <= last_day:
    for i in range(ref,n):
        deadline, nudle = data[i]
