from collections import deque
from itertools import permutations

n = int(input())
series = deque(map(int,input().split()))
ops = list(map(int,input().split()))
signs = ['+','-','*','/']

operators = []

for i in range(4):
    gen = [signs[i] for _ in range(ops[i])]
    for j in gen:
        operators.append(j)

all_case = list(permutations(operators,len(operators)))

result = 0
def check(series, case):
    global result
    a = series[i]
    b = series[i+1]
    op = case.pop()
    ref = 
    for i in range(len(series)):
    
        if op == '+':
            result += (a + b)
        elif op == '-':
            result += (a - b)
        elif op == '*':
            result += (a * b)
        elif op == '/':
            result += (a // b)