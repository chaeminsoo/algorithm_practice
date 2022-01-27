import sys
sys.setrecursionlimit(3000)

n = int(input())
power = list(map(int,input().split()))
lds = [1]*(n)

def find_lds(idx):
    if idx <0:
        return max(lds)
    ref = [1]
    if power[idx] >= power[idx+1]:        
        for i in range(idx+1,n):
            ref.append(lds[i]+1)

    lds[idx] = max(ref)
    idx -= 1
    return find_lds(idx)

print(n-find_lds(n-2))