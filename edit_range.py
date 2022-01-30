a = input()
b = input()

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(len(a)-1,-1,-1):
    for j in range(len(b)-1,-1,-1):
        if a[i] == b[j]:
            dp[i][j] = dp[i+1][j+1]+1
        else:
            dp[i][j] = max(dp[i+1][j],dp[i][j+1])

print(max(len(a),len(b))-dp[0][0])