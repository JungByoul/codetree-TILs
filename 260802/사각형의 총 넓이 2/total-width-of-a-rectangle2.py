
OFT = 100
N = int(input())

#싹 다 더하고
#2차원배열 그려서 겹친 구간들은 다 빼주기?
    # 그냥 1이상인 애들의 개수 더하면 되잖아

total_list = [[0 for j in range(200)] for i in range(200)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+OFT, y1+OFT, x2+OFT, y2+OFT
    for i in range(x1, x2):
        for j in range(y1, y2):
            total_list[i][j] +=1

# print(total_list)
cnt = 0
for i in range(200):
    for j in range(200):
        if total_list[i][j] >0:
            cnt+=1
print(cnt)

