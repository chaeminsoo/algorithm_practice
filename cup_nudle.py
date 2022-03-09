#1781
n = int(input())
data = []
for _ in range(n):
    d,p = map(int,input().split())
    data.append((d,p))

data.sort(key= lambda x: (-x[1],x[0]))
ref_time = 0
ans = 0
for i in data:
    deadline, nudle = i
    if ref_time < deadline:
        ans += nudle
        ref_time += 1
print(ans)