
ingred = list(input().split())
s = ingred[0]
q = int(ingred[1])

def judge(num, array):
    if  num == '1':
        print(array[1:]+array[0])
        array = array[1:]+array[0]
        return array
    elif num == '2':
        print(array[-1]+array[:-1])
        array = array[-1]+array[:-1]
        return array
    else: #num =='3
        n_array = ''
        for elem in reversed(array):
            # print(elem, end='')  #여기서 이걸 해버리며 end 때문에 여러 경우에서 꼬임
            n_array += elem
        print(n_array)
        return n_array

        # print([elem for elem in reversed(array)]) #오 지린다
        # array = sorted(array)#여기서 이걸 쓰는게 시간복잡도 상에서는 바람직하지는 않음


for i in range(q):
    nums = input()
    s = judge(nums, s)

