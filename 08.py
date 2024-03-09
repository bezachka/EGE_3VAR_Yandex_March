from itertools import *

words = permutations('КАБИНЕТ')
alph = 'КБНТ'
count = 0
for w in words:
    word = ''.join(w)
    if word[-1] in alph:
        count += 1

print(count)

