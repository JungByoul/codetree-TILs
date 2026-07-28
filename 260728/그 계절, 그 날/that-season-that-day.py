y, m, d = map(int, input().split())

def leap_flag(month):  #윤년이면 True, 평년이면 False
    if month % 400 == 0:
        return True
    elif month % 100 == 0:
        return False
    elif month % 4 ==0:
        return True
    else:
        return False

if m in [4, 6, 9, 11] and d ==31:
        print(-1)
else:
    #윤년 여부는 2월에서만 중요함. 나머지는 상관없음
    if m == 2: 
        if leap_flag(y):
            if d >=30: #윤년은 29일까지 있음
                print(-1)
            else:
                print('Winter')
        elif not leap_flag(y): #평년임
            if d >=29:
                print(-1)
            else:
                print('Winter')

    elif m in [12, 1]:
        print('Winter')
    elif m in [3,4,5]:
        print('Spring')
    elif m in [6, 7, 8]:
        print('Summer')
    else:
        print('Fall')













# # 25년 10월의 내가 풀었던 풀이..
# Y, M, D = map(int, input().split())


# def check_leap(Y, Leap):
#     if Y % 400 ==0:
#         Leap = True
#     elif Y % 100 ==0:
#         Leap = False
#     elif Y % 4 == 0:
#         Leap = True
#     else:
#         Leap = False
#     return Leap

# def date_return(y, m, d):

#     if M in [2, 4, 6, 9, 11] and D ==31:
#         return -1

#     if M == 2:
#         if D in [30, 31]:
#             return -1
#         elif D == 29:
#             flag = False
#             flag = check_leap(Y, flag)
#             if not flag:
#                 return -1

#     if M in [3, 4, 5]:
#         return 'Spring'
#     elif M in [6, 7, 8]:
#         return 'Summer'
#     elif M in [9, 10, 11]:
#         return 'Fall'
#     else:
#         return 'Winter'

# print(date_return(Y, M, D))

# # 1) 월별로 30 31 여부로 -1 처리
# # 2) 윤년 처리
# # 3) 계절 처리