for i in range(int(input())):
    a,b,x = map(int, input().split())
    diff = abs(a-b)
    if ((b-a)%(x*2)==0):
        print('yes')
    else:
        print('no')