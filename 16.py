f = [0] * 2028
f[2027] = 1
f[2026] = 1
f[2025] = 1
f[2024] = 1
for i in range(2023, 1, -1):
    f[i] = f[i + 2] + f[i + 4]

s = set(f)
print(len(s))