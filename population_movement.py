# def sol(n,L,R,nations):
n,L,R = map(int,input().split())

N = n*n
cnt = 0
nations=[]
for _ in range(n):
    nations.append(list(map(int,input().split())))

visit = [[0]*n for _ in range(n)]

def fast_copy(list):
    return [i[:] for i in list]

standard_v = fast_copy(visit)

def give_not_visit(visit):
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                return [i,j]

stack=[]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def make_un(stack):
    try:
        coordinate = stack.pop()
    except IndexError:
        return 

    union.append(coordinate)
    r,c = coordinate
    visit[r][c] = 1

    standard = nations[r][c]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            ref = nations[nr][nc]
            diff = abs(standard-ref)

            if diff >= L and diff <= R:
                if visit[nr][nc] != 1:
                    stack.append([nr,nc])

    make_un(stack)
    
def move(gou):
    for uns in gou:
        len_uns = len(uns)
        total = 0

        for con in uns:
            total += nations[con[0]][con[1]]

        res = total // len_uns

        for con in uns:
            nations[con[0]][con[1]] = res

while True:
    gou = []

    while True:
        union=[]
        
        coordin = give_not_visit(visit)
        if coordin == None:
            break
        else:
            stack.append(coordin)
            make_un(stack)

            gou.append(union)

    if len(gou) == N:
        break

    move(gou)

    cnt +=1
    visit = fast_copy(standard_v)

print(cnt)
# return cnt
# ******************************************************************
# def a():
#     n = random.randint(1,50)
#     l = random.randint(1,100)
#     r = random.randint(1,100)
#     list = [[] for _ in range(n)]
#     for i in range(n):
#             for j in range(n):
#                     list[i].append(random.randint(0,100))
#     return n,min(l,r),max(l,r),list
# #************************************************************************

# def sol2(n,l,r,graph):
#     # n, l, r = map(int, input().split(' '))
#     # graph = [list(map(int, input().split(' '))) for _ in range(n)]

#     d_x = [-1, 0, 1, 0]
#     d_y = [0, 1, 0, -1]

#     is_move = False


#     def bfs(c_x, c_y, visited, grpah):
#         global is_move
#         people = graph[c_x][c_y]
#         count = 1
#         queue = deque()
#         queue.append((c_x, c_y))
#         visited[c_x][c_y] = True
#         temp = list()
#         temp.append((c_x, c_y))

#         while queue:
#             pop_x, pop_y = queue.popleft()

#             for i in range(4):
#                 n_x = pop_x + d_x[i]
#                 n_y = pop_y + d_y[i]

#                 if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:
#                     continue

#                 if visited[n_x][n_y]:
#                     continue

#                 if l <= abs(grpah[pop_x][pop_y] - grpah[n_x][n_y]) <= r:
#                     visited[n_x][n_y] = True
#                     queue.append((n_x, n_y))
#                     people += graph[n_x][n_y]
#                     count += 1
#                     temp.append((n_x, n_y))

#         move_people = people // count

#         if count > 1:
#             is_move = True
#             for x, y in temp:
#                 graph[x][y] = move_people

#     answer = 0

#     while True:
#         is_move = False
#         visited = [[False] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if not visited[i][j]:
#                     bfs(i, j, visited, graph)

#         if is_move:
#             answer += 1
#         else:
#             break

#     # print(answer)
#     return answer
# #************************************************
# # while True:
# #     n,l,r,lis = a()
# #     v1 = sol(n,l,r,lis)
# #     v2 = sol2(n,l,r,lis)

# #     if v1 != v2:
# #         print(v1,v2,'\n')
# #         print(n,l,r,'\n')
# #         for i in range(len(lis)):
# #             print(lis[i])
# #         print('\n')
# #         print(v1)
# #         break
# #***************************

# print(sol(2,46,73,[[32,32],[32,71]]))
# print(sol2(2,46,73,[[32,32],[32,71]]))