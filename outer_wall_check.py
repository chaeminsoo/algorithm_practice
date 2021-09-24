from itertools import permutations


def close_num(target,liist):
    ref = 0
    for i in liist:
        if i >= target:
            ref = i
            break
    return ref

def solution(n, weak, dist):
    wl = len(weak)
    new_weak = weak + [i + n for i in weak] # 원 표현
    min_cnt = 100#float('inf')
    all_cases = list(permutations(dist,len(dist))) # 확인할 친구 순서 모든 경우의 수
    for sp in weak: # 시작점 바꿔가며
        for case in all_cases: 
            wp = sp
            cnt = 0
            weak_cnt = 0
            for friend in case: # 시작점에서 친구 한명 출발
                arrived = wp +friend

                for i in new_weak: # 한친구가 커버한 취약점 개수 확인
                    if i >= wp and i <= arrived:
                        weak_cnt +=1
                cnt += 1 # 친구 한명 씀
                if weak_cnt >= wl: # 모든 취약점을 확인한 경우
                    min_cnt = min(min_cnt,cnt) # 최소인원 갱신
                    break
                else: 
                    wp  = close_num(arrived,weak) # 시작점 갱신
                    # if wp == 0:
                    #     break
                    # # print(wp)##
    
    if min_cnt > 8:#== float('inf'): # 모든 친구로도 커버 못했을 시
        answer = -1
    else:
        answer = min_cnt
        
    return answer
#-------------------------------------------------------------

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4])) # 2
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7])) # 1
print(solution(12,[1, 3, 4, 9, 10],[1,3])) # 2 안나옴
print(solution(12,[1, 3, 4, 9, 10],[1,1,1])) # 3
print(solution(12,[1,2,5,6,9,10],[1,1,1])) # 3 안나옴
print(solution(12,[1,2,4,5],[1,1])) # 1 안나옴

print(solution(12,[1,2,3],[5])) # test