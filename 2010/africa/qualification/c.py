from common import *

Alps = 'abcdefghijklmnopqrstuvwxyz '
Nums = ['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999', '0']

T = readInt()
for t in range(T):
    S = readLineRaw()
    out = ''
    for s in S:
        cur = Nums[Alps.index(s)]
        if out.endswith(cur[0]):
            out += ' ' + cur
        else:
            out += cur
    writeLine('Case #{}: {}'.format(t+1, out))