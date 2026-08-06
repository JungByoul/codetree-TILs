# N = int(input())
# arr = [int(input()) for _ in range(N)]

# # Please write your code here.

N = int(input())
inp_list = []
for _ in range(N):
    inp_list.append(int(input()))

cnt = 0
max_cnt = -1

if N == 1:
    print(1)
else:
    for i, elem in enumerate(inp_list):
        if i == 0:
            cnt = 1
        elif elem > inp_list[i-1]: #이전보다 증가
            cnt += 1
        elif elem <= inp_list[i-1]: #이전보다 감소. 같은 것도 '증가'가 아니니까 상관없겠지?
            if cnt > max_cnt:
                max_cnt = cnt
                cnt = 1 #새로 시작
            else: #cnt M= max_cnt
                cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt #처음부터 계속 전부 연속 수열일 때 max_cnt가 갱신이 안됨
    print(max_cnt)