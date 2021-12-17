# Pieton
On the run Python translator (EN -> NL). Used by more than 1.000+ Dutch successful businesses.
We believe that programming should be possible for anyone, regardless the human-language.

## Installatie
De programmeer taal Python is vereist om Pieton te gebruiken.

## Gebruik
```code
.\pieton.py <bestand.py> [anderbestand.py] [anderbestand.py] [...]
```

## Voorbeeld
KrachtVanPieton.py
```py

definieer fibonacci(x, y, n):
    x, y = y, x + y
    als n != 0:
        keerterug fibonacci(x, y, n-1)
    keerterug x, y

definieer nice(l, d):
    keerterug [x voor x in l als x == d]

definieer huidig(x):
    voor i in bereik(1, x):
        als i % 3 == 0 en i % 5 == 0:
            schrijf("FizzBuzz")
        andersals i % 3 == 0:
            schrijf("Fizz")
        andersals i % 5 == 0:
            schrijf("Buzz")
        anders:
            schrijf(i)

    schrijf(nice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

    voor x in bereik(1, x):
        schrijf(fibonacci(1, 1, x))

    probeer:
        meld ConnectieFout
    behalve Uitzondering is e:
        schrijf('Een uitzondering heeft plaats gevonden')
    
    schrijf(1/0)

huidig(3)
```

Pieton executeren
```bash
.\pieton.py KrachtVanPieton.py
```

Pieton uitvoer
```bash
1
2
[3]
(2, 3)
(3, 5)
Een uitzondering heeft plaats gevonden
Terugvondst (meest recente roep laatste):
  Bestand "D:\Programmen_en_die_shit\Code\Python\Pieton\pieton.py", lijn 18, in ren_bestand
    executeer(code, globalen())
  Bestand "<snaar>", lijn 33, in <module>
  Bestand "<snaar>", lijn 31, in huidig
NulDeelFout: delen door nul
```

