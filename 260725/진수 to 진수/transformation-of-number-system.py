a, b = map(int, input().split())
n = input()

#a진수의 수 n을 10진수로 변환
    # 10진수를 다시 B진수로 변환

# 1. n을 10진수로 변환하기
num = 0
n = list(n)

for i in range(len(n)):
    num = num * a + int(n[i])
# print(num)


# 2. 10진수를 다시 B진수로 변환
num_10 =num
b_list =[]
while True:

    if num_10 < b:
        b_list.append(num_10)
        break

    b_list.append(num_10%b)
    num_10 //= b

# print(b_list)
for elem in reversed(b_list):
    print(elem, end='')






# num_10 = 0
# n = list(n)

# for i in range(len(n)):
    
#     num_10 = num_10 * int(n[i])
# print(num_10)

# # print(n)
# last_n = int(n[-1]) #n의 가장 마지막 수는 저장.
# n = n[0:len(n)-1] #n은 그 앞의 수들로 사용.
# print('n=',n)

# for elem in n:
#     elem = int(elem)
#     num_10 += elem*a

# num_10 += last_n
# print('num_10', num_10)



# digits = []
# while True:

#     if n < 2:
#         digits.append(n%2)
#         break
    
#     digits.append(n%2)
#     n //= 2

