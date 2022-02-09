n,m = map(int,input().split())
roads = []
total_power = 0
costs = 0
for _ in range(m):
    x,y,z = map(int,input().split())
    total_power+=z
    roads.append((z,x,y))

parent = []
for i in range(n):
    parent.append(i)

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

roads.sort()

for road in roads:
    cost, a, b = road
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        costs+=cost

print(total_power-costs)