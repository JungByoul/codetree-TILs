import sys

n = int(input())
a = list(map(int, input().split()))

# 오 약간 빡센듯?
# Please write your code here.

max_val = sorted(a, reverse= True)[0] #최초 최댓값 출력
# print(max_val)
max_ind = a.index(max_val)
# ind = max_ind #매 최댓값마다 갱신해주는 인덱스 값
ans_list = [max_ind] #정답 출력할 바구니. 나중에 전부 1씩 더해줘야함. 답은 ~번째가 나와야하니까
# print(ans_list)
if max_ind ==0:
    print(1)
else:
    while True: #1 되면 끝

        a = a[:max_ind]
        # print(a)
        max_val = sorted(a, reverse= True)[0] #IndexError: list index out of range
        max_ind = a.index(max_val)

        ans_list.append(max_ind)
        if max_ind <= 0:
            break

    for elem in ans_list:
        elem += 1
        print(elem, end=' ')

