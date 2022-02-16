import heapq

fishes = [[0]*4 for _ in range(4)]
direction = [[0]*4 for _ in range(4)]
for i in range(4):
    fish = list(map(int,input().split()))
    for j in range(len(fish)):
        if j%2 == 0:
            fishes[i][j//2] = fish[j]
        else:
            direction[i][j//2] = fish[j]

field = [[0]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        field[i][j] = [fishes[i][j], direction[i][j]]

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,-1,-1,-1,0,1,1,1]

def turn(n):
    a = n+1
    if a < 9: return a
    else: return 1

def fish_move():
    heap = []
    for i in range(4):
        for j in range(4):
            if field[i][j] != 's':
                heapq.heappush(heap, (field[i][j][0],(i,j)))
    
    while heap:
        r,c = heapq.heappop(heap)[1]
        # field[r][c][1] = direction
        ok = True
        while ok:
            if (r+dr[field[r][c][1]-1]) >=0 and (r+dr[field[r][c][1]-1]) < 4 and (c+dc[field[r][c][1]-1]) >= 0 and (c+dc[field[r][c][1]-1]) <4 and field[r+dr[field[r][c][1]-1]][c+dc[field[r][c][1]-1]] != 's':
                ref = field[r+dr[field[r][c][1]-1]][c+dc[field[r][c][1]-1]]
                field[r+dr[field[r][c][1]-1]][c+dc[field[r][c][1]-1]] = field[r][c]
                field[r][c] = ref
                ok = False
            else:
                field[r][c][1] = turn(field[r][c][1])
        break
def shark_move():
    return

field[0][0] = 's'
fish_move()
for i in field:
    print(i)