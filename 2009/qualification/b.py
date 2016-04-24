from common import *
import string

def sink(arr,r,c):
    n = arr[r-1][c] if r>0 else 10001
    w = arr[r][c-1] if c>0 else 10001
    e = arr[r][c+1] if c<len(arr[0])-1 else 10001
    s = arr[r+1][c] if r<len(arr)-1 else 10001
    p = arr[r][c]
    mn = min(n,w,e,s,p)
    if p == mn:
        return r,c
    elif n == mn:
        return r-1,c
    elif w == mn:
        return r,c-1
    elif e == mn:
        return r,c+1
    elif s == mn:
        return r+1,c

def newpoint(arr):
    for r in range(R):
        for c in range(C):
            if arr[r][c] is None:
                return r,c
    return -1,-1

def handle_stack(stk, outarr, i, j):
    count = 0
    while len(stk) != 0:
                (x,y) = stk.pop()
                outarr[x][y] = outarr[i][j]
                count += 1
    return count

T = readInt()
for t in range(T):
    R,C = readIntArr()
    inarr,outarr = [],[]
    for Null in range(R):
        inarr.append(readIntArr())
        outarr.append([None]*C)

    i,j = 0,0
    scnt,count = 0,0
    stk = []
    while count < R*C:
        sx,sy = sink(inarr,i,j)
        if sx == i and sy == j:
            if outarr[i][j] is None:
                outarr[i][j] = string.ascii_lowercase[scnt]
                scnt += 1
                count += 1
            count += handle_stack(stk, outarr, i, j)
            i,j = newpoint(outarr)
        elif outarr[sx][sy] is not None:
            outarr[i][j] = outarr[sx][sy]
            count += handle_stack(stk, outarr, i, j)+1
            i,j = newpoint(outarr)
        else:
            stk.append((i,j))
            i,j = sx,sy

    writeLine('Case #{}:'.format(t+1))
    for i in range(R):
        writeLine(' '.join(outarr[i]))
