n = int(input())

fear = list(map(int,input().split()))

fear.sort(reverse=True)

cnt=0

while fear:
    now = fear[0]
    
    if now > n:
        fear = fear[1:]
        continue
    
    fear = fear[now:]
    cnt+=1

print(cnt)