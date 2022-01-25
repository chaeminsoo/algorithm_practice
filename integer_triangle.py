n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int,input().split())))

def tir_down(triangle,level,idx):
    if idx == 0:
        return triangle[level][idx] + triangle[level-1][idx]
    elif idx != 0 and idx < level:
        a = triangle[level-1][idx]
        b = triangle[level-1][idx-1]
        return triangle[level][idx] + max(a,b)
    elif idx >= level:
        return triangle[level][idx] + triangle[level-1][idx-1] 

for i in range(1,n):
    for j in range(i+1):
        triangle[i][j] = tir_down(triangle,i,j)

print(max(triangle[n-1]))