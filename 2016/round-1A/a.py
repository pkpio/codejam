L = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

T = int(input())
for t in range(T):
    S = raw_input()
    lword = S[0] + ''
    for c in S[1:]:
        if L.index(lword[0]) <= L.index(c):
            lword = c + lword
        else:
            lword = lword + c
    print('Case #{}: {}'.format(t+1,lword))
