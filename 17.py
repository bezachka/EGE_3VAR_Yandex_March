f = [int(i) for i in open('17(2).txt')]
mx = 0
ms = -10000
for i in f:
    if i > 99 and i < 1000:
        mx = max(mx, i)
count = 0
for i in range(len(f) - 1):
    c = 0
    summ1 = 0
    summ2 = 0
    sf1 = str(f[i])
    sf2 = str(f[i + 1])
    for n in sf1:
        if n == '-':
            summ1 += 0
        else:
            summ1 += int(n)
    
    if summ1 % 5 == 0:
        c += 1
    
    for n in sf2:
        if n == '-':
            summ2 += 0
        else:
            summ2 += int(n)
    
    if summ2 % 5 == 0:
        c += 1 

    k = abs((f[i] ** 2) - (f[i + 1] ** 2))

    if c == 1 and k >= (mx ** 3):
        count += 1
        ms = max(ms, f[i] + f[i + 1])


    

print(count, ms)