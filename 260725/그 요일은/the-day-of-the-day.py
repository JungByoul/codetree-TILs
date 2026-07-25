m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
A_f = 0 # Mon
if A == 'Tue':
    A_f = 1
elif A == 'Wed':
    A_f = 2
elif A == 'Thu':
    A_f = 3
elif A == 'Fri':
    A_f = 4
elif A == 'Sat':   
    A_f = 5
elif A == 'Sun':
    A_f = 6

#이전 문제랑 다른점은 나머지를 활용해서 요일별 예외처리를 해줘야함
    #m2 d2가 속한 날의 해당 주차가 기준임.
        # 변수1 m2 d2 의 해당 일
        # 변수2 A로 주어진 요일. 
            #경우1:  A < m2 d2  share +1
            #경우2:  A = m2 d2  share +1
            #경우3: m2 d2 < A   share
# 두 날짜의 합산된 수를 빼기.
#     몫만큼 등장한 것임. + 만약 나머지가 0이면 +1

day_max = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cum(pre_month, days_list): # 현재 월이랑 월별 리스트 들어가면, 그 월 전까지 더해줌
    sum = 0
    for i, elem in enumerate(days_list):
        if i == pre_month-1:
            break
        sum += elem

    return sum

sum_1 = cum(m1, day_max) + d1
sum_2 = cum(m2, day_max) + d2
# print(sum_1, sum_2)
share = (sum_2 - sum_1) // 7 #어차피 m2 d2가 m1 d1보다 같거나 앞서게 되어있음
remainder = (sum_2 - sum_1) % 7

if remainder < A_f:
    print(share)
else:
    print(share+1)

# if A == 'Mon':
#     print(share +2) #m2 d2일이 A요일인 경우에는 해당 날짜도 포함시텨야함
# else:
#     print(share + 1)




