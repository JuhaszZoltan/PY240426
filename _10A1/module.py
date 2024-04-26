from random import choice 

class Dijazott:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.evszam:int = int(v[0])
        self.nev:str = v[1]
        self.orszag:str = v[2]


def f01() -> None:
    nev:str = input('ird be a neved: ')
    ev:str = input('ird be a szuletesi eved: ')
    specs:list[chr] = ['#', '&', '@', '!', '%']

    p1:str = nev[:4]
    p2:str = ev[2:]
    p3:str = f"{choice(specs)}{choice(specs)}"
    jelszo:str = f'{p1.capitalize()}{p2}{p3}'
    print(jelszo)


def f02() -> None:
    meret:int = -1
    while meret < 5 or meret > 15:
        meret:int = int(input('irjon be egy [5; 15] közötti gesz szamot: '))
    hely:int = int(input(f'irjon be egy [0;{meret}) közötti szamot: '))
    if hely < 0 or hely > meret:
        print('hibás input!')
    else:
        abc:str = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(meret):
            if i == hely:
                print('#', end=' ')
            else: print(f'{abc[i]}', end=' ')
    tipp:str = str(input('\nmelyik betu van a # helyen: '))
    if tipp == abc[hely]:
        print('helyes!')
    else: print(f'nem, a megoldas: {abc[hely]}')


