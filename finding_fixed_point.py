import re


n = int(input())
series = list(map(int,input().split()))

def bi_search(series,start,end):
    if series[start] == start:
        return start
    elif series[end] == end:
        return end
    elif start == end:
        return -1
        
    mid = (end+start)//2
    if series[mid] > mid:
        return bi_search(series,start,mid-1)
    elif series[mid] < mid:
        return bi_search(series,mid+1,end)
    elif series[mid] == mid:
        return mid

print(bi_search(series,0,n-1))