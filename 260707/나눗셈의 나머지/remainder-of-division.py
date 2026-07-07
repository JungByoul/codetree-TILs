a, b = list(map(int, input().split()))

ans = [0] * b
# print(ans)
# while True:

while True:
# while True:
    if a<=1 :
        break
    elif a < b:
        ans[a % b] += 1
        break
    ans[a % b] += 1
    # if a< b :
    #     break
    a //= b
# print(ans)
ans_sum = 0
for i in range(b):
    ans_sum += ans[i]**2

print(ans_sum)


# 9
# 1000 4..0
# 250 4..2
# 62 4..2
# 15 4..3
# 3 4..3

# 4 4..2
# 1 4..0

# 420 4..0
# 105 4..1
# 26 4..2
# 6 4..2
# 1 4..1