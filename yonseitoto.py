#12018
n,m = map(int,input().split())
small_mil = []
for _ in range(n):
    applica, limit = map(int,input().split())
    mil = list(map(int,input().split()))
    if applica < limit:
        small_mil.append(1)
    else:
        mil.sort(reverse=True)
        small_mil.append(mil[limit-1])
small_mil.sort()
cnt=0
for i in small_mil:
    m -= i
    if m >= 0:
        cnt += 1
    else:
        break
print(cnt)