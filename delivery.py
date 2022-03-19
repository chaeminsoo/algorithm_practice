#8980
n, c = map(int,input().split())
m = int(input())
vil = [[] for _ in range(n+1)]
for _ in range(m):
    sned, reci, num_box = map(int,input().split())
    vil[sned].append([reci,num_box])

cnt = 0
car = [0]*(n+1)
storage = 0

for i in range(1,n+1):
    cnt += car[i]
    storage -= car[i]

    vil[i].sort()
    for vv in vil[i]:
        v_num, v_load = vv[0], vv[1]
        if storage+v_load <= c:
            storage += v_load
            car[v_num] +=v_load
        else:
            car[v_num] += c-storage
            storage = c
            break
        
print(cnt)