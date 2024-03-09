def f(n):
    ost = ''
    while n != 0:
        ost = str(ost) + str(n % 4)
        n = n // 4

    return ost[::-1]

for n in range(1, 200):
    s = f(n)
    d = s[-3:-1] + s[-1]
    if d == '123':
        print(n)