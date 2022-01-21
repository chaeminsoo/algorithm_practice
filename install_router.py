n, c = map(int,input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

start = houses[1] - houses[0]
end = houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (start+end)//2
    value = houses[0]
    cnt = 1
    
    for i in range(1,n):
        if houses[i] >= value + mid:
            value = houses[i]
            cnt+=1
    if cnt >= c:
        start = mid +1  # target is bigger
        answer = mid
    else:
        end = mid-1  # target is smaller

print(answer)