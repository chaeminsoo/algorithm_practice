from collections import deque

def solution(board):
    n = len(board)
    answer = 0

    q = deque()    
    shortest_distance = [i[:] for i in board]
    # shortest_distance = [[0]*n for _ in range(n)]

    drone = {(0,0),(0,1)}
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    visit = []

    def drone_move(drone):
        # visit.append(drone[0])

        r1,r2 = drone[0][0], drone[1][0]
        c1,c2 = drone[0][1], drone[1][1]
        
        for i in range(4):
            nr1 = r1 + dr[i]
            nc1 = c1+ dc[i]
            nr2 = r2 + dr[i]
            nc2 = c2 + dc[i]

            if nr1 >= 0 and nr1 < n and nc1 >= 0 and nc1 <n and nr2 >= 0 and nr2 < n and nc2 >= 0 and nc2 <n:
                if board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                    continue
                else:
                    if {(nr1,nc1),(nr2,nc2)} in visit:
                        continue
                    else:
                        q.append({(nr1,nc1),(nr2,nc2)})
    
    def drone_turn(drone):

        r1,r2 = drone[0][0], drone[1][0]
        c1,c2 = drone[0][1], drone[1][1]
        
        if r1 == r2:
            status = 0 # hor
        elif c1 == c2:
            status = 1 # ver
        
        if status == 0:
            if r1+1<n and r2+1<n and board[r1+1][c1] == 0 and board[r2+1][c2] == 0:
                q.append({(r1,c1),(r1+1,c1)})                
                q.append({(r2,c2),(r2+1,c2)})                
            elif r1-1>=0 and r2-1>=0 and board[r1-1][c1] == 0 and board[r2-1][c2] == 0:
                q.append({(r1,c1),(r1-1,c1)})                
                q.append({(r2,c2),(r2-1,c2)})                
        elif status == 1:
            if r1+1<n and r2+1<n and board[r1+1][c1] == 0 and board[r2+1][c2] == 0:
                q.append({(r1,c1),(r1+1,c1)})                
                q.append({(r2,c2),(r2+1,c2)})                
            elif r1-1>=0 and r2-1>=0 and board[r1-1][c1] == 0 and board[r2-1][c2] == 0:
                q.append({(r1,c1),(r1-1,c1)})                
                q.append({(r2,c2),(r2-1,c2)})                


                
        else:
            
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))