n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

color_list =[0] *10000
pointer = 5000

for idx, (nums, dirs) in enumerate(zip(x, dir)):

    if dirs == 'R':
        goal = pointer + nums
        color_list[pointer] = 'R' #검정
        while True:
            if pointer +1 >= goal:
                break
            pointer +=1
            color_list[pointer] = 'R' #검정

    
    elif dirs == 'L':
        goal = pointer - nums
        color_list[pointer] = 'L' #하양
        while True:
            if pointer -1 <= goal: 
                break
            pointer -=1
            color_list[pointer] = 'L' #하양


print(color_list.count('L'), color_list.count('R'))

