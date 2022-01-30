n = int(input())
m = int(input())
inf = 1e9
city =[[inf]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            city[i][j] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    city[a-1][b-1] = c

for i in range(n):
    for a in range(n):
        if a == i:
            break
        for b in range(n):
            if b == i:
                break
            city[a][b] = min(city[a][b],city[a][i]+city[i][b])

for i in city:
    while True:
        try:
            i[i.index(inf)] = 0
        except ValueError:
            break

for i in city:
    print(i)