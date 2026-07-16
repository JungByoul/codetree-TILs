a, b = map(int, input().split())

# b는고정.

# a/b
# ->a//b는 그냥 출력붙임
# ->a%b한거에 10곱한것. =x
#     -> x//b를 출력붙임
#     -> x%b한거에 10곱한것. =y
#         -> y//b를 출력붙임..
#         -> y%b한거에 10곱한것....
#             ->.....
#             ->....
#                 총((아이걸 '소수점' 20번째 자리요?))
#                     =>어차피 양수는 최대 2자릿수라. 결과 다 내고 자르면 되지 않나

# 점표시하는걸 못하겠음!!헬
num=0
remainder = a%b # 2 #2
share = a//b # 4 #6
num += share # 4
print(share, end='.')
a = 10*remainder #20

for i in range(20):
    remainder = a%b # 2 #2
    share = a//b # 4 #6
    num += share # 4
    print(share, end='')
    a = 10*remainder #20

# if a % b == 0:  #예제 2의 경우
#     for _ in range()

# x = a/b
# print(f'{x:.20f}')




