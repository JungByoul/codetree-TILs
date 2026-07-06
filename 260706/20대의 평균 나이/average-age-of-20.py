#  처음아ㅡ로 20 대
arr =[]
x =0
i = 0
while True:
    x = int(input())
    if x >=30 or x<20:
        break
    arr.append(x)
    i +=1
# print(i, arr)
print(f'{sum(arr[:])/ i:.2f}')
# print(avg(arr[:]))