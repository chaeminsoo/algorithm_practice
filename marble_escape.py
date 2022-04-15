#13469
from collections import deque

n,m = map(int,input().split())
board = []
status_ = [0,0,0]
for i in range(n):
    data = list(input())
    if 'R' in data:
        status_[0] = [i,data.index('R')]
    if 'B' in data:
        status_[1] = [i,data.index('B')]
    board.append(data)

def go():
    return

dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()
q.append(status_)

while True:
    