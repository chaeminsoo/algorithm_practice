n = int(input())
planet = []
for _ in range(n):
    x,y,z = map(int,input().split())
    planet.append((x,y,z))

def cost(a,b):
    a1,a2,a3 = a
    b1,b2,b3 = b
    return min(abs(a1-b1),abs(a2-b2),abs(a3-b3))

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

parent = []

for i in range(n):
    parent.append(i)

ternals = []

for i in range(len(planet)):
    for j in range(len(planet)):
        if i == j:
            continue
        ternals.append((cost(planet[i],planet[j]),i,j))

ternals.sort()
total_money = 0
for ternal in ternals:
    money, a, b = ternal
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total_money+=money

print(total_money)