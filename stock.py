# 11501
t = int(input())

def buysell(n,data):
    top = 0
    profit = 0
    for i in range(-1,-n-1,-1):
        if data[i] > top:
            top = max(top,data[i])
        else:
            profit += (top-data[i])
    return profit

for _ in range(t):
    days = int(input())
    stocks = list(map(int,input().split()))
    print(buysell(days,stocks))
