#2885
k = int(input())

def find_n(kk):
    a = 0
    while 2**a <kk:
        a+=1
    return 2**a

