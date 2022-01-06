def polePodlogiWzorKlasyczny(l, w):
    return 1.05 * l * w


def polePodlogiWzorKaro(l, w):
    return 1.1 * l * w


def polePlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi):
    return (dlugoscPlytkiPodlogowej + szerokoscFugi) * (szerokoscPlytkiPodlogowej + szerokoscFugi)


def objetoscFugiDlaPlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi,
                                    wysokoscFugi):
    return (dlugoscPlytkiPodlogowej * szerokoscFugi * wysokoscFugi) + (
            szerokoscPlytkiPodlogowej * szerokoscFugi * wysokoscFugi)


def dlugosc_Podlogi():
    shouldContinue = True
    while shouldContinue:
        try:
            l = float(input("Prosze podac dlugosc pomieszczenia w metrach: "))
            shouldContinue = False
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")
    return l

def szerokosc_Podlogi():
    shouldContinue = True
    while shouldContinue:
        try:
            w = float(input("Prosze podac szerokosc pomieszczenia w metrach: "))
            shouldContinue = False
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")
    return w

def dlugosc_Plytki_Podlogowej():

    shouldContinue = True
    while shouldContinue:
        try:
            print ("")
            dlugoscPlytkiPodlogowej = float(input("Prosze podac dlugosc plytki podlogowej w metrach: "))
            shouldContinue = False

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return dlugoscPlytkiPodlogowej


def szerokosc_Plytki_Podlogowej():

    shouldContinue = True
    while shouldContinue:
        try:
            szerokoscPlytkiPodlogowej = float(input("Prosze podac szerokosc plytki podlogowej w metrach: "))
            shouldContinue = False

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return szerokoscPlytkiPodlogowej


def szerokosc_Fugi():

    shouldContinue = True
    while shouldContinue:

        should_Continue = True
        while should_Continue:
            try:
                szerokoscFugi = float(input("Prosze podac szerokosc fugi w metrach: "))
                should_Continue = False
            except SyntaxError:
                print ("Niepoprawne dane")
            except NameError:
                print ("Niepoprawne dane")
            except TypeError:
                print ("Niepoprawne dane")
            except ValueError:
                print ("Niepoprawne dane")


        if 0 < szerokoscFugi <= 0.010:
            shouldContinue = False
        else:
            print ("Szerokosc fugi powinna miescic sie w zakresie 0 - 0.01 m")

    return szerokoscFugi








