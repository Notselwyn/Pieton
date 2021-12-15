import tokenize
import sys
import traceback

omgekeerd_woordenboek = lambda x: {v: k for k, v in x.items()}

error_woordenboek = {
    'BeweringFout': 'AssertionError',
    'AttribuutFout': 'AttributeError',
    'EOFFout': 'EOFError',
    'DrijvendeKommaFout': 'FloatingPointError',
    'GeneratorAfsluiten': 'GeneratorExit',
    'ImporteerFout': 'ImportError',
    'ModuleNietGevondenFout': 'ModuleNotFoundError',
    'IndexFout': 'IndexError',
    'SleutelFout': 'KeyError',
    'ToetsenbordOnderbreking': 'KeyboardInterrupt',
    'GeheugenFout': 'MemoryError',
    'NaamFout': 'NameError',
    'NietGeïmplementeerdeFout': 'NotImplementedError',
    'BSFout': 'OSError',
    'OverloopFout': 'OverflowError',
    'RecursieFout': 'RecursionError',
    'ReferentieFout': 'ReferenceError',
    'LooptijdFout': 'RuntimeError',
    'StopIteratie': 'StopIteration',
    'StopAsyncIteratie': 'StopAsyncIteration',
    'SyntaxFout': 'SyntaxError',
    'IndentatieFout': 'IndentationError',
    'TabFout': 'TabError',
    'SysteemFout': 'SystemError',
    'SysteemUitgang': 'SystemExit',
    'TypeFout': 'TypeError',
    'OngebondenLokaleFout': 'UnboundLocalError',
    'UnicodeFout': 'UnicodeError',
    'UnicodeEncodeerFout': 'UnicodeEncodeError',
    'UnicodeDecodeerFout': 'UnicodeDecodeError',
    'WaardeFout': 'ValueError',
    'NulDeelFout': 'ZeroDivisionError',
    'OmgevingFout': 'EnvironmentError',
    'IUFout': 'IOError',
    'RamenFout': 'WindowsError',
}

datatype_woordenboek = {
    # datatypes
    'snaar': 'str',
    'getal': 'int',
    'lijst': 'list',
    'tupel': 'tuple',
    'woordenboek': 'dict',
    'verzameling': 'set',
    'booleaan': 'bool',
    'drijvend': 'float',
}

pieton_woordenboek = {
    # function definitions
    'definieer': 'def',
    'keerterug': 'return',

    # loops
    'terwijl': 'while',
    'voor': 'for',
    'geef': 'yield',

    # errors
    'probeer': 'try',
    'behalve': 'except',
    'meld': 'raise',

    # if statements
    'als': 'if',
    'andersals': 'elif',
    'anders': 'else',

    # logic
    'en': 'and',
    'of': 'or',
    'niet': 'not',

    # naturals
    'Waar': 'True',
    'Nietwaar': 'False',
    'geen': 'None',
    'Uitzondering': 'Exception',

    # functions
    'bereik': 'range',
    'lees': 'input',
    'schrijf': 'print',
    'som': 'sum',
    'minimaal': 'min',
    'maximum': 'max',
    'aantal': 'len',
    'karakter': 'chr',
    'karaktergetal': 'ord',
    'absoluut': 'abs',
    'kaart': 'map',
    'uitgang': 'exit',
    'globalen': 'globals',
    'executeer': 'exec'
}

fout_woordenboek = {
    'name': 'naam',
    'not': 'niet',
    'most': 'meest',
    'recent': 'recente',
    'call': 'roep',
    'last': 'laatste',
    'defined': 'gedefinieerd',
    'File': 'Bestand',
    'Traceback': 'Terugvondst',
    'line': 'lijn',
    'string': 'snaar',
    'globals': 'globalen',
    'exec': 'executeer',
}

pieton_woordenboek.update(error_woordenboek)
pieton_woordenboek.update(datatype_woordenboek)

fout_woordenboek.update(omgekeerd_woordenboek(error_woordenboek))
fout_woordenboek.update(omgekeerd_woordenboek(datatype_woordenboek))


def ren_bestand(bestand_naam):
    with open(bestand_naam, "rb") as f:
        tokens = []
        for token in tokenize.tokenize(f.readline):
            if token.type == 1 and token.string in pieton_woordenboek:
                tokens.append((token.type, pieton_woordenboek[token.string]))
            else:
                tokens.append((token.type, token.string))
        code = tokenize.untokenize(tokens).decode('utf-8')

        try:
            exec(code, globals())
        except Exception as e:
            terugvondst = traceback.format_exc()

            for term in fout_woordenboek:
                terugvondst = terugvondst.replace(term, fout_woordenboek[term])
            print(terugvondst)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ren_bestand(sys.argv[1])
    elif len(sys.argv) > 2:
        for bestand in sys.argv[1:]:
            ren_bestand(bestand)
    else:
        print("Geen bestanden opgegeven")
