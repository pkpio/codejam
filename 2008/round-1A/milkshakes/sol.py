C = int(input())

for c in range(C):
    N = int(input())
    M = int(input())
    prefs = []
    for m in range(M):
        arr = [int(i) for i in raw_input().split(' ')]
        np = arr.pop(0)
        prefs.append([])
        for k in range(0, 2*np, 2):
            prefs[m].append([arr[k], arr[k+1]])
    print(prefs)