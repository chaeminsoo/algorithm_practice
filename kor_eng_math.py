n = int(input())

info=[]
for _ in range(n):
    info.append(tuple(input().split()))

info.sort(key= lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
# info.sort()
# info.sort(reverse=True,key=lambda x:int(x[3]))
# info.sort(key=lambda x:int(x[2]))
# info.sort(reverse=True,key=lambda x:int(x[1]))

for i in info:
    print(i[0])