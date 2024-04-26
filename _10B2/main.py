from module import *

dijazottak:list[Dijazott] = []
file = open('dijazottak.txt', 'r', encoding='utf-8')
for s in file: dijazottak.append(Dijazott(s))

print(f'3.1 fileban szereplo dijazottak szama: {len(dijazottak)}')

sdb:int = 0
for d in dijazottak:
    if d.orszag == 'Svédország':
        sdb += 1
print(f'3.2: sved dijazottak szama: {sdb}')

ko:str = input('3.3 irja be egy orszag nevet: ')
evszamok:list[int] = []
for d in dijazottak:
    if d.orszag == ko:
        evszamok.append(d.evszam)
if len(evszamok) == 0:
    print('\tebbol az orszagbol nem volt dijazott', end='')
else:
    print('\tebbol az orszagbol ekkor nyertek:', end='')
    for e in evszamok:
        print(e, end=' ')

maxi:int = 0
for i in range(1, len(dijazottak)):
    if len(dijazottak[i].nev) > len(dijazottak[maxi].nev):
        maxi = i
print('\n3.4: leghoszabb nevu dijazott:')
print(f'\t{dijazottak[maxi].nev}')