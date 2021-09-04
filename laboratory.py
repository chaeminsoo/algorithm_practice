n,m = map(int,input().split())

field = []
for _ in range(n):
    row = list(map(int,input().split()))
    field.append(row)
# 4-way
dx = [-1,0,1,0]
dy = [0,1,0,-1]

