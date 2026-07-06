a, b = list(map(int, input().split()))
# print(a, b)
prd = 1
for i in range(1, b+1):
    if i % a == 0:
        prd *= i

print(prd)