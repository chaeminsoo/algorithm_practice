def solution(N, stages):
    answer = []
    np = len(stages)
    fail_rate=[]
    stage_count = [0 for _ in range(N+1)]
    
    for stage in stages:
        stage_count[stage-1] +=1
    
    for i in range(len(stage_count)-1):
        if np == 0:
            fail_rate.append((i+1,0))
        else:
            players = stage_count[i]
            fail_rate.append((i+1,players/np))
            np-=players

    fail_rate.sort(key= lambda x:(-x[1],x[0]))
    for j in fail_rate:
        answer.append(j[0])

    return answer