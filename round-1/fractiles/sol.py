T = int(input())
for t in range(T):
    K,C,S = [int(i) for i in raw_input().split(' ')]
    out = 'Case #{}:'.format(t+1)
    for j in range(S):
        out += ' ' + str(j+1)
    print(out)