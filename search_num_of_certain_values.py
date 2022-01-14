from bisect import bisect_left, bisect_right

n, x = map(int,input().split())

standard = list(map(int,input().split()))

def bi_search(a,x):
    right_value = bisect_right(a,x)
    left_value = bisect_left(a,x)
    if right_value - left_value >0:
        return right_value - left_value
    else:
        return -1

print(bi_search(standard,x))