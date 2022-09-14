'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
n = int(input())

for row in range(n+1):
    for col in range(row):
        print(row,end=" ")
    print()