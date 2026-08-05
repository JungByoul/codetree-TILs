# 왜 x, y 의 최댓값을 100이 아닌 92로 했을까?

OST = 100 #TEST 후 100으로 바꿔줘야함
space = [[0 for _ in range(200)] for _ in range(200)] # TEST 후 200으로 바꿔줘야함

N = int(input())
inp_list = []
for i in range(N):
    x, y = map(int, input().split())
    inp_list.append([x,y])

# 다 돌면서  +1 해주고, count 1 인곳만.
for elem in inp_list:
    x1, y1 = elem[0], elem[1]
    x2, y2 = x1+8, y1+8 #정사각형인걸 고려해야함/ 한 변 길이는 무조건 8
 
    #이중 포문인데 음... 그냥 해보
    for i_x in range(x1, x2):
        for i_y in range(y1, y2):
            space[i_x][i_y] += 1
# print(space)

#이 작업을 안하면 겹치는건 아예 빼버림
for x_list in space:
    for i, elem in enumerate(x_list):
        if elem >= 2: #겹치는 구간이면
            x_list[i] = 1 #1로 바꿔주기

# print(space.count(1)) #이거 아님!!
cnt = 0
for x_list in space:
    cnt += x_list.count(1) #음 이러면 N^2인데

print(cnt)



# #함수 시도하다가 그냥 반복문 진행. 반복문이라도 제대로 숙지하자..
# def square(x, y):
#     return array #가득 차있는 리스트를 뱉어주기



