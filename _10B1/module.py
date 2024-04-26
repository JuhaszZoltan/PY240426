from random import choice

class Dijazott:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.ev:str = v[0]
        self.nev:str = v[1]
        self.orszag:str = v[2]

def f01() -> None:
    nev:str = input('irja be a nevet: ')
    szul:str = input('irja be a szuletesi evet: ')
    spec:str = '#&@!%'

    p1:str = nev[:4].capitalize()
    p2:str = szul[2:]
    p3:str = f'{choice(spec)}{choice(spec)}'

    print(f'jelszo: {p1}{p2}{p3}')

def f02() -> None:
    meret:int = -1
    while meret < 5 or meret > 15:
        meret = int(input('irjon be egy szamot [5; 15] kozott: '))
    hely = int(input(f'irjon be egy szamot [0; {meret}) kozott: '))
    if hely < 0 or hely >= meret:
        print('hibás input')
    else:
        abc:str = 'abcdefghijklmnopqrstuvwxyz'
        for index in range(meret):
            if hely == index: print('#', end=' ')
            else: print(abc[index], end=' ')
    tipp:str = input('\nmi lehet a # helyen?: ')
    if tipp == abc[hely]: print('így van!')
    else: print(f'nem, hanem a {abc[hely]}')