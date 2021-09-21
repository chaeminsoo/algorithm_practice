from collections import deque
from itertools import product

n = int(input())
series = deque(map(int,input().split()))
ops = list(map(int,input().split()))

def calcul(series, ops):
    result = 0
    