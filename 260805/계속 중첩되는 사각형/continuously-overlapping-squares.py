#  파란색 영역의 총 넓이를 구하는 프로그램을 작성
OFF = 100 #100으로 바꿔줘야함

N = int(input())
inp_list =[]
# col = 'Red'
for i in range(1, N+1): 
    if i % 2 == 1: #홀수
        col = 'R'
    else: # elif i %2 == 0
        col = 'B'
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+OFF, y1+OFF, x2+OFF, y2+OFF
    inp_list.append([x1, y1, x2, y2, col]) #여기서 col 넣어주기

space = [[0 for _ in range(200)] for _ in range(200)] # 200을 2000으로 바꿔줘야함
#R_space, B_space 따로 만들고
    # [i]][j] = 1 해주고, 
    # R 돌았으면 B를, B 돌았으면 R 을  = 0으로 초기화
R_space = [[0 for _ in range(200)] for _ in range(200)] # 200을 2000으로 바꿔줘야함
B_space = [[0 for _ in range(200)] for _ in range(200)] # 200을 2000으로 바꿔줘야함

for elem in inp_list:
    x1, y1, x2, y2, col = elem[0], elem[1], elem[2], elem[3], elem[4]
    if col == 'R':
        for i in range(x1, x2):
            for j in range(y1, y2):
                R_space[i][j] = 1
                B_space[i][j] = 0
    elif col == 'B':
        for i in range(x1, x2):
            for j in range(y1, y2):
                R_space[i][j] = 0
                B_space[i][j] = 1
# print(R_space)

cnt = 0
# for i_x in range(len(B_space)): #이거 하려했는데 각 B_space의 개별 요소도 필요함
for i_x, x_list in enumerate(B_space):
    for i_y, elem in enumerate(x_list):
        if elem == 1:
            cnt +=1
print(cnt) 
#아래작업 할 필요가 없음. 왜? 이미 위에서 다 처리함
# for i_x, x_list in enumerate(space):
#     for i_y, elem in enumerate(x_list):
#         if R_space[i_x][i_y] == 1:
#             space[i_]
