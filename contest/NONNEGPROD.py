for i in range(int(input())):
    x = int(input())
    arr = list(map(int,input().split()))[:x]
    count = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            count += 1
        elif arr[i] == 0:
            count = 0
            break
    if count % 2 == 0:
        print(0)
    else:
        print(1)
