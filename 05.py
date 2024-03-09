for n in range(100):
    n2 = bin(n)[2:]

    if n % 2 == 0:
        n0 = n2.count('0')
        n2 = n2 + '0' * n0
    else:
        n1 = n2.count('1')
        n2 = '1' * n1 + n2

    r = int(n2, 2)
    if r > 2000:
        print(n, r)
        break