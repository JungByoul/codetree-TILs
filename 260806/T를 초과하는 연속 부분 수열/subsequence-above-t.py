# n = int(input())
# arr = [int(input()) for _ in range(n)]

# # Please write your code here.
N, T = map(int, input().split())
# inp_list = []
# inp_list.append(map(int, input().split())) #이렇게 했다가 안담겨서 낭패봤음
inp_list = list(map(int, input().split()))

cnt = 0
max_cnt = -1

if N == 1 and inp_list[0] > T:
    print(1)
elif N == 1 and inp_list[0] <= T:
    print(0)
else:
    for i, elem in enumerate(inp_list):
        # print(i,elem)
        if i == 0 and elem > T:
            cnt = 1
        elif i == 0 and elem <= T:
            cnt = 0
        elif elem > T:
            cnt += 1
            # print('cnt',cnt, end=' ')
            # print(elem)

        elif elem <= T:
            if cnt > max_cnt:
                max_cnt = cnt
                cnt = 0 #새로 시작
            else: #cnt M= max_cnt
                cnt = 0
    if cnt >= max_cnt:
        max_cnt = cnt #처음부터 계속 전부 연속 수열일 때 max_cnt가 갱신이 안됨
    print(max_cnt)