import math

x1,x2 = map(int,input().split())

u1 = [[-0.3,1.0,1.2],[1.6,-1.0,-1.1]]
u2 = [[1.0,1.0,-1.0],[0.7,0.5,1.0]]
u3 = [[0.5,-0.8,0.9],[-0.1,0.3,0.4]]
u4 = [[1.0,0.1,-0.2],[-0.2,1.3,-0.4]]

u = [u1,u2,u3,u4]

def lo_si(z):
    return 1/(1+math.exp(-z))

def relu(x):
    if x<0:
        return 0
    else:
        return x

for i in range(4):
    un = u[i]
    z1 = un[0][0] + un[0][1]*x1 +un[0][2]*x2
    z2 = un[1][0] + un[1][1]*x1 +un[1][2]*x2

    # x1 = lo_si(z1)
    # x2 = lo_si(z2)
    x1 = relu(z1)
    x2 = relu(z2)

print(x1,x2)