# Returns a divisor of a number. If it's a prime, the number will be returned instead
def divisor(n):
    div = n
    for i in xrange(2, 10000): # Relaxing as factor below 10000 instead of long(n**0.5) + 1
        if n % i == 0:
            div = i
            break
    return div

# Tests if a string is jamcoin and returns a dict of 'result' and 'divs' <-- if true
def test_jamcoin(s):
    if s[0] != str(1) or s[len(s)-1] != str(1):
        return {'result':False}

    # Do prime check for each base and add found divisors
    divs = []
    for i in range(2,11):
        num = int(s, i)
        div = divisor(num)
        if div != num:
            divs.append(div)
        else:
            return {'result':False}

    return {'result':True, 'divs':divs}

# Prints a jam coin and its divisors
def print_jc(jc, divs):
    out = jc
    for div in divs:
        out += ' ' + str(div)
    print(out)

# Binary string of given length
def binary(num, length):
    return format(num, '#0{}b'.format(length + 2))

## Main program ###
T = int(input())
N,J = [int(i) for i in raw_input().split(' ')]

for t in range(T):
    jc = ''.join([str(0)]*(N-2))
    count = 0         # no of jam coins found

    print('Case #{}:'.format(t+1))
    while count < J:
        ajc = '1'+jc+'1'    # Actual jam coin
        res = test_jamcoin(ajc)
        if res['result'] == True:
            print_jc(ajc, res['divs'])
            count += 1

        # Increment JC for next iteration
        jc = binary(int(jc,2)+1, N-2)[2:]