rols = [42, 41, 40, 39]
foots = [42, 42, 41, 41]

count = 0

rols.sort(reverse=True)
foots.sort(reverse=True)

for i_foot in foots:
    for i_rol in rols:
        if i_foot <= i_rol:
            rols.remove(i_rol)
            count += 1

print(count)