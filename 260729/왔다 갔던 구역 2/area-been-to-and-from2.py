n = int(input())

# 음수 좌표를 커버하기 위해 충분히 큰 리스트 생성 (중앙을 100000으로 설정)
offset = 100000
visited = [0] * (offset * 2 + 1)
cur = offset  # 시작 위치 (0에 해당)

for _ in range(n):
    x_str, d = input().split()
    x = int(x_str)
    
    if d == 'R':
        # 오른쪽으로 x만큼 이동하며 각 칸 방문 횟수 증가
        for _ in range(x):
            cur += 1
            visited[cur] += 1
    elif d == 'L':
        # 왼쪽으로 x만큼 이동하며 각 칸 방문 횟수 증가
        for _ in range(x):
            visited[cur] += 1
            cur -= 1

# 2번 이상 지나간 영역(방문 횟수 >= 2)의 크기 계산
ans = 0
for count in visited:
    if count >= 2:
        ans += 1

print(ans)


# # 포기
#     # 아니 포기같은건 없다. 
# n = int(input())
# x = []
# dir = []

# for _ in range(n): 
#     xi, di = input().split()
#     x.append(int(xi))
#     dir.append(di)

# r_list = [0] *  20000
# l_list = [0]   *  20000
# ans_list = [0]  *  20000
# #
# i = 10000

# for idx, (xi, dir) in enumerate(zip(x, dir)):
#     # print(xi,dir)
#     if dir == 'R':
#         r_list[i] += 1
#         goal = i + xi

#         while True:
#             if i+1 >= goal : 
#                 i+=1
#                 break
#             i += 1
#             r_list[i] +=1

#     elif dir == 'L':
#         l_list[i] += 1
#         goal = i - xi

#         while True:
#             if i-1 <= goal: break
#             i -= 1
#             l_list[i] +=1

# # print(r_list)
# # print(l_list)
            
# # ans_list 작업해줘야함
# for idx, (r, l) in enumerate(zip(r_list, l_list)):
#     if r+ l >= 2:
#         ans_list[idx] = True
# print(ans_list.count(True))

# ---28일(화)에 아래방법으로 하다가 포기했음
# n = int(input())
# # x = []
# # dir = []
# x_dir = {}
# for _ in range(n): #오히려 이렇게 담기니까 애매하네 쓰기가. dict으로 바꿈
#     xi, di = input().split()
#     xi = int(xi)
#     x_dir[xi] = di
#     # x.append(int(xi))
#     # dir.append(di)
# # print(x_dir)

# # Please write your code here.
# #  2번 이상 지나간 영역의 크기를 출력
#     #이하 세팅. =디테일
#     #x1-> x2 이동했을 때 x2-1해줘야함
#     #음수는 못하니까 x에 전부 +100을 해줌
#     #-> 빈 0 리스트를 300으로 만들어두자

# z_list = [0] * 50
# # def move(num):
# #     num += 100
# #     return num

# starting = 30   #200에서 시작  
# for key, values in x_dir.items(): #이거 까먹음


#     if values == 'L':
#         goal = starting - key
#         while starting > goal: #starting은 1번의 반복 단위에서 출발점
#             print('Lgoal', goal)
#             z_list[goal] +=1
#             starting -= 1
            
#     else: #values =='R'
#         goal = starting + key

#         while starting <= goal: #starting은 1번의 반복 단위에서 출발점
#             print('Rgoal', goal)
#             z_list[goal] +=1
#             starting += 1

#     print('each_key_starting',starting)
#     # print(z_list)
# print(starting)

# print(z_list)




