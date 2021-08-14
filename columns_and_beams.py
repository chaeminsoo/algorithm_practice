def solution(n, build_frame):
    answer = []
    
    for commend in build_frame:
        ir = commend[3]
        order = commend[:3]
        
        if ir ==1:
            answer.append(order)
            if check(answer):
                continue
            else:
                answer.remove(order)
        elif ir ==0:
            answer.remove(order)
            
            if check(answer):
                continue
            else:
                answer.append(order)
    answer.sort()
    return answer

def check(answer):
    result = True
    for i in answer:
        cb = i[2]
        coordinate = i[:2]
        
        if cb ==0:
            if coordinate[1] == 0:
                continue
            elif [coordinate[0],coordinate[1]-1,0] in answer or [coordinate[0]-1,coordinate[1],1] in answer or [coordinate[0],coordinate[1],1] in answer:
                continue
            else:
                return False
        elif cb==1:
            if [coordinate[0],coordinate[1]-1,0] in answer or [coordinate[0]+1,coordinate[1]-1,0] in answer:
                continue
            if [coordinate[0]-1,coordinate[1],1] in answer and [coordinate[0]+1,coordinate[1],1] in answer:
                continue
            else:
                return False
    return result