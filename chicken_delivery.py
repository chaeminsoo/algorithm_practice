from itertools import combinations

n,m = map(int,input().split())

city=[]
for i in range(n):
    row = list(map(int,input().split()))
    city.append(row)

def distance(home,chick):
    n = abs(home[0]-chick[0])
    m=abs(home[1]-chick[1])
    return n+m
r,c=0,0

houses=[]
chickens=[]
for i in city:
    for j in i:
        if j ==0:
            pass
        elif j == 1:
            houses.append((r,c))
        elif j == 2:
            chickens.append((r,c))
        c+=1
    r+=1
    c=0


def ccd(houses,chickens):
    city_chicken_distance=0
    for house in houses:
        chicken_distance=200
        for chicken in chickens:
            ref_chicken_distance = distance(house,chicken)
            chicken_distance = min(ref_chicken_distance,chicken_distance)
        city_chicken_distance+=chicken_distance
    return city_chicken_distance

if m < len(chickens):
    final_ccd = float('inf')
    new_chicks = combinations(chickens,m)
    for i in new_chicks:
        ref_final_ccd = ccd(houses,i)
        final_ccd = min(ref_final_ccd,final_ccd)
    print(final_ccd)
else:
    print(ccd(houses,chickens))