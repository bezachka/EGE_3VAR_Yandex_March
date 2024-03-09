from fnmatch import *

pattern = '48*15*0'

for n in range(0, 10 ** 10, 42):
    if fnmatch(str(n), pattern):
        print(n, n//47)