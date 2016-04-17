from common import *

T = readInt()
for t in range(T):
    C = readInt()
    N = readInt()
    P = readIntArr()

    C1 = 0
    C2 = 0
    for i in range(len(P)):
        C1 = i
        try:
            C2 = P.index(C-P[i])
            if C1 != C2:
                break
        except:
            pass

    if C1 > C2:
        C1, C2 = C2, C1
    writeLine("Case #{}: {} {}".format(t+1, C1+1, C2+1))