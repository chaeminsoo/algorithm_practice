# 2212
n = int(input())
k = int(input())
sensor_ = list(map(int,input().split()))
if n <= k:
    print(0)
else:
    sensor_.sort()
    interval_list = []
    for i in range(n-1):
        interval_list.append(sensor_[i+1]-sensor_[i])
    print(interval_list)
    interval_list.sort()
    print(sum(interval_list[:-(k-1)]))