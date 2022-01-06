def solution(N, stages):
    answer = []
    num_players = len(stages)
    max_num_players = num_players-1
    fail_rate=[]
    stages.sort()

    cnt = 0
    index=0
    for i in range(1,N+1):
        while index < max_num_players:
            if i == stages[index]:
                cnt+=1
                index+=1
                continue
            else:
                break
        fail_rate.append((i,cnt/num_players))
        num_players-=cnt
        cnt = 0
        
    fail_rate.sort(key= lambda x: (-x[1],x[0]))

    for i in fail_rate:
        answer.append(i[0])

    return answer

print(solution(4,[4,4,4,4,4]))
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))