N= int(input())
inp_list = []
for _ in range(N):
    inp_list.append(int(input()))

max_cnt = -1
cnt = 0

# basket =list(inp_list[0]) #첫번째 거 담기  에러남. iterable 이거 공유해야함
if N == 1:
    print(1)
else: #N이 2이상
    for idx, elem in enumerate(inp_list):
        #case0. 일단 첫번째꺼는 담아야함
        if idx == 0:
            cnt = 1
        #case1. 직전이랑 같은 부호면 계속 담기(이렇게 마지막에 끝나면? ->for문 밖에 추가해주자)
            #elif가 아니라 if를 했더니, inp_list[idx-1]이 inp_list[-1]이 돼서 1을 한번 추가하고 시작하게 됨!@!
        elif (elem > 0 and inp_list[idx-1] > 0 ) or (elem < 0 and inp_list[idx-1] < 0): #0아니랬음 고려안해도됨
            cnt += 1

        #case2. 직전이랑 다른부호
        elif (elem > 0 and inp_list[idx-1] < 0 ) or (elem < 0 and inp_list[idx-1] > 0): #0아니랬음 고려안해도됨
            #case2-1. max_cnt 갱신
            if cnt > max_cnt: #직전까지 쌓았던 cnt가 더 크면 바꿔줌
                max_cnt = cnt
                cnt = 1 #갱신
            #case2-2. max_cnt 비갱신
            else:
                cnt = 1 #이거만 갱신
        # print(cnt)
    if cnt > max_cnt:
        max_cnt = cnt
    print(max_cnt)