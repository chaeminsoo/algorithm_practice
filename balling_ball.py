n,m = map(int,input().split())

weight = list(map(int,input().split()))

cnt=1
result=0

for i in weight:

    if cnt == n:
        break

    for j in weight[cnt:]:

        if i != j:
            result+=1            
        else:
            continue
    cnt +=1


print(result)