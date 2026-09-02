import sys


def solve():
  input = sys.stdin.read
  data = input().split()
  if not data:
    return

  n = int(data[0])
  m = int(data[1])

  idx = 2
  a_moves = []
  for _ in range(n):
    v = int(data[idx])
    t = int(data[idx + 1])
    a_moves.append((v, t))
    idx += 2

  b_moves = []
  for _ in range(m):
    v = int(data[idx])
    t = int(data[idx + 1])
    b_moves.append((v, t))
    idx += 2

  # 각 초별 위치를 기록하는 함수
  def get_positions(moves):
    positions = [0]
    current_pos = 0
    for v, t in moves:
      for _ in range(t):
        current_pos += v
        positions.append(current_pos)
    return positions

  a_pos = get_positions(a_moves)
  b_pos = get_positions(b_moves)

  # 선두 변경 횟수 계산
  lead_changes = 0
  current_leader = None  # None, 'A', 'B'

  for t in range(1, len(a_pos)):
    if a_pos[t] > b_pos[t]:
      new_leader = 'A'
    elif a_pos[t] < b_pos[t]:
      new_leader = 'B'
    else:
      # 동점인 경우 이전 선두가 그대로 유지됨
      continue

    if current_leader is None:
      current_leader = new_leader
    elif current_leader != new_leader:
      lead_changes += 1
      current_leader = new_leader

  print(lead_changes)


if __name__ == '__main__':
  solve()

# n, m = map(int, input().split())

# # Process A's movements
# v = [] #속도
# t = [] #시간
# sum_a = 0
# for _ in range(n):
#     vi, ti = map(int, input().split())
#     v.append(vi)
#     t.append(ti)
#     sum_a += (vi*ti)

# a_list = [0 for _ in range(sum_a+10000)]

# # Process B's movements
# v2 = []
# t2 = []
# sum_b = 0
# for _ in range(m):
#     vi, ti = map(int, input().split())
#     v2.append(vi)
#     t2.append(ti)
#     sum_b += (vi*ti)
# b_list = [0 for _ in range(sum_b)]


# # Please write your code here.


# def making(v_list, t_list): #input은 속도랑 시간.
#     pointer = 0
#     out_list = [0] # 0초일 때의 위치 (시작점)
#     for v, t in zip(v_list, t_list):

#         step = v/t #이렇게 1초에 얼마나 가는지 정해야돼
#         for _ in range(t):
#             # pointer += step
#             out_list.append(step) #와 이렇게 하면 각 초마다 얼마나 움직였는지 보이네
#     return out_list

# a_out = making(v,t)
# b_out = making(v2, t2)

# #여기서 길이 맞추어야될듯?
# a_len, b_len = 0, 0
# for v_a, t_a in zip(v, t):
#     a_len += v_a * t_a
# for v_b, t_b in zip(v2, t2):
#     b_len += v_b * t_b

# # ----------------
# #누적을 시키고
#     #리스트 길이를 맞춰야함
# def cum_list(inp_list):
#     idx = 1
#     while True:
#         if idx >= len(inp_list): break
#         inp_list[idx] += inp_list[idx-1]
#         idx += 1

#     return inp_list
# a_out = cum_list(a_out)
# b_out = cum_list(b_out)
# print(a_out)
# print(b_out)

# # -------------
# #길이 맞추기

# max_len = max(a_len, b_len)

# if a_len > b_len:
#     idx = b_len -1
#     while idx <= max_len:
#         b_out.append(0)
#         idx += 1

# elif a_len < b_len:
#     idx = a_len -1
#     while idx <= max_len:
#         a_out.append(0)
#         idx += 1

# print(a_out)
# print(b_out)


# # A와 B의 전체 이동 시간이 다를 수 있으므로 짧은 쪽에 맞추거나 길이에 맞춰 비교


# cnt = 0
# # ans = 0

# # Fir = ''
# # for idx in range(1, min_len+1):
# #     if Fir == '': #아직 선두가 안정해졌을 때
# #         if a_out[idx] > b_out[idx]:
# #             Fir = 'a'
# #         elif a_out[idx] < b_out[idx]:
# #             Fir = 'b'

# #     #a 가 1초 때 먼저 클 때/ B가 먼저 클 때/ 동일할 때
# #     if Fir == 'b' and a_out[idx] > b_out[idx]: #b가 선두-> a가 추월했을 때
# #         Fir = 'a'
# #         cnt += 1
# #     elif Fir == 'a' and a_out[idx] < b_out[idx]: #a가 선두 -> b가 추월했을 때
# #         Fir = 'b'
# #         cnt += 1
# #     else: #같은 위치일 때
# #         pass
# # print(cnt)


# # --------------------
# #1 공통으로, 인덱스가 시간 초인 리스트. = 각 초마다 A는 어딨는지, B는 어딨는지.
# #2 Flag로 해서, 둘중 하나라도 다른 애보다 커지면? 넘기기?
#     # if a_list[i-1] > b_list[i-1] and a_list[i-1] < b_list[i-1]
#     # elif a_list[i-1] < b_list[i-1] and a_list[i-1] > b_list[i-1]


# # v_idx =0
# # t_idx = 0
# # sec = 1

# # while True:
# #     time_goal = sec + t[t_idx]
# #     while True:
# #         if v_idx ==0 and t_idx ==0:
# #             if sec > time_goal:
# #                 sec -= 1
# #                 break
# #         elif sec >= time_goal:
# #             sec -= 1
# #             break
# #         a_list[sec] = a_list[sec-1] + v[v_idx]/t[t_idx] #현재 초당 속도 더해주기
# #         sec += 1

# #     v_idx += 1
# #     t_idx += 1
# #     sec += 1
# # print(a_list)
