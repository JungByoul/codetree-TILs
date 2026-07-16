
# 1 입력값들 리스트로 싹 받고
# 2 일단 not in으로 B가 A에 아예 없는 경우 만들고.
# 3 pointer 사용해야할듯?
    # A 포인터
    #B  포인터
        #만약 동일한게 걸리면
        #while  b 전부 다 돌 때까지. = B 다 돌았다는건 연속부분수열임
            #만약 b 남았는데, A 포인터 끝났으면 False
#3 if/ else 문으로 Yes/No 출력

#1
n_1, n_2 = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

if n_2> n_1:
    print('No')
else:
# print(n_1, n_2)
# print(a_list)
# print(b_list)

# 2 
# while 문에 포함해도 될듯

#3 
    a_pointer = 0
    b_pointer = 0
    starting_flag = False #B list 기준, A랑 겹치는 지점의 인덱스?

    while a_pointer < len(a_list) and b_pointer < len(b_list): #pointer는 인덱스 len은 길이.
        if starting_flag == False and b_list[b_pointer] != a_list[a_pointer]:    
            a_pointer +=1 #종료조건까지 계속진행
        elif starting_flag == True and b_list[b_pointer] != a_list[a_pointer]: # 이게 바로 예제 1의 경우
            # break #이렇게 하면 test case 3 못해결함. 뒤에 또 나올 수도 있다
            starting_flag = False #초기화
            b_pointer = 0 #초기화
            
        elif starting_flag == False and b_list[b_pointer] == a_list[a_pointer]: #가장 처음으로 일치
            starting_flag = True
            b_pointer +=1 # 포인터 이동
            a_pointer +=1
        elif starting_flag == True and b_list[b_pointer] == a_list[a_pointer]: #이전에도 일치했다면
            b_pointer +=1
            a_pointer +=1
        else:
            a_pointer +=1

    if b_pointer == len(b_list) and starting_flag == True:
        print('Yes')
    else:
        print('No')


