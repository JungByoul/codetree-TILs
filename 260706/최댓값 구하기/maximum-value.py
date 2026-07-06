a, b, c = list(map(int, input().split()))

if a>=b:
    if b>=c: 
        print(a) # a b c
    else: # b<c
        if a>= c: # a c b
            print(a)
        else: # a< c
            print(c)  # c a b

elif b>=a:
    if a >= c:  # b a c
        print(b)
    else: # a<c
        if b >= c:
            print(b) # b c a
        else: # b < c
            print(c) # c b a

#  > >
# a b c
# a c b 
# b a c
# b c a
# c a b
# c b a

# 처음에 막  일단 시작하고 봤더니 꼬였음








