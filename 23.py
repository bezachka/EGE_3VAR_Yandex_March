def first(n):
    n2 = str(n ** 2)
    return int(n2[0])

def caleca(n):
    summ = 0
    for i in str(n):
        summ += int(i)
    
    return summ

def f(curr, end):
    if curr < end:  return 0
    if curr == end: return 1
    if curr > end: return f(curr - first(curr), end) + f(curr - caleca(curr), end)

print(f(32,1))
