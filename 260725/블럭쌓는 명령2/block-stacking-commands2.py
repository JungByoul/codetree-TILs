#1. 2차원 배열에 입력담기

#2. 2차원 배열 돌면서 블럭들 리스트에 블럭 쌓기

#3. 쌓인 블럭 리스트 돌기. 이 때 sys 사용해서 최댓값 저장 후 출력

import sys


n, k = map(int,input().split())
input_list=[]

#1. 2차원 배열에 입력담기
for _ in range(k):
    a, b = map(int,input().split())
    input_list.append([a, b])
# print(input_list) # good 잘담김

#2. 2차원 배열 돌면서 블럭들 리스트에 블럭 쌓기
block_list = [0] * (n+1)

for elem in input_list:
    a,b = elem[0], elem[1] #지시받은 입력값 언패킹

    for i in range(a, b+1): #이중 for문 쓰는게 걸리긴하네..
        block_list[i] += 1

# print(block_list)
max_val = -sys.maxsize
# print(max_val)
for elem in block_list:

    if elem > max_val:
        max_val = elem

print(max_val)






# import sys, math

# T = int(input())
# nInputs = list(map(int, sys.stdin.readlines()))
# # print(max(nInputs))
# nRange = max(nInputs)

# nDecimals =[0] * (nRange+1)
# nDecimals[0], nDecimals[1] = 1, 1 #0과 1도 소수 아니니까 합성수 처리
# # Flag=False

# for i in range(2, int(round(math.sqrt(nRange), 0))+1):
#     if not nDecimals[i]:
#         for j in range(i*2, nRange+1, i):
#             nDecimals[j] +=1
# sosu =[]
# for i in range(nRange+1):
#     if not nDecimals[i]:
#         sosu.append(i)

# # print(nDecimals)

# for elem in nInputs:
#     cnt = 0
#     nList=[]
#     for i in range(len(sosu)):

#         for j in range(i, len(sosu)):
#             if sosu[i] + sosu[j] == elem:
#                 cnt+=1
#     print(cnt)

# # for _ in range(T):
# #     N = int(sys.stdin.readline())
# #     cnt =0
# #     nList=[] #3+5, 5+3 같은 중복 방지
# #     for i in range(2, N):
# #         if not nDecimals[i] and not nDecimals[N-i]:
# #             nCandis = sorted([i,N-i])
# #             if nCandis not in nList:
# #                 nList.append(nCandis)
# #                 cnt+=1
# #     # print(nList)
# #     print(cnt)