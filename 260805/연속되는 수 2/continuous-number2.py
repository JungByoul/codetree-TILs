N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

max_cnt = -1  #이거에다가 최댓값 갱신
cnt = 0 #해당 값마다 바꿔주기

for i, elem in enumerate(array):
    if i == 0 :
        cnt += 1
        continue #이러면 돌아가자
    # print(max_cnt)
    if array[i] == array[i-1]:
        cnt += 1
        # max_cnt = cnt
    elif array[i] != array[i-1] and cnt > max_cnt:
        max_cnt = cnt
        cnt = 1 #초기화하고 새로 시작
    elif array[i] != array[i-1]: #그냥 단순히 다르기만 하면
        cnt = 1
    else: #처음부터 싹다 같은경우
        print(-1000)

# print(max_cnt)
if N == 1:
    print(1)
elif max_cnt == -1 : #전부 같은 수란 소리
    print(cnt)
else:
    print(max_cnt)







# 풀다가 너무 복잡해짐. 다시시도
# log_ar = [{} for _ in range(20)] #다 담아버려?

# for i, elem in enumerate(array):
#     if i == 0:
#         log_ar[0][elem] = 1 #1개 추가
#     log_ar[i][elem] = 1
#     # if elem in log_ar.keys()


# print(log_ar)
# key_list = [] #동일한 숫자 체크용
# max_cnt = 0 #최댓값 저장
# for idx, dic_elem in enumerate(log_ar):
#     # print(idx, dic_elem)

#     for k, v in dic_elem.items():
#         if not idx : #idx = 0
#             key_list.append(k)
            
#         if k == key_list[-1]: #가장 직전이랑 같다면
#             key_list.append(k)
#             dic_elem[k] += 1
#         elif k != key_list[-1]:
#             key_list = [k] #초기화

        
#         print(k, v)
# print(log_ar)
#     # print(list(elem.keys())) #list로 안감싸주면 dict_keys 라는 형태로 나옴
# #아 갑자기 개귀찮네 그냥 답만 맞으면 되잖아, 뭔 완벽한 풀이야


# # Traceback (most recent call last):
# #   File "/tmp/Main.py", line 15, in <module>
# #     set_ar = set(log_ar) #고유하게 보관
# #              ^^^^^^^^^^^
# # TypeError: unhashable type: 'dict'