t = int(input())
n,m = map(int,input().split())
nm = []
gold = []

for _ in range(t):
    nm.append(tuple(map(int,input().split())))
    gold.append(list(map(int,input().split())))


def moving(gold,coordinate,n,m,ref):
    r,c = coordinate
    ref += gold[r][c]
    if c+1 >= m:
        return ref
    for i in (-1,0,1):
        if r+i >=0 and r+i <=n:
            moving(gold,coordinate,r+i,c+1,ref)

def solution(nm,gold):
    n,m = nm
    answer=[]
    gold_field = []

    for i in range(0,n):
        gold_field.append(gold[m*i:m*(i+1)])
        
    cnt=1
    for i in gold:
        gold_field[cnt//m].append(i)
        cnt+=1

    for k in range(n):
        ref = 0
        answer.append(moving(gold_field,(k,0),n,m,ref))

    return max(answer)

for i in range(t):
    print(solution(nm[i],gold[i]))