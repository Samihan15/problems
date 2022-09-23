for i in range(int(input())):
    x = int(input())
    y = str(input())[:x]
    z = list(y)
    z.sort()
    z.reverse()
    a = ''


    l = len(z)
    l1 = len(z) -1
    l2 = len(z) -2
    l3 = len(z) -3

    for i in range(len(z)):
        if ('+' and '-') in z:
            if '0' in z :
                if '0' != z[i] and '-' != z[i] and '+' !=z[i]:
                    a = a + str(z[i])
                elif '0' == z[i]:
                    a = a + str(z[len(z)-1])
                    a = a + '-'
                elif '-' == z[i]:
                    continue
                elif '+' == z[i]:
                    a = a + str(z[i])
                    a = a + '0'
            else:
                if i < l3:
                    a = a+str(z[i])
                elif i == l3:
                    a = a + '+' + str(z[l3]) + str(z[l1]) + str(z[l2]) + str(z[l])
        elif '-' in z:
            if (i <= l2):
                a = a+str(z[i])
            else:
                a = a + '-' +str(z[l1])
        elif '+' in z:
            if (i<=l1):
                a = '+' + str(z[l1])
        else:
            a = a + str(z[i])

    print(a)


# z.sort()
# z.reverse()
# print(z)

# 7
# 4-89+20
# ['9', '8', '4', '2', '+']
# 98+4-2