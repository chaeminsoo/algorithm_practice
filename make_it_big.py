#2812
n,k = map(int,input().split())
ref = list(map(int,input()))
ans = []
cnt = 0
for i in ref:
    if not ans:
        ans.append(i)
    else:
        while ans:
            if cnt >= k:
                break
            top = ans.pop()
            if top >= i:
                ans.append(top)
                break
            else:
                cnt+=1
                continue
        ans.append(i)
for i in ans[:n-k]:
    print(i,end='')