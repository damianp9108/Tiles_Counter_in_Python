def polePlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi):
    return (dlugoscPlytkiSciennej + szerokoscFugi) * (szerokoscPlytkiSciennej + szerokoscFugi)


def poleWszystkichOtworowSciennych(liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna,
                                   szerokoscOkna):
    return (liczbaDrzwi * wysokoscDrzwi * szerokoscDrzwi) + (liczbaOkien * wysokoscOkna * szerokoscOkna)


def poleScianBezOtworowWzorKlasyczny(w, l, h):
    return 1.05 * (2 * w * h + 2 * l * h)


def poleScianBezOtworowWzorKaro(w, l, h):
    return 1.1 * (2 * w * h + 2 * l * h)


def objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi2, wysokoscFugi):
    return (dlugoscPlytkiSciennej * szerokoscFugi2 * wysokoscFugi) + (
                szerokoscPlytkiSciennej * szerokoscFugi2 * wysokoscFugi)


def wysokoscSciany():

    shouldContinue = True
    while shouldContinue:
        try:
            h = float(input("Prosze podac wysokosc pomieszczenia w metrach: "))
            shouldContinue = False

        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return h

def dlugosc_Plytki_Sciennej():

    shouldContinue = True
    while shouldContinue:
        try:
            dlugoscPlytkiSciennej = float(input("Prosze podac dlugosc plytki sciennej w metrach: "))
            shouldContinue = False

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return dlugoscPlytkiSciennej


def szerokosc_Plytki_Sciennej():

    shouldContinue = True
    while shouldContinue:
        try:
            szerokoscPlytkiSciennej = float(input("Prosze podac szerokosc plytki sciennej w metrach: "))
            shouldContinue = False

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return szerokoscPlytkiSciennej


def liczba_Drzwi():
    shouldContinue = True
    while shouldContinue:
        try:
            liczbaDrzwi = float(input("Prosze podac liczbe otworow drzwiowych: "))
            if liczbaDrzwi.is_integer():
                shouldContinue = False
            else:
                print ("Prosze podac liczbe calkowita")

        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return liczbaDrzwi


def liczba_Okien():
    shouldContinue = True
    while shouldContinue:
        try:
            liczbaOkien = float(input("Prosze podac liczbe otworow okiennych: "))
            if liczbaOkien.is_integer():
                shouldContinue = False
            else:
                print ("Prosze podac liczbe calkowita")

        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return liczbaOkien


def wysokosc_Drzwi():
    shouldContinue = True
    while shouldContinue:
        try:
            wysokoscDrzwi = float(input("Prosze podac wysokosc otworu drzwiowego w metrach: "))
            shouldContinue = False
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return wysokoscDrzwi


def szerokosc_Drzwi():
    shouldContinue = True
    while shouldContinue:
        try:
            szerokoscDrzwi = float(input("Prosze podac szerokosc otworu drzwiowego w metrach: "))
            shouldContinue = False
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return szerokoscDrzwi


def wysokosc_Okna():
    shouldContinue = True
    while shouldContinue:
        try:
            wysokoscOkna = float(input("Prosze podac wysokosc otworu okiennego w metrach: "))
            shouldContinue = False
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return wysokoscOkna


def szerokosc_Okna():
    shouldContinue = True
    while shouldContinue:
        try:
            szerokoscOkna = float(input("Prosze podac szerokosc otworu okiennego w metrach: "))
            shouldContinue = False
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return szerokoscOkna
