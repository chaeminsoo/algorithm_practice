#8980
n, c = map(int,input().split())
m = int(input())
vil = [[] for _ in range(n+1)]
for _ in range(m):
    sned, reci, num_box = map(int,input().split())
    vil[sned].append([reci,num_box])

cnt = 0
car = [0]*(n+1)

