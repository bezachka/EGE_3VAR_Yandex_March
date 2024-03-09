def f(s, n, m):
    if (s + n) >= 189:  return m%2 == 0
    if m == 0:  return 0
    h1 = [f(s + n, n, m - 1),f(s, n + s, m - 1), f(s, s, m - 1)]
    h2 = [f(s + n, n, m - 1),f(s, n + s, m - 1), f(n, n, m - 1)]
    if s > n:
        return any(h1) if m%2 != 0 else all(h1)
    if s <= n:
        return any(h2) if m%2 != 0 else all(h2)
    
    
print('19)', [s for s in range(1, 184) if f(5, s, 2)])#all -> any
print('20)', [s for s in range(1, 184) if (not f(5, s, 1)) and f(5, s, 3)])
print('21)', [s for s in range(1, 184) if not f(5, s, 2) and f(5,s,4)])
