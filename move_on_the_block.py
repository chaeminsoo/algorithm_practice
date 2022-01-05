from collections import deque

def get_next_pos(pos,new_borad):
    next_pos = []
    pos = list(pos)

    pos1_r, pos1_c, pos2_r, pos2_c = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    
    for i in range(4):
        n_pos1_r = pos1_r + dr[i]
        n_pos1_c = pos1_c + dc[i]
        n_pos2_r = pos2_r + dr[i]
        n_pos2_c = pos2_c + dc[i]

        if new_borad[n_pos1_r][n_pos1_c] == 0 and new_borad[n_pos2_r][n_pos2_c] == 0:
            next_pos.append({(n_pos1_r,n_pos1_c),(n_pos2_r,n_pos2_c)})
    
    if pos1_r == pos2_r:
        for i in [-1,1]:
            if new_borad[pos1_r+i][pos1_c] == 0 and new_borad[pos2_r+i][pos2_c] == 0:
                next_pos.append({(pos1_r,pos1_c),(pos1_r+i,pos1_c)})
                next_pos.append({(pos2_r,pos2_c),(pos2_r+i,pos2_c)})
    if pos1_c == pos2_c:
        for i in [-1,1]:
            if new_borad[pos1_r][pos1_c+i] == 0 and new_borad[pos2_r][pos2_c+i] == 0:
                next_pos.append({(pos1_r,pos1_c),(pos1_r,pos1_c+i)})
                next_pos.append({(pos2_r,pos2_c),(pos2_r,pos2_c+i)})
    return next_pos


def solution(borad):
    n = len(borad)

    new_borad = [[1]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            new_borad[i+1][j+1] = borad[i][j]

    q = deque()
    visit =[]
    pos = {(1,1),(1,2)}
    q.append((pos,0))
    visit.append(pos)

    while q:
        pos, cost = q.popleft()

        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos,new_borad):
            if next_pos not in visit:
                q.append((next_pos,cost+1))
                visit.append(next_pos)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))