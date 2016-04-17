from common import *

#setInOut('B-small-practice.in','B-small-practice.out')
setInOut('B-large-practice.in','B-large-practice.out')

T = readInt()
for t in range(T):
    hts = [0]*2501

    N = readInt()
    inlist = []
    for n in range(2*N-1):
        inlist.append(readIntArr())

    for list in inlist:
        for num in list:
            hts[num] ^= 1

    write('Case #{}:'.format(t+1))
    for i in range(len(hts)):
        if hts[i]:
            write(' ' + str(i))
    writeLine('')
done()