#12100
n = int(input())
borad = []
for _ in range(n):
    a = list(map(int,input().split()))
    borad.append(a)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def moving(borad,direct):
    for r in range(n):
        for c in range(n):
            nr = r + dx[direct]
            nc = c + dx[direct]
            if nr >=0 and nr < n and nc >=0 and nc<n:
                while:
            else:
                continue
            
    return

for i in range(4):
    moving(borad,i)