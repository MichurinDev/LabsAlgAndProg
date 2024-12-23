line1 = input('Введите стоку 1: ')
line2 = input('Введите стоку 2: ')
line = line1 + line2

for s in line:
    if (s in line1 and s not in line2) or (s in line2 and s not in line1):
        print(s, end='')
