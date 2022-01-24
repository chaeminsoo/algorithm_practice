t = int(input())
nm = []
gold = []

for _ in range(t):
    nm.append(tuple(map(int,input().split())))
    gold.append(list(map(int,input().split())))

def collect(r,c,gold_field,n):
    ref = gold_field[r][c]
    answer=[]
    if r-1 >= 0:
        answer.append(ref + gold_field[r-1][c-1])
    if r+1 < n:
        answer.append(ref + gold_field[r+1][c-1])
    answer.append(ref + gold_field[r][c-1])
    return max(answer)    

def solution(nm,gold):
    n,m = nm
    answer=0
    gold_field = []

    for i in range(0,n):
        gold_field.append(gold[m*i:m*(i+1)])

    for k in range(1,m):
        for j in range(n):
            gold_field[j][k] = collect(j,k,gold_field,n)
    
    for l in range(n):
        answer = max(answer,gold_field[l][m-1])

    return answer

for i in range(t):
    print(solution(nm[i],gold[i]))