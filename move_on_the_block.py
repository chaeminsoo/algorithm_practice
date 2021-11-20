from collections import deque

def solution(board):
    answer = 0
    
    shortest_distance = [i[:] for i in board]

    drone = {(0,0),(0,1)}
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def drone_move(drone):
        q = deque()
        q.append(drone)

        

    

    return answer