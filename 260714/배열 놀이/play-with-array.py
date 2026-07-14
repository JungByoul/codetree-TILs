
# 문제에서 주어지는 입력을 한번에 받지 않고
# 질의마다 입력받고, 출력하는 것을 반복하여도 올바른 출력 결과가 나온다면 맞는 코드입니다.

# NQ 받고. -> Q만큼 반복문 -> 각 q 때마다 입력받고 출력 ->반복

n, q = map(int, input().split())
# print(n, q)
n_list = list(map(int, input().split())) #차피 n개임

for _ in range(q):
    arr = list(map(int, input().split())) #1~2유형은 2개, 3유형은 3개를 받으니까
    if len(arr) == 3: #3유형ㅇㅁ
        n, s, e = arr[0], arr[1], arr[2]
        new_list = n_list[s-1:e]
        for output in new_list:
            print(output, end=' ') #여기서 계속 sep만 주구장창
        print() #이거 안해주니까 3유형 2번연속 나올 때 한줄에 출력됨
    elif len(arr) == 2: #1,2유형
        num, val = arr[0], arr[1]
        if num == 1:
            print(n_list[val-1]) # 1번째 내나 = index =0
        elif num == 2:
            for i, elem in enumerate(n_list):
                if elem == val:
                    print(i+1) #n_list의 원소가 val이랑 같으면 -> i번째 +1
                    break
                if i == len(n_list)-1: #다돌았는데 없으면ㅇㅇ
                    print(0)

        

