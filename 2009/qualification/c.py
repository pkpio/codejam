from common import *
import re

W = 'welcome to code jam'

def DP(S, cpos):
    if cpos == 0:
        yield len(re.findall(W[cpos], S))
    elif S.endswith(W[cpos]):
        yield DP(S[:-1],cpos-1) + DP(S[:-1], cpos)
    else:
        yield DP(S[:-1],cpos)


T = readInt()
for t in range(T):
    S = readLineRaw()
    writeLine('Case #{}: {:04}'.format(t+1, DP(S,len(W)-1)))