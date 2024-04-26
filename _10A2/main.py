from module import *

dijazottak:list[Dijazott] = []

file = open('dijazottak.txt', 'r', encoding='utf-8')
for sor in file: dijazottak.append(Dijazott(sor))

print(f'3.1: dijazottak szama: {len(dijazottak)}')

sdb:int = 0
for d in dijazottak:
    if d.orszag == 'Svédország':
        sdb += 1
print(f'3.2: sved dijazottak szama: {sdb}')

kor:str = input('3.3: irja be egy orszag nevet: ')
evek:list[int] = []
for d in dijazottak:
    if d.orszag == kor:
        evek.append(d.ev)
if (len(evek) == 0):
    print('\tnincs ilyen dijazott!')
else:
    print('\ta kovetkezo evekben volt dijazott innen:', end='\n\t')
    for e in evek:
        print(f'{e}', end=' ')

maxi:int = 0
for i in range(1,  len(dijazottak)):
    if len(dijazottak[i].nev) > len(dijazottak[maxi].nev):
        maxi = i
print('3.4: leghoszabb nevu irodalmi nobeldijas:')
print(f'\t{dijazottak[maxi].nev}')