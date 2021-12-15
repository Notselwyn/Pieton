import tokenize
import sys
import traceback
from woordenboeken import pieton_woordenboek, fout_woordenboek


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
