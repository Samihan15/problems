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

n = int(input())

for i in range(n*2):
    c = 2*n - i if i>n else i
    space = n - c

    for j in range(space):
        print(end=" ")

    for k in range(c):
        print("*",end=" ")
    print()