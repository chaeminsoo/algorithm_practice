from collections import deque

def solution(board):
    n = len(board)
    # answer = 0

    q = deque()    
    shortest_distance = [i[:] for i in board]
    # shortest_distance = [[0]*n for _ in range(n)]

    # drone = {(0,0),(0,1)}
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    visit = []

    def drone_move(drone):
        cnt = drone[1]
        # visit.append(drone[0])

        r1,r2 = drone[0][0][0], drone[0][1][0]
        c1,c2 = drone[0][0][1], drone[0][1][1]
        
        for i in range(4):
            nr1 = r1 + dr[i]
            nc1 = c1+ dc[i]
            nr2 = r2 + dr[i]
            nc2 = c2 + dc[i]

            if nr1 >= 0 and nr1 < n and nc1 >= 0 and nc1 <n and nr2 >= 0 and nr2 < n and nc2 >= 0 and nc2 <n:
                if board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                    continue
                else:
                    if [(nr1,nc1),(nr2,nc2)] in visit:
                        continue
                    else:
                        q.append([[(nr1,nc1),(nr2,nc2)],cnt+1])
    
    def drone_turn(drone):
        cnt = drone[1]

        r1,r2 = drone[0][0][0], drone[0][1][0]
        c1,c2 = drone[0][0][1], drone[0][1][1]
        
        if r1 == r2:
            status = 0 # hor
        elif c1 == c2:
            status = 1 # ver
        
        if status == 0:
            if r1+1<n and r2+1<n and board[r1+1][c1] == 0 and board[r2+1][c2] == 0:
                q.append([[(r1,c1),(r1+1,c1)],cnt+1])                
                q.append([[(r2,c2),(r2+1,c2)],cnt+1])                
            elif r1-1>=0 and r2-1>=0 and board[r1-1][c1] == 0 and board[r2-1][c2] == 0:
                q.append([[(r1,c1),(r1-1,c1)],cnt+1])                
                q.append([[(r2,c2),(r2-1,c2)],cnt+1])                

        elif status == 1:
            if c1+1<n and c2+1<n and board[r1][c1+1] == 0 and board[r2][c2+1] == 0:
                q.append([[(r1,c1),(r1,c1+1)],cnt+1])                
                q.append([[(r2,c2),(r2,c2+1)],cnt+1])                
            elif c1-1>=0 and c2-1>=0 and board[r1][c1-1] == 0 and board[r2][c2-1] == 0:
                q.append([[(r1,c1),(r1,c1-1)],cnt+1])                
                q.append([[(r2,c2),(r2,c2-1)],cnt+1])                
    
    q.append([[(0,0),(0,1)],0])
    while q:
        drone = q.popleft()
        # print(drone)
        # break
        count = drone[1]

        dr1, dr2 = drone[0][0][0], drone[0][1][0]
        dc1, dc2 = drone[0][0][1], drone[0][1][1]

        check = {(dr1,dc1),(dr2,dc2)}
        
        if check in visit:
            continue

        if board[dr1][dc1] == 0:
            board[dr1][dc1] = count
        else:
            board[dr1][dc1] = min(board[dr1][dc1],count)

        if board[dr2][dc2] == 0:
            board[dr2][dc2] = count
        else:
            board[dr2][dc2] = min(board[dr2][dc2],count)
        
        visit.append(check)

        drone_move(drone)
        drone_turn(drone)

    return board[n-1][n-1]

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))