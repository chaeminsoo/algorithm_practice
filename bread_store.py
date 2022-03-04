from collections import deque

x, y = map(int,input().split())
field = []
cnt = 0
for _ in range(x):
  data = input()
  field.append(list(data))
visit = [[False]*y for _ in range(x)]

dr = [-1,0,1]
dc = [1,1,1]
q = deque()
def moving(q):
  global cnt
  r,c = q.popleft()
  visit[r][c] = True
  for i in range(3):
    nr = r + dr[i]
    nc = c + dc[i]
    if nr >= 0 and nr < x and nc >= 0 and nc < y:
      if nc == y-1 and visit[nr][nc] != True:
        visit[nr][nc] = True
        cnt += 1
        return 
      elif field[nr][nc] != 'x' and visit[nr][nc] != True:
        q.append((nr,nc))        
        return moving(q)
  
for i in range(x):
  q.append((i,0))
  moving(q)
print(cnt)
for i in visit:
  print(i)