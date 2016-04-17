IN = open('data.in', 'r')
OUT = open('data.out', 'w')

def setInOut(src, dst):
    global IN
    global OUT
    IN = open(src, 'r')
    OUT = open(dst, 'w')

def readLine():
    return IN.readline()

def readInt():
    return int(readLine())

def readIntArr():
    return [int(i) for i in readLine().split(' ')]

def readCharArr():
    return [i for i in readLine().split(' ')]

def write(data):
    OUT.write(data)

def writeLine(data):
    write(data + "\n")

def done():
    IN.close()
    OUT.close()