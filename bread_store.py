from collections import deque

r,c = map(int,input().split())
field = []
for _ in range(r):
    data = list(input())
    field.append(data)
visit = [[False]*c for _ in range(r)]

# for i in range(r):
#     visit[i][0] = i

dr = [-1,0,1]
dc = [1,1,1]

def moving(x,y):
    q = deque()
    q.append((x,y))
    visit[x][y] = True
    while q:
        ref_r, ref_c = q.popleft()
        for i in range(3):
            nr = ref_r + dr[i]
            nc = ref_c + dc[i]

            if nr >= 0 and nr < r and nc >= 0 and nc < c:
                if field[nr][nc] != 'x' and visit[nr][nc] != True:
                    visit[nr][nc] = True
                    q.append((nr,nc))

            # visit[ref_r][ref_c] = False

moving(2,0)

for i in visit:
    print(i)
# ------------------------------------
# def moving(x,y,n):
#     for i in range(3):
#         nr = x + dr[i]
#         nc = y + dc[i]

#         if nr >= 0 and nr < r and nc >= 0 and nc < c:
#             if field[nr][nc] != 'x' and type(visit[nr][nc]) != int:
#                 visit[nr][nc] = n
#                 break

# for i in range(c-1):
#     for j in range(r):
#         target = visit[j][i]
#         if type(target) == int:
#             moving(j,i,target)
# # cnt = 0
# # for i in range(r):
# #     if visit[i][c-1] == True:
# #         cnt +=1

# for i in visit:
#     print(i)