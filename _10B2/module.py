from random import choice

class Dijazott:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.evszam:int = int(v[0])
        self.nev:str = v[1]
        self.orszag:str = v[2]

def f01() -> None:
    nev:str = input('irja be a nevet: ')
    szul:str = input('irja be a szuletesi evet: ')
    specs:list[str] =  ['#', '&', '@', '!', '%']
    p1:str = nev[:4].capitalize()
    p2:str = szul[2:]
    p3:str = f'{choice(specs)}{choice(specs)}'
    print(f'{p1}{p2}{p3}')

def f02() -> None:
    while True:
        meret:int = int(input('irjon be egy [5; 15] kozotti szamot: '))
        if meret >= 5 and meret <= 15: break
    hely:int = int(input(f'irjon be egy [0; {meret}) kozotti szamot: '))
    if hely < 0 or hely >= meret:
        print('hibás input')
    else:
        abc:str = 'abcdefghijklmnopqrstuvwxyz'
        for index in range(meret):
            if index == hely: print('#', end=' ')
            else: print(abc[index], end=' ')
    tipp:str = input('mi lehet a # helyen?: ')
    if tipp == abc[hely]: print('helyes')
    else: print(f'nem, hanem a {abc[hely]}')