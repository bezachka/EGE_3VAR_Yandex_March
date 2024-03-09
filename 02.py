print('x z y w F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((1 == w) == (not((w and x) or y))) <= z

                print(x, z, y, w, f)