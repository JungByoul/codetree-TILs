a, b, c = map(int, input().split())

# Please write your code here.
#  C는 59된 직후 0 초기화
    # B는 23된 직후 0 초기화
    # A는 뭐 없음

s_a, s_b, s_c = 11, 11, 11 #starting point

elapsed_min = 0

if a == 11 and b < 11:
    print(-1)
elif a == 11 and b == 11 and c < 11:
    print(-1)

else:
    while True:

        if s_a == a and  s_b == b and s_c == c:
            break
        
        s_c += 1
        elapsed_min += 1
        if s_c > 59:
            s_b += 1
            s_c = 0
        if s_b > 23:
            s_a += 1
            s_b = 0
    print(elapsed_min)


