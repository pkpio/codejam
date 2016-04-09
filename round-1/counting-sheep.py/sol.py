def checkDigits(num, notseen):
    nstr = str(num)
    for d in nstr:
        try:
            notseen.remove(int(d))
        except ValueError:
            pass


T = int(input())
for t in range(T):
    notseen = [0,1,2,3,4,5,6,7,8,9]
    N = int(input())

    if N == 0:
        print('Case #' + str(t+1) + ': INSOMNIA')
        continue

    i=2
    num = N
    while True:
        checkDigits(num, notseen)
        if len(notseen) == 0:
            break
        else:
            num = N*i
            i += 1

    print('Case #' + str(t+1) + ': ' + str(num))
