# 2831
import sys
input = sys.stdin.readline

n = int(input())
men_u = []
men_d =  []
data = list(map(int,input().split()))
for i in data:
    if i > 0:
        men_u.append(i)
    else:
        men_d.append(i)
women_u = []
women_d =  []
data = list(map(int,input().split()))
for i in data:
    if i > 0:
        women_u.append(i)
    else:
        women_d.append(i)
men_d.sort(reverse=True)
men_u.sort()
women_d.sort(reverse=True)
women_u.sort()

ans = 0
while men_d and women_u:
    if men_d[-1] + women_u[-1] < 0:
        ans += 1
        men_d.pop()
        women_u.pop()
    else:
        women_u.pop()
while men_u and women_d:
    if men_u[-1] + women_d[-1] < 0:
        ans += 1
        men_u.pop()
        women_d.pop()
    else:
        men_u.pop()
print(ans)