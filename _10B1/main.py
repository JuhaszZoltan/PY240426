from module import *

dijazottak:list[Dijazott] = []
file = open('dijazottak.txt', 'r', encoding='utf-8')
for s in file: dijazottak.append(Dijazott(s))

print(f'3.1: dijazottak szama a fileban: {len(dijazottak)}')

db:int = 0
for d in dijazottak:
    if d.orszag == 'Svédország':
        db += 1
print(f'3.2: sved dijazottak szama: {db}')

ko:str = input('3.3: irja be egy orszag nevet: ')
evek:list[str] = []
for d in dijazottak:
    if d.orszag == ko:
        evek.append(d.ev)
if len(evek) == 0: print('\tnem volt dijazott')
else: print(f'\t ezekben az evekben volt dijazott: {evek}')

maxi:int = 0
for i in range(1, len(dijazottak)):
    if len(dijazottak[i].nev) > len(dijazottak[maxi].nev):
        maxi = i
print('3.4: leghoszabb nevu dijazott:')
print(f'\t{dijazottak[maxi].nev}')