from module import *

dijazottak:list[Dijazott] = []

file = open('dijazottak.txt', 'r', encoding='utf-8')
for sor in file:
    dijazottak.append(Dijazott(sor))

print(f'3.1: dijazottak szama: {len(dijazottak)}')

sveddb:int = 0
for d in dijazottak:
    if d.orszag == 'Svédország':
        sveddb += 1
print(f'3.2: sved dijazottak szama: {sveddb}')


kerorszag:str = input('3.3: adja meg egy orszag nevet: ')
evszamok:list[int] = []
for d in dijazottak:
    if d.orszag == kerorszag:
        evszamok.append(d.evszam)

if len(evszamok) == 0:
    print('\tnem volt ebbol az orszagbol dijazott')
else:
    print(f'\tezekben az evekben nyert {kerorszag} szarmazasu:', end='\n\t')
    for e in evszamok:
        print(f'{e}', end=' ')

maxi:int = 0
for i in range(1, len(dijazottak)):
    if len(dijazottak[i].nev) > len(dijazottak[maxi].nev):
        maxi = i
print('3.4: leghoszabb nevu dijazott neve:')
print(f'\t{dijazottak[maxi].nev}')