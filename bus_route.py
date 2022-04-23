#10165
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
routes = []
ans = [True]*m
for i in range(m):
    a,b = map(int,input().split())
    if a > b:
        b += n
    else:
        routes.append([a+n,b+n,i+1])
    routes.append([a,b,i+1])

routes.sort(key=lambda x:(x[0],-x[1]))

very_right = 0

for route in routes:
    st,ed,num = route
    if ed > very_right:
        very_right = ed
    else:
        ans[num-1] = False

for an in enumerate(ans):
    idx,tf = an
    if tf:
        print(idx+1,end=' ')