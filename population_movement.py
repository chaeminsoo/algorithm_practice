n,l,r = map(int,input().split())

A=[]
for i in range(n):
    row = list(map(int,input().split()))
    A.append(row)

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def check():

