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
        field[i][j] = (fishes[i][j], direction[i][j])

def moving(d,r,c):
    if d == 1:
        if r-1 >= 0 and field[r-1][c] != 's':
            ref = field[r-1][c]
            field[r-1][c] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif d == 2:
        if r-1 >= 0 and c-1 >= 0 and field[r-1][c-1] != 's':
            ref = field[r-1][c-1]
            field[r-1][c-1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif d == 3:
        if c-1 >= 0 and field[r][c-1] != 's':
            ref = field[r][c-1]
            field[r][c-1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif d == 4:
        if r+1 < 4 and c-1 >= 0 and field[r+1][c-1] != 's':
            ref = field[r+1][c-1]
            field[r+1][c-1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif d == 5:
        if r+1 < 4 and field[r+1][c] != 's':
            ref = field[r+1][c]
            field[r+1][c] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif d == 6:
        if r+1 < 4 and c+1 < 4 and field[r+1][c+1] != 's':
            ref = field[r+1][c+1]
            field[r+1][c+1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif d == 7:
        if c+1 < 4 and field[r][c+1] != 's':
            ref = field[r][c+1]
            field[r][c+1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif d == 8:
        if r-1 >=0 and c+1 < 4 and field[r-1][c+1] != 's':
            ref = field[r-1][c+1]
            field[r-1][c+1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)


def fish_move():
    order = []
    for i in range(4):
        for j in range(4):
            heapq.heappush(order,(field[i][j][0],(i,j)))

    while order:
        r,c = heapq.heappop(order)[1]
        d = field[r][c][1]
        moving(d,r,c)
    
s_d = 0    
def shark_move(shark):
    r,c = shark
    if s_d == 1:
        if r-1 >= 0:
            ref = field[r-1][c]
            field[r-1][c] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif s_d == 2:
        if r-1 >= 0 and c-1 >= 0:
            ref = field[r-1][c-1]
            field[r-1][c-1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif s_d == 3:
        if c-1 >= 0:
            ref = field[r][c-1]
            field[r][c-1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif s_d == 4:
        if r+1 < 4 and c-1 >= 0:
            ref = field[r+1][c-1]
            field[r+1][c-1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif s_d == 5:
        if r+1 < 4:
            ref = field[r+1][c]
            field[r+1][c] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif s_d == 6:
        if r+1 < 4 and c+1 < 4:
            ref = field[r+1][c+1]
            field[r+1][c+1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif s_d == 7:
        if c+1 < 4:
            ref = field[r][c+1]
            field[r][c+1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)
    elif s_d == 8:
        if r-1 >=0 and c+1 < 4:
            ref = field[r-1][c+1]
            field[r-1][c+1] = field[r][c]
            field[r][c] = ref
        else:
            d+=1
            if d >8: d = 1
            return moving(d,r,c)