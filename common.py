#############   CONFIG  ##########
prob = 'C'
small = 0

test = 0
practice = 1
attempt = 0
##################################

src = 'data/'
dst = 'data/'
if test:
    src += 'test.in'
    dst += 'test.out'
else:
    set = 'small' if small else 'large'
    base = '{}-{}'.format(prob, set)
    if practice:
        base += '-practice'
    else:
        if small:
            base += '-attempt' + str(attempt)
    src += base + '.in'
    dst += base + '.out'

IN = open(src, 'r')
OUT = open(dst, 'w')

def readLineRaw():
    return IN.readline().rstrip('\n')

def readLine():
    return IN.readline().strip()

def readInt():
    return int(readLine())

def readIntArr():
    return [int(i) for i in readLine().split(' ')]

def readStringArr():
    return [i for i in readLine().split(' ')]

def write(data):
    OUT.write(data)

def writeLine(data):
    write(data + "\n")

def done():
    IN.close()
    OUT.close()