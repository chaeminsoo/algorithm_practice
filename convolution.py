field = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,0,0,0,0,0,0,0,0,0]
]

ref_field = [i[:] for i in field]

kernel = [
    [-1,-1,-1],
    [0,0,0],
    [1,1,1]
]

# num = [0,2,4,6,8]
len_num = 8#en(num)

result = [[0]*len_num for _ in range(len_num)]



for i in range(len_num):
    for j in range(len_num):

        ref = 0
        for k in range(3):
            for l in range(3):
                
                ref += ref_field[k+i][l+j] * kernel[k][l]

        result[i][j] = ref


# # print(result)
# for i in result:
#     print(i)

for i in range(len(result)):
    for j in range(len(result)):
        result[i][j] += 0.5

# for i in result:
#     print(i)
real_result = []
for i in range(6):
    real_result_row=[]
    for j in range(6):
    
        hab = 0

        for k in range(3):
            for l in range(3):
                hab += result[i+k][j+l]
                # print(hab)
        real_result_row.append((hab/9))
    real_result.append(real_result_row)
        
# print(real_result)
for i in real_result:
    print(i)