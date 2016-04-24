from common import *
import re

L,D,N = readIntArr()
words = []
for Null in range(D):
    words.append(readLine())

for t in range(N):
    pattern = re.compile(readLine().replace('(','[').replace(')',']'))
    count = 0
    for w in words:
        if pattern.match(w):
            count+=1
    writeLine("Case #{}: {}".format(t+1, count))