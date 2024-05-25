def plusMinus(arr):
    # Write your code here
    s=0
    u=0
    m=0
    for i in range(n):
        if (arr[i]>0):
            s=s+1
        elif (arr[i]<0):
            u=u+1
        elif (arr[i]==0):
            m=m+1
    print("{0:.4f}".format((s / n)))
    print("%1.4f "%(u / n))
    print("%1.4f "%(m / n))
    print()
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)