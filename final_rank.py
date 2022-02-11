from collections import deque

t = int(input())

def solution(n,prev_rank,changeed):
    q = deque()
    indgree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1,n):
            graph[prev_rank[i]].append(prev_rank[j])
            indgree[prev_rank[j]] += 1
    try:
        for k in changeed:
            a,b = k
            graph[b].remove(a)
            indgree[b] += 1
            graph[a].append(b)
            indgree[a] -= 1
    except ValueError:
        return 'IMPOSSIBLE'

    q.append(indgree[1:].index(0)+1)
    answer = []
    while q:
        ref = q.popleft()
        answer.append(ref)
        cnt = 0
        for i in graph[ref]:
            indgree[i] -= 1
            if indgree[i] == 0:
                q.append(i)
                cnt += 1
        if cnt >1:
            return "?"
        
    if len(answer)<n:
        return 'IMPOSSIBLE'
    else:
        return answer

real_ans = []
for _ in range(t):
    n = int(input())
    prev_rank=list(map(int,input().split()))
    m = int(input())
    changeed = []
    for _ in range(m):
        a,b = map(int,input().split())
        changeed.append((a,b))
    real_ans.append(solution(n,prev_rank,changeed))
    
for each in real_ans:
    if type(each) == str:
        print(each)
    else:
        for i in each:
            print(i,end=' ')
    print()