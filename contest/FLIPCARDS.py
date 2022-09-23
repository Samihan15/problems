t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    total = n-x
    y = min(x, total)
    print(y)
    
