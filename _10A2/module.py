from random import choice

class Dijazott:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.ev:int = int(v[0])
        self.nev:str = v[1]
        self.orszag:str = v[2]


def f01() -> None:
    nev:str = input('irja be a nevet: ')
    ev:str = input('irja be a suletesi evet: ')
    specs:list[str] = ['#', '&', '@', '!', '%']
    p1:str = nev[:4].capitalize()
    p2:str = ev[2:]
    p3:str = f'{choice(specs)}{choice(specs)}'
    print(f'jelszo: {p1}{p2}{p3}')


def f02() -> None:
    meret:int = 0
    while meret < 5 or meret > 15:
        meret:int = int(input('irjon be egy [5; 15] kozti szamot: '))
    hely:int = int(input(f'irjon be egy [0; {meret}) kozti szamot: '))
    if hely < 0 or hely >= meret:
        print('hibás input')
    else:
        abc:str = 'abcdefghijklmnopqrstuvwxyz'
        for index in range(meret):
            if index == hely: print('#', end= ' ')
            else: print(abc[index], end=' ')
        tipp:str = input('\nmi lehet a # helyen?: ')
        if tipp == abc[hely]: print('helyes')
        else: print(f'nem, a valasz a {abc[hely]}')