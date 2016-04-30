from common import *


def substrNum(S, roff):
    if roff == 0:
        return 0
    else:
        return int(''.join(map(str, S[:roff])))

T = readInt()
for t in range(T):
    CODE, JAM = readStringArr()
    CODE, JAM = list(CODE), list(JAM)

    for i in range(len(CODE)):
        cln = substrNum(CODE, i)
        jln = substrNum(JAM, i)

        if CODE[i] == '?' and JAM[i] != '?':
            if cln < jln:
                CODE[i] = '9'
            elif cln > jln:
                CODE[i] = '0'
            else:
                CODE[i] = JAM[i]
        elif CODE[i] != '?' and JAM[i] == '?':
            if jln < cln:
                JAM[i] = '9'
            elif jln > cln:
                JAM[i] = '0'
            else:
                JAM[i] = CODE[i]
        elif CODE[i] == '?' and JAM[i] == '?':
            if cln == jln:
                CODE[i], JAM[i] = '0', '0'
            elif cln < jln:
                CODE[i], JAM[i] = '9','0'
            else:
                CODE[i], JAM[i] = '0','9'

    writeLine("Case #{}: {} {}".format(t+1, ''.join(map(str,CODE)), ''.join(map(str,JAM))))
