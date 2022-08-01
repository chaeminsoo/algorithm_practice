# 2036
import sys
input = sys.stdin.readline

n = int(input())
nnt = 0
pnt = 0
nega = []
ont = 0
znt = 0
posi = []
for _ in range(n):
    a = int(input())
    if a == 0:
        znt+=1
    elif a == 1:
        ont+=1
    elif a > 0:
        posi.append(a)
        pnt += 1
    elif a < 0:
        nega.append(a)
        nnt += 1

nega.sort(reverse = True)
posi.sort()
ans = 0

if nnt >0:
    if nnt%2 == 0:
        while nega:
            n1 = nega.pop()
            n2 = nega.pop()
            ans += (n1*n2)
    else:
        while nnt > 1:
            n1 = nega.pop()
            n2 = nega.pop()
            nnt-=2
            ans += (n1*n2)
        if znt > 0:
            pass
        else:
            ans += nega.pop()
if pnt >0:
    if pnt%2 == 0:
        while posi:
            n1 = posi.pop()
            n2 = posi.pop()
            ans += (n1*n2)
    else:
        while pnt > 1:
            n1 = posi.pop()
            n2 = posi.pop()
            pnt-=2
            ans += (n1*n2)
        ans += posi.pop()
print(ans+ont)