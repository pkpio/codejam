from common import *
import re

W = 'welcome to code jam'

def findcounts(S, cpos):
    count = 0
    for offset in re.finditer(W[cpos],S):
        if cpos < len(W)-1:
            count += findcounts(S[offset.start():], cpos+1)
        else:
            count += 1
    return count

T = readInt()
for t in range(T):
    S = readLineRaw()
    writeLine('Case #{}: {:04}'.format(t+1, findcounts(S,0)))