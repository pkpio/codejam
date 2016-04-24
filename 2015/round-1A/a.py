from common import *

T = readInt()
for t in range(T):
    _,obs = readInt(),readIntArr()
    c1, c2, rate = 0,0,0

    for i in range(len(obs)-1):
        rate = max(rate, obs[i]-obs[i+1])
        if obs[i]-obs[i+1] > 0:
           c1 += obs[i]-obs[i+1]

    for i in range(len(obs)-1):
        c2 += min(rate, obs[i])

    writeLine("Case #{}: {} {}".format(t+1, c1, c2))