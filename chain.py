# 2785
n = int(input())
chains = list(map(int,input().split()))
chains.sort(reverse=True)
ans = 0
if n == 2:
    print(1)
else:
    ref = chains.pop()
    n -= 1
    while ref > 0:
        ref -= 1
        ans += 1
        n -= 1
        if n == 1:
            if ref == 0:
                break
            else:
                ans += 1
                break
        elif n != 1 and ref == 0:
            ref = chains.pop()
            n -= 1
    print(ans)