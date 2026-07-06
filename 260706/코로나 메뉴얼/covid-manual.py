# 이럴 때 입력 어떻게? 계속 list(map(int, input().split())) 이거만 외우다시피하니까 뇌가 굳어버림
    # 만약 입력값에 사람 수까지 같이 줬다면? 지금은 3명인데.
l_1 = list(input().split())
a_1, a_2 = l_1[0], int(l_1[1])

l_2 = list(input().split())
b_1, b_2 = l_2[0], int(l_2[1])

l_3 = list(input().split())
c_1, c_2 = l_3[0], int(l_3[1])

# flag_pandemic = 0

def exam(x, y, flag_pandemic): # 사람 1명의 증상과 체온이 들어가는 것임

    if x == 'Y' and y>= 37:
        flag_pandemic +=1
    return flag_pandemic


cnt = exam(a_1, a_2, 0) + exam(b_1, b_2, 0) + exam(c_1, c_2, 0)
# print(cnt)

if cnt >= 2:
    print('E')
else:
    print('N')

# 1 증상유무
# 2 체온 정도


# 감기있다 Y
# 감기없다 N









