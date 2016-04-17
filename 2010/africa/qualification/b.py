from common import *

T = readInt()
for t in range(T):
    strs = readStringArr()
    strs.reverse()
    out = strs.pop(0)

    for s in strs:
        out += ' ' + s
    writeLine('Case #{}: {}'.format(t+1, out))