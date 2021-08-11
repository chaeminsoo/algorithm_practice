def solution(n, build_frame):
    answer = []
    top_column=[]
    start_beam=[]
    end_beam=[]
    bottom_column=[]
    
    for commend in build_frame:
        ir = commend[3]
        order = commend[:3]
        if ir == 1:
            if install(order,top_column,end_beam,bottom_column,start_beam):
                answer.append(order)
            else:
                continue
        elif ir == 0:
            
    answer.sort()
    return answer

def install(order,top_column,end_beam,bottom_column,start_beam):
    cb = order[2]
    coordinate = order[:2]
    if cb == 0:
        if coordinate[1] == 0 or coordinate in top_column or coordinate in end_beam or coordinate in start_beam:
            bottom_column.append(coordinate)
            top_column.append([coordinate[0],coordinate[1]+1])
            return True
        else:
            return False
    elif cb == 1:
        if coordinate in top_column or [coordinate[0]+1,coordinate[1]] in top_column:
            start_beam.append(coordinate)
            end_beam.append([coordinate[0]+1,coordinate[1]])
            return True
        elif coordinate in end_beam and [coordinate[0]+1,coordinate] in start_beam:
            start_beam.append(coordinate)
            end_beam.append([coordinate[0]+1,coordinate[1]])
            return True
        else:
            return False

def remove(order,top_column,end_beam,bottom_column,start_beam):
    cb = order[2]
    coordinate = order[:2]
    if cb == 0:
        if [coordinate[0],coordinate[0]+1] in bottom_column and [coordinate[0],coordinate[0]+1] not in end_beam and [coordinate[0],coordinate[0]+1] not in start_beam:
            return False
        elif [coordinate[0],coordinate[0]+1] in start_beam and [coordinate[0]+1,coordinate[1]] not in end_beam and [coordinate[0]+1,coordinate[0]+1] not in top_column:
            return False
        else:
            return True
    elif cb == 1:
        if 