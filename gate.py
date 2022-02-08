g = int(input())
p = int(input())
planes = []
for _ in range(p):
    planes.append(int(input()))

gate = [False]*g

def find_gate(num):
    while num >= 0:
        if gate[num] == False:
            break
        num-=1
    return num

for plane in planes:
    ref = find_gate(plane-1)
    if ref < 0:
        break
    gate[ref] = True

print(gate.count(True))