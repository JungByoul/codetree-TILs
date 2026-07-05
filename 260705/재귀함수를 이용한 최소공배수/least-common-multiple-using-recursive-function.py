n = int(input())
arr = list(map(int, input().split()))

# 몸통
# 종료조건

def gcd(a,b):
    if not a%b:
        return b
    return gcd(b, a%b)

def lcm(a,b):
    return int((a*b) / gcd(a,b))
# 최대공약수와 최소공배숙 구한건 오케이임. 근데
    #다수의 숫자를 어캐해야할지 모르겠다

# 이 함수가 미쳤음.
def f(arr):
    if len(arr) == 1:
        return arr[0]
    
    return lcm(arr[0], f(arr[1:])) #-> 여기서 리스트의 가장 뒷자리수까지감

print(f(arr))
