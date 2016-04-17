from common import *

L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
T = readInt()
for t in range(T):
    S = readLine()
    lword = S[0] + ''
    for c in S[1:]:
        lword = max(lword + c, c + lword)
    write('Case #{}: {}'.format(t+1,lword))
done()