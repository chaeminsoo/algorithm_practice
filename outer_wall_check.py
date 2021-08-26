from itertools import permutations

def close_num(targrt,liist):
    ref = []
    index=0
    for i in range(len(liist)):
        val = liist[i]
        distance = val-targrt
        ref.append((distance,i))
    ref.sort()
    for i in ref:
        if i[0] > 0:
            index = i[1]
            break
        else:
            continue
    return liist[index]

def solution(n, weak, dist):
    answer = 0
    wl = len(weak)
    new_weak = weak + [i + n for i in weak]
    min_cnt = float('INF')
    all_cases = list(permutations(dist,len(dist)))
    for sp in weak:
        for case in all_cases:
            cnt = 0
            weak_cnt = 0
            for friend in case:
                arrived = sp +friend

                for i in new_weak:
                    if i >= sp and i <= arrived:
                        weak_cnt +=1
                cnt += 1
                if weak_cnt >= wl:
                    min_cnt = min(min_cnt,cnt)
                    break
                else:
                    sp  = close_num(sp+friend,weak)

    answer = cnt        


    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4])) # 2
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7])) # 1