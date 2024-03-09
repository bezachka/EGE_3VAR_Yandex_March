file = open('24.txt')
f = file.read()

alph = ['ABA', 'BAB']
count = 0
ms = 0    
for s in range(3):    
    for i in range(s, len(f) - 2, 3):
        if f[i:i+3] in alph:
            count += 1
            ms = max(ms, count)
        else:
            count = 0

print(ms)