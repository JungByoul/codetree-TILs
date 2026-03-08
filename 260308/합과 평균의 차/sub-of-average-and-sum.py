a,b,c = map(int, input().split())
sum = a+b+c
avg = int(sum/3)
# avg = sum//3

print( sum, avg, sum-avg, sep='\n')