for i in range(int(input())):
    x = int(input())
    s = str(input())[:x]
    a = '1'
    b = '0'
    y = ''
    if len(s) == 2:
        print(s)
    elif len(s) == s.count('0') or len(s) == s.count('1'):
        print(s)
    else:
        z = list(s)
        z.sort()
        for i in range(len(z)):
            y = y + str(z[i])
        print(y) 


