'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
n = int(input())

while n:
    for i in range(n):
        print(i+1,end=" ")
    print()
    n = n-1