m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

# m1월 d1일이 월요일.
# 만약 m1월이 ?월이면 그 해당 월의 일수가 뭔지 파악됨 오키.
#     누적된 값을 각자 더한뒤
#         더한 날짜 값들을 둘이 빼줌
#     결과의 절댓값을 7로나눔.
#         나머지만큼 더해주는게 요일임

day_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def cum(pre_month, days_list): # 현재 월이랑 월별 리스트 들어가면, 그 월 전까지 더해줌
    sum = 0
    for i, elem in enumerate(days_list):
        if i == pre_month-1:
            break
        sum += elem

    return sum

#그냥 구현. 절댓값 해주고 서로 빼는거
sum_1 = cum(m1, day_max) + d1
sum_2 = cum(m2, day_max) + d2
# print(sum_1, sum_2)
# print(abs(sum_1 - sum_2) / 4)
flag = sum_1 - sum_2
o = abs(sum_1 - sum_2) % 7

def cal_back(o): #m1 d1이 더 m2 d2보다 작은경우임. 날짜계산이 뒤로감
    if o == 1:
        print('Tue')
    elif o == 2:
        print('Wed')
    elif o == 3:
        print('Thu')
    elif o == 4:
        print('Fri')
    elif o == 5:
        print('Sat')
    elif o == 6:
        print('Sun')
    else:
        print('Mon')

def cal_front(o): #m1 d1이 더 m2 d2보다 큰 경우임. 날짜계산이 앞으로 감
    if o == 1:
        print('Sun')
    elif o == 2:
        print('Sat')
    elif o == 3:
        print('Fri')
    elif o == 4:
        print('Thu')
    elif o == 5:
        print('Wed')
    elif o == 6:
        print('Tue')
    else:
        print('Mon')

if flag > 0: #양수 여부 판별
    cal_front(o)
else:
    cal_back(o)

# 5월 4일.            6월 2일
# 31+28+31+30+4      31+28+31+30+31+2

# -> -29.
# 만약 30이면 월요일?
