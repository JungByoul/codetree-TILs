m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# 시작일 포함해서 세기

day_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0 
elapsed_days = 1

while True:
    if m1 == m2 and d1 == d2:
        break
    
    elapsed_days += 1
    d1 +=1

    if d1 >= day_max[m1-1]:
        m1 += 1
        d1 = 0

print(elapsed_days)
    

