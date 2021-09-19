from collections import deque
from itertools import permutations

n = int(input())
series = deque(map(int,input().split()))
ops = list(map(int,input().split()))

operators = []
for i in range(len(ops)):
    if i == 0:
        ops.append('+')
    elif i == 1:
        ops.append('-')
    elif i == 2:
        ops.append('*')
    elif i == 3:
        ops.append('/')

all_case = list(permutations(operators,len(operators)))

def calcul(a,b,operators):
    op = operators.popleft()

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a < 0:
            return -((-a)//b)
        else:
            return a // b

for case in all_case:
    a = series[0]
    b = series[1]
    result = calcul(a,b,case[0])
