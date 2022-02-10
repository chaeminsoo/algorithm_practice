n = int(input())
planet_x = []
planet_y = []
planet_z = []
for i in range(n):
    x,y,z = map(int,input().split())
    planet_x.append((x,i))
    planet_y.append((y,i))
    planet_z.append((z,i))

planet_x.sort()
planet_y.sort()
planet_z.sort()

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

for dists in planet_x,planet_y,planet_z:
    for j in range(1,len(dists)):
        new_dist = abs(dists[j-1][0]-dists[j][0])
        ternals.append((new_dist,dists[j-1][1],dists[j][1]))

ternals.sort()
total_money = 0
for ternal in ternals:
    money, a, b = ternal
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total_money+=money

print(total_money)