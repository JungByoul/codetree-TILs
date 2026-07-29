# testcase3 추가함
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)
# print(x)
# print(dir)
# Please write your code here.

#R일 때 b_list 채우기
#L일 때 w_list 채우기
#gray_list는 0으로 세팅

#실시간으로 lat_list 체크하기
    #

#i기준으로 b_list  w_list 각 위치 파악해서
    #각각 2이상이면, 
    #lat_list에 gray 표시

#lat_list 돌면서 흰,검,회 개수 더하기
    #총길이 20, pointer(i) 10으로 계속 테스트함
b_list = [0]*2000000 #최대로 나올 수 있는걸 때려박음. 아님 여기서 2배 더해줘야함. 91808이 나오는 경우도 있음
w_list = [0]*2000000
lat_list = [0]*2000000 #최종 무슨 색인지
i = 1000000 #pointer

for nums, dirs in zip(x, dir): #같이 돌기

    if dirs == 'R':
        b_list[i] += 1
        lat_list[i] = 'B'
        goal = i+nums

        while True:
            if i+1 >= goal: #같아지는 순간 안더함. nums가 1이면 본인만 더하고 끝
                break
            #<= 당연한걸 써놨네 븅신인가
            #어차피 R은 우측으로 가니까
            i += 1 #1인 경우에는 칸이 이동하지 않는데 포인터가 이동하니까 문제가 생김
            b_list[i] += 1
            lat_list[i] = 'B'
            # print(lat_list)

    elif dirs == 'L':
        w_list[i] += 1
        lat_list[i] = 'W'
        goal = i-nums
        while True:
            if goal >= i-1 : # 이작업이진짜개빡치네
                break
            i -= 1
            w_list[i] += 1
            lat_list[i] = 'W'

# print(b_list, w_list, lat_list, sep='\n')

for idx, (b, w) in enumerate(zip(b_list, w_list)):
    
    if b>=2 and w>=2: #각 2번씩지나쳤으면
        lat_list[idx] = 'G'

# print(lat_list)
print(lat_list.count('W'), lat_list.count('B'), lat_list.count('G'))
