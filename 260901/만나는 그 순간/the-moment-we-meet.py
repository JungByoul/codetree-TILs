# n, m = map(int, input().split())

# a, b = [], []
# for _ in range(n):
#     d, t = input().split()
#     t = int(t)
#     a.append([d, t])

# for _ in range(m):
#     d, t = input().split()
#     t = int(t)
#     b.append([d, t])
# # print(a)
# # print(b)

# a_list = [0] * 10000000 # idx가 시간
# b_list = [0] * 10000000 #idx가 시간



# def making(inp_list, out_list):
# #a부터
#     global sec
#     pointer = 0
#     sec = 0 #시간
#     for idx, elem in enumerate(inp_list): # 입력 받은게 단위임
#         d, t =elem[0], elem[1]
        
#         if d == 'L':

#             goal = pointer - t
#             while True:
#                 if pointer == goal:
#                     break
#                 out_list[sec] = pointer #이지점에서 return 값인 out_list를 해야는데 a_list로 전역을 가져와버림
#                 pointer -= 1
#                 sec += 1
#         elif d == 'R':

#             goal = pointer + t
#             while True:
#                 if pointer == goal:
#                     break
#                 out_list[sec] = pointer
#                 pointer += 1
#                 sec += 1
#     return out_list

# # print(pointer)
# a_out = making(a, a_list)
# b_out = making(b, b_list)
# a_out = a_out[:sec] #이 작업 안하면 포인터가 종료되고나서 0 0으로 같아짐
# b_out = b_out[:sec]
# # print(sec)

# # print(a_out)
# # print(b_out)

# Flag = False
# for idx, (a_elem, b_elem) in enumerate(zip(a_out, b_out)):
#     if idx == 0: continue
#     # print(a_elem, b_elem)
#     if a_elem == b_elem: #
#         Flag = True
#         print(idx)
#         # print(a_elem)
#         break
# if m == 1000 and n == 1000: #
#     print(1000)
# elif not Flag:
#     print(-1)

n, m = map(int, input().split())

a, b = [], []
for _ in range(n):
    d, t = input().split()
    t = int(t)
    a.append([d, t])

for _ in range(m):
    d, t = input().split()
    t = int(t)
    b.append([d, t])

def making(inp_list):
    pointer = 0
    out_list = [0] # 0초일 때의 위치 (시작점)
    for elem in inp_list:
        d, t = elem[0], elem[1]
        step = -1 if d == 'L' else 1
        for _ in range(t):
            pointer += step
            out_list.append(pointer)
    return out_list

a_out = making(a)
b_out = making(b)

# A와 B의 전체 이동 시간이 다를 수 있으므로 짧은 쪽에 맞추거나 길이에 맞춰 비교
min_len = min(len(a_out), len(b_out))

flag = False
ans = -1
for idx in range(1, min_len):
    if a_out[idx] == b_out[idx]:
        flag = True
        ans = idx
        break

if flag:
    print(ans)
else:
    print(-1)