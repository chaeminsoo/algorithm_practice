n,m = map(int,input().split())
location=[]
for _ in range(n):
    location.append(list(map(int,input().split())))

plan = list(map(int,input().split()))

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
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    for j in range(n):
        if location[i][j] == 1:
            union_parent(parent,i,j)

main_root = find_parent(parent,plan[0])
answer = 'YES'
for k in plan:
    if main_root != find_parent(parent,k):
        answer = 'NO'
        break
print(answer)