T = int(input())
for t in range(T):
    L = int(input())
    V1 = [int(i) for i in raw_input().split(' ')]
    V2 = [int(i) for i in raw_input().split(' ')]

    # Sort them
    V1.sort()
    V2.sort(reverse=True)

    prod = 0
    for i in range(L):
        prod += V1[i]*V2[i]
    print('Case #{}: {}'.format(t+1,prod))