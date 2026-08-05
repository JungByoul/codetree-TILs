arr = [
    tuple(map(int, input().split()))
    for _ in range(3)
]
OST = 0 #테스트 후 1000으로 바꿔줘야함
#arr 돌면서 위치 담기

# 1 a_b_list 돌면서 위치한 칸들 +1 해주기

# 2 m_list 돌면서 위치한 칸들 +1 해주기

# 3 zip으로 돌면서 겹치면 a_b_list -1 해주기
    #a, b 는 안겹치니까 -1만 해줘도 됨

# 4 a_b_list 에서 count 로 1 세주면 끝
# ----------------------------------------------------------
#arr 돌면서 위치 담기

# 1 a_b_list 돌면서 위치한 칸들 +1 해주기
a_b_list =[[0 for _ in range(2000)] for _ in range(2000)] #테스트 후 전부 2000으로 바꿔줘야함
# print(a_b_list)
_A =arr[0]
x1, y1, x2, y2 =_A[0]+OST, _A[1]+OST, _A[2]+OST, _A[3]+OST 

# #  뇌 쓰는걸까먹었나? range(x1, y1) range(x2, y2) 계속 ㅣ이러고 있었네
for i in range(x1, x2): 
    for j in range(y1, y2):
        a_b_list[i][j] += 1
        # print(i,j)

_B =arr[1]
x1, y1, x2, y2 =_B[0]+OST, _B[1]+OST, _B[2]+OST, _B[3]+OST 
# print(x1, y1, x2, y2)
for i in range(x1, x2):
    for j in range(y1, y2):
        # print(i,j)
        a_b_list[i][j] += 1

# print(a_b_list)

# 2 m_list 돌면서 위치한 칸들 +1 해주기
m_list =[[0 for _ in range(2000)] for _ in range(2000)] #테스트 후 전부 2000으로 바꿔줘야함
_M =arr[2]
x1, y1, x2, y2 =_M[0]+OST, _M[1]+OST, _M[2]+OST, _M[3]+OST 
for i in range(x1, x2):
    for j in range(y1, y2):
        m_list[i][j] += 1
# print(m_list)
# print(arr[0])

# 3 zip으로 돌면서 겹치면 a_b_list -1 해주기-> 굳이 둘이 같이 돌 필요 없음
    #a, b 는 안겹치니까 -1만 해줘도 됨
for idx_x, x_list in enumerate(m_list): #x_list는 리스트 형태임
    for idx_y, elem in enumerate(x_list): #elem이 해당 좌표에 담긴 값
        if elem and a_b_list[idx_x][idx_y]: #m_list의 요소랑 겹치면
            a_b_list[idx_x][idx_y] = -100 #아예 알아보기 쉽게
# print(a_b_list)

# #이중 for문 접근이 잘 안됨
# for idx_1, (a_b, m_1) in enumerate(zip(a_b_list, m_list)):
#     for idx_2, (a_b_2, m_2) in zip(a_b_list[idx_1], m_list[idx_1]):
#         if m_list[idx_1][idx_2] == True :
#             a_b_list[idx_1][idx_2] -= 1


# # 4 a_b_list 에서 count 로 1 세주면 끝
# print(a_b_list.count) #2차원 배열이라서아래처럼 출력됨
# <bound method list.count of [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, -100, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, -100, -100, 1, 0, 0, 0, 0, 0, 0, 0], [1, -100, -100, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]>

cnt = 0
for x_list in a_b_list:
    for elem in x_list:
        if elem == 1 : #살아남은 값
            cnt+=1
print(cnt)