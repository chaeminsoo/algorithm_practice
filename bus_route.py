#10165
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
routes = []
ans = []
for i in range(m):
    a,b = map(int,input().split())
    if a > b:
        b += n
    else:
        routes.append([a+n,b+n,i+1])
    routes.append([a,b,i+1])
    ans.append(i+1)

routes.sort(key=lambda x:(x[0],-x[1]))

very_right = 0
pre_st = -1

for route in routes:
    st,ed,num = route
    if ed > very_right:
        very_right = ed
    else:
        ans.remove(num)

for an in ans:
    print(an,end=' ')