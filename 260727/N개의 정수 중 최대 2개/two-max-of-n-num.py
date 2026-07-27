# import sys
# print(sys.maxsize)

n = int(input())

a = list(map(int, input().split() ))

# Please write your code here.
x = sorted(a)
print(x[-1], x[-2])