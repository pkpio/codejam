import math

num = 3 + 5**0.5
T = int(input())
for t in range(T):
    n = int(input())
    res = str(num**n)
    print(res)
    res = res[:res.index('.')]
    if len(res) == 2:
        res = '0'+res
    print('Case #{}: {}'.format(t+1,res[len(res)-3:]))