def polePlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi):
        return (dlugoscPlytkiSciennej + szerokoscFugi)*(szerokoscPlytkiSciennej + szerokoscFugi)

def poleWszystkichOtworowSciennych(liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna):
        return (liczbaDrzwi * wysokoscDrzwi * szerokoscDrzwi) + (liczbaOkien * wysokoscOkna * szerokoscOkna)

def poleScianBezOtworowWzorKlasyczny(w, l, h):
        return 1.05 * (2*w*h + 2*l*h)

def poleScianBezOtworowWzorKaro(w, l, h):
        return 1.1 * (2*w*h + 2*l*h)

def objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi):
        return (dlugoscPlytkiSciennej*szerokoscFugi*wysokoscFugi) + (szerokoscPlytkiSciennej*szerokoscFugi*wysokoscFugi)


dlugoscPlytkiSciennej = 0.5
szerokoscPlytkiSciennej = 0.35