
#어려운 문제임. 문제분석부터

# 첫 번째 직사각형이 먼저 놓여 있고, 두 번째 직사각형이 그 다음 놓아졌을 때 
# 그 이후에 남아있는 첫 번째 직사각형의 잔해물
# 을 덮기 위한 최소 직사각형의 넓이를 구하는 
    #'직사각형'임!!! 자유자재로 옮길 수 있는 그런 다각형이 아님. 이게 관건
OFF = 1000 #이거는 그냥 좌표들 양수 맞춰주기
ran = 2000 #최대 넓이
inp_list = []
for _ in range(2):
    a,b,c,d = map(int, input().split())
    a,b,c,d = a+OFF, b+OFF, c+OFF, d+OFF
    inp_list.append([a,b,c,d])
# print(inp_list)
# sq_list = [[0] * ran ] * ran # 여기서 2개 사각형 표시하기. #개낭패봄
sq_list = [[0 for _ in range(ran)] for _ in range(ran)]

# print(sq_list)
    # 0: 아무 사각형도 그려지지 않았음
    # 1: 1번째 사각형만 있는 공간(안겹쳐진 곳)
    # -2: 2번째 사각형만 있는 공간
    # -1: 1~2번째 사각형이 겹쳐진 공간
        # 1만 있는 다각형을, 덮을 수 있는 최소 넓이의 사각형 구하기

for idx, elem in enumerate(inp_list):
    x1, y1, x2, y2 = elem[0], elem[1], elem[2], elem[3] 
    # print(    x1, y1, x2, y2 )
        #지금 계속 매  리스트의 4~8의 인덱스값들이 매우 동일하
    if idx == 0 : #1번째 사각형
        for i in range(x1, x2): #1번째 사각형 채움
            for j in range(y1, y2):
                    sq_list[i][j] += 1
    else: #2번ㅈ째 사각형
        for i in range(x1, x2): 
            for j in range(y1, y2):
                    # print(i, j)
                    sq_list[i][j] -= 2

# print(sq_list)
# 이제 1만 있는 공간을 채울 수 있는
#     최소 넓이의 직사각형 구하자

#     아니뭐야 머리 엄청 싸매다가, 결국 안돼서 토론도 뒤지다가 못했는데
#         기본개념에 있었네, 개쉽네. 좀 쉽게쉽게 생각하자, 너무 경우의수 나눠가면서 하는게 때로는 독이 된다

min_x, min_y, max_x, max_y = 0, 0, 0, 0

#sq_list 싹 돌면서 최솟값 최댓값 저장해야함.
    # and 걸어주고, if에 내부 셀값이 == 1

x_flag = False #가장 처음에 x값 만났을 때 True
y_flag = False #가장 처음에 y값 만났을 때 False

for i in range(0, ran):
    for j in range(0, ran):
        if sq_list[i][j] == 1:
            if not x_flag and not y_flag:
                min_x, min_y = i, j #갱신. 이러고 바꿔주면 안됨
                x_flag, y_flag = True, True #이렇게 무식하게하면 안ㄴ되지, 그럼 무조건 x1,y1이 나옴
            elif x_flag and y_flag: #둘다 참이면
                if max_x < i: #계속 갱신, 이 사각형 끝날 때까지
                    max_x = i
                if max_y < j: #계속 갱신, 이 사각형 끝날 때까지
                    max_y = j

if not x_flag and not y_flag: #그냥 1번째 사각형이 먹혔을 때
    print(0)
else:
# print(min_x, min_y, max_x, max_y)
# print(x_flag, y_flag)
    print((max_x+1 - min_x) * (max_y+1 - min_y))