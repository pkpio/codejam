def popFlipPush(qu, pos):
    qa,qb = [],[]
    try:
        qa = list(qu[:pos])
        qb = list(qu[pos:])
    except TypeError:
        pass

    # Flip qa and symbols
    qa.reverse()
    for i in range(len(qa)):
        qa[i] = '-' if qa[i] == '+' else '+'

    # We need strings!
    qa.extend(qb)
    return ''.join(qa)


############ Main program #############
T = int(input())
for t in range(T):
    S = raw_input()

    # Good string looks like
    G = ''
    NG = ''
    for i in range(len(S)):
        G += '+'
        NG += '-'
    count = 0

    while True:
        if S == G:
            break
        elif S == NG:
            count += 1
            break
        else:
            diff = 0
            for i in range(1,len(S)):
                if S[i] != S[0]:
                    S = popFlipPush(S, i)
                    count += 1
                    break

    print('Case #' + str(t+1) + ': ' + str(count))