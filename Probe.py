lenght = int(input('How long lenght: '))
sigh = int(input('How many signs: '))

half_lengs = (lenght - sigh) // 2

print(half_lengs * '~' + sigh * '!' + half_lengs * '~')