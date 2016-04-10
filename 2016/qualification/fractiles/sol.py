# Notation : G = 1,   L = 0

# Binary string of a given number - length of output is always length
def binary(num, length):
    return format(num, '#0{}b'.format(length + 2))[2:]

# Gen all possible original seqs of length K
def gen_org_seqs(K):
    org_seqs = []
    for i in xrange(2**K):
        org_seqs.append(binary(i, K))
    return org_seqs

# Get artwork of given complexity
def get_artwork(C, org_sq):
    if C == 1:
        return org_sq

    # Get artwork of prev complexity
    a_prev = get_artwork(C-1, org_sq)
    a_gold = ''.join([str(1)]*len(org_sq))

    # Build current artwork
    a_cur = ''
    for tile in a_prev:
        if tile == '0':
            a_cur += org_sq
        else:
            a_cur += a_gold

    return a_cur

def print_trivial_case(t, S):
    out = 'Case #{}:'.format(t+1)
    for j in range(S):
        out += ' ' + str(j+1)
    print(out)


T = int(input())
for t in range(T):
    K,C,S = [int(i) for i in raw_input().split(' ')]

    # Trivial cases
    if C == 1 and S < K:
        print('Case #{}: IMPOSSIBLE'.format(t+1))

    elif S >= K:
        print_trivial_case(t,S)

    # Observation
    elif C >= K and K < 8:
        C = K

        # Gen all original seqs
        org_seqs = gen_org_seqs(K)

        # Get the C complex artwork for each orginal seq
        c_seqs = []
        for or_sq in org_seqs:
            c_seqs.append(get_artwork(C,or_sq))

        clen = len(c_seqs[0])
        out = int(''.join([str(1)]*clen), 2)
        for cseq in c_seqs[1:]:
            out = int(out & int(cseq,2))
        print('Case #{}: {}'.format(t+1, binary(out,clen).index('1')))

    else:
        print('Case #{}: {} {}'.format(t+1,2,(K**C)-2))
