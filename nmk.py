# 1201
n,m,k = map(int,input().split())
series_ = []
for i in range(n):
    series_.append(i+1)

if m+k-1 <= n <= m*k:
    ans = []
    new_s = [series_[i:i+k] for i in range(0,n,k)]
    while len(new_s) != m:
        for i in range(-1,-n,-1):
            if len(new_s[i]) == 1:
                continue
            else:
                ref = new_s.pop(i)
                new_s.append(ref[:-1])
                new_s.append(ref[-1:])
                new_s.sort()
                break
    for i in new_s:
        i.reverse()
        ans.extend(i)
    for i in ans:
        print(i,end=' ')
else:
    print(-1)