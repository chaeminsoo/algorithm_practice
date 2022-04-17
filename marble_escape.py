#13469
from collections import deque

n,m = map(int,input().split())
board = []
status_ = [0,0,0]
goal = 0
for i in range(n):
    data = list(input())
    if 'R' in data:
        status_[0] = [i,data.index('R')]
    if 'B' in data:
        status_[1] = [i,data.index('B')]
    if 'O' in data:
        goal = [i,data.index('O')]
    board.append(data)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def go(status_,direct):
    now_rb = [0,0]
    for rb in range(2):
        x,y = status_[rb]
        cnt = 0
        while True:
            nx = x + dx[direct]
            ny = y + dy[direct]
            cnt += 1
            if board[nx][ny] == '#':
                now_rb[rb] = [x,y,cnt]
                break
            elif board[nx][ny] == 'O':
                now_rb[rb] = [nx,ny,-1]
                break
            else:
                x,y = nx, ny
                continue
    if now_rb[0][:-1] == now_rb[1][:-1] and now_rb[0][2] != -1:
        if now_rb[0][2] > now_rb[1][2]:
            return [[now_rb[0][0]-dx[direct],now_rb[0][1]-dy[direct]],now_rb[1][:-1],status_[2]+1]
        else:
            return [now_rb[0][:-1],[now_rb[1][0]-dx[direct],now_rb[1][1]-dy[direct]],status_[2]+1]
    else:
        return [now_rb[0][:-1],now_rb[1][:-1],status_[2]+1]

q = deque()
q.append(status_)
ans = 20
while q:
    ref = q.popleft()
    for i in range(4):
        nxt_r, nxt_b, nxt_num = go(ref,i)
        print('#####',nxt_num)
        if nxt_num > 10:
            continue
        if nxt_r == goal and nxt_b != goal:
            ans = min(ans,nxt_num)
            continue
        elif nxt_r == goal and nxt_b == goal:
            continue
        
        q.append([nxt_r,nxt_b,nxt_num])

if ans > 10:
    print(-1)
else:
    print(ans)