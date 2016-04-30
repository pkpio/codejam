from common import *

nums = {0:'ZERO',
        1:'ONE',
        2:'TWO',
        3:'THREE',
        4:'FOUR',
        5:'FIVE',
        6:'SIX',
        7:'SEVEN',
        8:'EIGHT',
        9:'NINE'}

def delNums(n):
    for c in nums[n]:
        Sar[c] -= 1

def checkNum(n, ch):
    if ch not in Sar:
        return

    while Sar[ch] != 0:
        Fnum.append(n)
        delNums(n)

T = readInt()
for t in range(T):
    S = readLine()
    Sar = dict([])
    for c in S:
        if c in Sar:
            Sar[c] += 1
        else:
            Sar[c] = 1

    Fnum = []
    checkNum(0, 'Z')
    checkNum(2, 'W')
    checkNum(6, 'X')
    checkNum(4, 'U')
    checkNum(1, 'O')
    checkNum(3, 'R')
    checkNum(5, 'F')
    checkNum(7, 'V')
    checkNum(8, 'T')
    checkNum(9, 'N')

    writeLine("Case #{}: {}".format(t+1, ''.join(map(str,sorted(Fnum)))))