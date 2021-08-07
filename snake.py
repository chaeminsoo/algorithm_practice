def eat_apple(location,apples):
    if location[0] in apples:
        apples.remove(location[0])
        return 1
    else:
        return 0
    
def trun(ddd,ooo):
    if ddd == 'u' and ooo == 'L':
        ddd = 'l'
    elif ddd == 'r' and ooo == 'L':
        ddd = 'u'
    elif ddd == 'd' and ooo == 'L':
        ddd = 'r'
    elif ddd == 'l' and ooo == 'L':
        ddd = 'd'
    if ddd == 'u' and ooo == 'D':
        ddd = 'r'
    elif ddd == 'r' and ooo == 'D':
        ddd = 'd'
    elif ddd == 'd' and ooo == 'D':
        ddd = 'l'
    elif ddd == 'l' and ooo == 'D':
        ddd = 'u'
    return ddd

n = int(input())
field = [[0]*n for _ in range(n)]

k = int(input())
apples=[]
for i in range(k):
    row, column = map(int,input().split())
    apples.append((row-1,column-1))

l = int(input())
moves=[]
for i in range(l):
    x, c = input().split()
    moves.append((int(x),c))
moves.sort(reverse=True)

location =[(0,0)]
eaten_apples =1
direction = 'r'
cnt = 0
order = moves.pop()
while location[0][0] >=0 and location[0][0] < n and location[0][1] >=0 and location[0][1] < n:
    
    if cnt == order[0]:
        direction = trun(direction,order[1])
        if moves:
            order = moves.pop()
        
    if direction == 'u':
        cnt+=1
        location.insert(0,(location[0][0]-1,location[0][1]))
        eaten_apples += eat_apple(location,apples)
        
    elif direction == 'r':
        cnt+=1
        location.insert(0,(location[0][0],location[0][1]+1))
        eaten_apples += eat_apple(location,apples)
        
    elif direction == 'd':
        cnt+=1
        location.insert(0,(location[0][0]+1,location[0][1]))
        eaten_apples += eat_apple(location,apples)
        
    elif direction == 'l':
        cnt+=1
        location.insert(0,(location[0][0],location[0][1]-1))
        eaten_apples += eat_apple(location,apples)
        
    #location = location[:eaten_apples]
    
    # if location[0] in apples:
    #     apples.remove(location[0])
    #     eaten_apples+=1

    # if len(location) != eaten_apples:
    

    if location.count(location[0]) != 1:
        break

print(cnt)
print(apples)
print(eaten_apples)
print(location)
print(len(location))
# 2