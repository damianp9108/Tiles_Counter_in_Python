from fuga import szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3
from podloga import polePodlogiWzorKlasyczny, objetoscFugiDlaPlytkiPodlogowej, dlugoscPlytkiPodlogowej, \
    szerokoscPlytkiPodlogowej, polePlytkiPodlogowej, polePodlogiWzorKaro
from sciana import polePlytkiSciennej, poleWszystkichOtworowSciennych, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, \
    poleScianBezOtworowWzorKlasyczny, objetoscFugiDlaPlytkiSciennej, poleScianBezOtworowWzorKaro

pole_plytki_podlogowej = polePlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi)
pole_plytki_sciennej = polePlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi)


def podlogaWzorKlasyczny(l, w):
    pole_Podlogi = polePodlogiWzorKlasyczny(l, w)
    n = pole_Podlogi / pole_plytki_podlogowej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = (objetoscFugiDlaPlytkiPodlogowej(dlugoscPlytkiPodlogowej,
                                                                       szerokoscPlytkiPodlogowej, szerokoscFugi,
                                                                       wysokoscFugi)) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekPodlogowych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("Liczba potrzebnych plytek podlogowych dla wzoru klasycznego: " + str(liczbaPotrzebnychPlytek))
    print ("Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekPodlogowych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekPodlogowych


def podlogaWzorKaro(l, w):
    pole_Podlogi = polePodlogiWzorKaro(l, w)
    n = pole_Podlogi / pole_plytki_podlogowej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = (objetoscFugiDlaPlytkiPodlogowej(dlugoscPlytkiPodlogowej,
                                                                       szerokoscPlytkiPodlogowej, szerokoscFugi,
                                                                       wysokoscFugi)) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekPodlogowych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("Liczba potrzebnych plytek podlogowych dla wzoru karo: " + str(liczbaPotrzebnychPlytek))
    print ("Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekPodlogowych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekPodlogowych


def scianaWzorKlasyczny(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna):
    poleScianBezOtworowWzorKlas = poleScianBezOtworowWzorKlasyczny(w, l, h)
    poleScianZotworami = poleScianBezOtworowWzorKlas - poleWszystkichOtworowSciennych(liczbaDrzwi, liczbaOkien,
                                                                                      wysokoscDrzwi, szerokoscDrzwi,
                                                                                      wysokoscOkna, szerokoscOkna)

    n = poleScianZotworami / pole_plytki_sciennej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej,
                                                                    szerokoscFugi,
                                                                    wysokoscFugi) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekSciennych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("Liczba potrzebnych plytek sciennych dla wzoru klasycznego: " + str(liczbaPotrzebnychPlytek))
    print ("Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekSciennych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekSciennych


def scianaWzorKaro(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna):
    poleScianBezOtworow = poleScianBezOtworowWzorKaro(w, l, h)
    poleScianZotworami = poleScianBezOtworow - poleWszystkichOtworowSciennych(liczbaDrzwi, liczbaOkien, wysokoscDrzwi,
                                                                              szerokoscDrzwi, wysokoscOkna,
                                                                              szerokoscOkna)

    n = poleScianZotworami / pole_plytki_sciennej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej,
                                                                    szerokoscFugi,
                                                                    wysokoscFugi) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekSciennych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("Liczba potrzebnych plytek sciennych dla wzoru karo: " + str(liczbaPotrzebnychPlytek))
    print ("Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekSciennych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekSciennych


def wyborWzoruDlaPodlogi():
    badInput = True

    while badInput:
        try:
            wzorPodlogi = float(input(
                "Prosze wybrac wzor ulozenia plytek dla podlogi. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: "))

            if ((wzorPodlogi != 1) and (wzorPodlogi != 2)):
                print ("Niepoprawne dane")
            else:
                badInput = False

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return wzorPodlogi


def wyborWzoruDlaSciany():
    badInput = True
    while badInput:
        try:
            wzorSciany = float(input(
                "Prosze wybrac wzor ulozenia plytek dla sciany. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: "))

            if ((wzorSciany != 1) and (wzorSciany != 2)):
                print ("Niepoprawne dane")
            else:
                print ("")
                badInput = False

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return wzorSciany
