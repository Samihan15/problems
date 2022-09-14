'''
 *********
  *******
   *****
    ***
     *
'''
n = int(input())

k = 2*n

for row in range(n):
    for space in range(row+1):
        print(end=" ")
    while k != row*2+1:
        print("*",end="") 
        k -= 1

    k = 2*n
    print()