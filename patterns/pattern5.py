'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * *
* * *
* *
*
'''
# n = int(input())

# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
#     n = n -1

n = int(input())

for row in range(2*n):
    c = n*2 - row if row>n else row
    for col in range(c):
        print("*",end=" ")
    print()
