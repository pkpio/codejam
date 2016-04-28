from common import *

def reverse(num):
    return int(str(num)[::-1])

T = readInt()
for t in range(T):
    N = readInt()
    count,n = 1,1
    while n != N:
        rev = reverse(n)
        if N-rev < 0:
            n += 1
        elif N-rev < N-n-1:
            n = rev
        else:
            n += 1
        count += 1
    writeLine("Case #{}: {}".format(t+1, count))