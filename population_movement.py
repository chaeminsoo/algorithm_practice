n,l,r = map(int,input().split())

A=[]
for i in range(n):
    row = list(map(int,input().split()))
    A.append(row)

dr=[-1,1,0,0]
dc=[0,0,-1,1]
check = True

def union():
    check = False
    return 

def move():
    return

result = 0

while check == False:
    for i in range(n):
        for j in range(n):
            union(i,j)

    move()

    result+=1

print(result)