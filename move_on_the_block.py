from collections import deque

def solution(board):
    n = len(board)
    answer = 0
    
    shortest_distance = [i[:] for i in board]
    # shortest_distance = [[0]*n for _ in range(n)]

    drone = [{(0,0),(0,1)},0]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def drone_move(drone):
    
        r1,r2 = drone[0][0][0], drone[0][0][1]
        c1,c2 = drone[0][1][0], drone[0][1][1]
        
        for i in range(4):
            nr1 = r1 + dr[i]
            nc1 = c1+ dc[i]
            nr2 = r2 + dr[i]
            nc2 = c2 + dc[i]

            if nr1 >= 0 and nr1 < n and nc1 >= 0 and nc1 <n and nr2 >= 0 and nr2 < n and nc2 >= 0 and nc2 <n:
                if board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                    continue
                else:
                    shortest_distance[nr][nc] = min(shortest_distance[n][c]+1,shortest_distance[nr][nc])
                    shortest_distance[nr][nc] = min(shortest_distance[n][c]+1,shortest_distance[nr][nc])
    
    def drone_turn(drone):
        status = drone[1]

        if status == 0:
            
        elif status == 0:



    

    return answer