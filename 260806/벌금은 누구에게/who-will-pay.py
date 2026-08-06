N, M, K = map(int, input().split())

inp_list = []
for _ in range(M):
    inp_list.append(int(input()) - 1)

#idx를 그 학생 고유번호로 생각하자. dict으로도 가능할듯?
check_list = [0] * (N+1)

Flag = True
for i, elem in enumerate(inp_list): #여기서 elem은 학생 번호
    check_list[elem] += 1

    if check_list[elem] >= K:
        print(elem +1)
        Flag = False
        break
if Flag: #안거쳤다면
    print(-1)