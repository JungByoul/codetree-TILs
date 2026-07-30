
n = int(input())
lines_list = [0] * 1000 # line들 겹치는지 점검하는 거
OFFSET = 100 #x2가 -100까지 있으니까

for _ in range(n):
    a, b = map(int,input().split())
    a, b = a+OFFSET , b+OFFSET
    
    for i in range(a, b):
        lines_list[i] += 1
max_num = 0
for elem in lines_list:
    if elem > max_num:
        max_num = elem

print(max_num)

#음수는 어떻게 구현하지?
#1 입력받기, 2차원배열로.
#2 베이스라인 깔고, 여기서  애들 쌓기
    # 이 때 x_2를 -1 처리. 그래야 안겹치게하는것 구현됨
#3 베이스라인에서 중복 길이가 가장 긴 수를 저장해서 출력
    #max 사용해서 쌓기
    #포인터 사용해서 스타트하다가, 0 만나면 초기화

# import sys

# #1 입력받기, 2차원배열로.
# n = int(input())
# input_list = []
# for _ in range(n):
#     a, b = map(int,input().split())
#     a += 100 #음수처리
#     b += 100 #음수처리
#     input_list.append([a, b])

# #2 베이스라인 깔고, 여기서  애들 쌓기
# base_line = [0] * 300
# for el_list in input_list:
#     a, b = el_list[0], el_list[1]

#     for i in range(a, b): #여기서 b에 -1 작업이 들어갔음
#         base_line[i] += 1
# print(base_line)
# # import sys

# #3 베이스라인에서 중복 길이가 가장 긴 수를 저장해서 출력
#     #max 사용해서 쌓기
#     #포인터 사용해서 스타트하다가, 0 만나면 초기화

# max_num = -sys.maxsize

# cnt = 0
# st_pointer = 0
# co_flag = False

# for i, elem in enumerate(base_line):

#     if elem and not co_flag: #값이 있으면서 첫진행일 때
#         st_pointer = i #i 갱신
#         cnt +=1

# x, y, n = map(int, sys.stdin.readline().split())
# nList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# # print(nList)

# nGraph=[[0 for _ in range(x+1)] for _ in range(y+1)]
# for elem in nList:
#     nGraph[elem[0]][elem[1]] +=1

# print(nGraph)