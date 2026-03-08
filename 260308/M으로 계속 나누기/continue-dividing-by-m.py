N, M = map(int, input().split())

# Please write your code here.
print(N)
while N >0:
    N = N//M
    if not N: break
    print(N)