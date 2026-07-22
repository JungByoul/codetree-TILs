a, b, c, d = tuple(map(int, input().split()))
#a와 c를 분으로 바꿔줌
a, c = a * 60 , c * 60

start_min = a + b
fin_min = c + d

print(fin_min - start_min)



