t = int(input())
for i in range(t):
    l,k = map(int, input().split())
    if l%k==0:
        print(0)
    else:
        print(1)