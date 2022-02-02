t = int(input())

def solution(n,field):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for i in range(n):
        for j in range(n):
            ref = []
            if i-1 >= 0:
                ref.append(field[i][j]+field[i-1][j])
            if j-1 >= 0:
                ref.append(field[i][j]+field[i][j-1])
            try:
                field[i][j] = min(ref)
            except ValueError:
                pass
    return field#[n-1][n-1]
# answer=[]
for _ in range(t):
    n = int(input())
    field = []
    for _ in range(n):
        field.append(list(map(int,input().split())))

    for i in solution(n,field):
        print(i)
#     answer.append(solution(n,field))
# for i in answer:
#     print(i)