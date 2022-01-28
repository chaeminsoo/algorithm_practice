n = int(input())
soldier = list(map(int,input().split()))
lds = [1]*(n)

for idx in range(n-2,-1,-1):
    ref = [1]
    for i in range(idx+1,n):
        if soldier[idx] > soldier[i]:
            ref.append(lds[i]+1)
    lds[idx] = max(ref)

print(n-max(lds))