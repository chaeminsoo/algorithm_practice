field = [[0]*4 for _ in range(4)]

for i in range(4):
    data  = list(map(int,input().split()))
    for j in range(4):
        field[i][j] = [data[j*2],data[j*2+1]-1]

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,-1,-1,-1,0,1,1,1]

def turn(direction):
    return (direction+1)%8

def find_fish(n):
    for i in range(4):
        for j in range(4):
            if field[i][j][0] == n:
                return (i,j)
    return None

def fish_move(s_r,s_c):
    for i in range(1,17):
        coordinate = find_fish(i)

        if coordinate != None:
            r,c = coordinate[0],coordinate[1]
            d = field[r][c][1]

            for _ in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr >=0 and nr < 4 and nc >= 0 and nc < 4 and not (nr == s_r and nc == s_c):
                    field[r][c][1] = d
                    field[r][c], field[nr][nc] = field[nr][nc], field[r][c]
                    break
                d = turn(d)

def get_fish(s_r,s_c):
    coordinates = []
    direction = 