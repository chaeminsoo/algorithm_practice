from _typeshed import ReadOnlyBuffer
from collections import deque

def solution(board):
    n = len(board)
    answer = 0
    
    # shortest_distance = [i[:] for i in board]
    shortest_distance = [[0]*n for _ in range(n)]
    shortest_distance[0][0] = 1
    shortest_distance[0][1] = 1

    drone = [{(0,0),(0,1)},0]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def drone_move(drone):
        # q = deque()
        # q.append(drone)

        # current = q.popleft()
        # c1,c2 = current
        for coordin in drone[0]:#current:
            r,c = coordin
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr >= 0 and nr < n and nc >= 0 and nc <n:
                    if shortest_distance[nr][nc] == 0:
                        shortest_distance[nr][nc] = shortest_distance[n][c] + 1
                    elif shortest_distance[nr][nc] != 0 and shortest_distance[nr][nc] != 1:
                        shortest_distance[nr][nc] = min(shortest_distance[n][c]+1,shortest_distance[nr][nc])
    
    def drone_turn(drone):
        status = drone[1]

        if status == 0:
            
        elif status == 0:



    

    return answer