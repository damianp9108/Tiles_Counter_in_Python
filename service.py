from podloga import polePodlogiWzorKlasyczny, objetoscFugiDlaPlytkiPodlogowej, polePodlogiWzorKaro, polePlytkiPodlogowej
from sciana import poleWszystkichOtworowSciennych, poleScianBezOtworowWzorKlasyczny, \
    objetoscFugiDlaPlytkiSciennej, poleScianBezOtworowWzorKaro, polePlytkiSciennej


def podlogaWzorKlasyczny(l, w, dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3):
    pole_Podlogi = polePodlogiWzorKlasyczny(l, w)
    pole_plytki_podlogowej = polePlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi)
    n = pole_Podlogi / pole_plytki_podlogowej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = (objetoscFugiDlaPlytkiPodlogowej(dlugoscPlytkiPodlogowej,
                                                                       szerokoscPlytkiPodlogowej, szerokoscFugi,
                                                                       wysokoscFugi)) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekPodlogowych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("* Liczba potrzebnych plytek podlogowych dla wzoru klasycznego: " + str(liczbaPotrzebnychPlytek))
    print ("* Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekPodlogowych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekPodlogowych


def podlogaWzorKaro(l, w, dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3):
    pole_Podlogi = polePodlogiWzorKaro(l, w)
    pole_plytki_podlogowej = polePlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi)
    n = pole_Podlogi / pole_plytki_podlogowej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = (objetoscFugiDlaPlytkiPodlogowej(dlugoscPlytkiPodlogowej,
                                                                       szerokoscPlytkiPodlogowej, szerokoscFugi,
                                                                       wysokoscFugi)) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekPodlogowych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("* Liczba potrzebnych plytek podlogowych dla wzoru karo: " + str(liczbaPotrzebnychPlytek))
    print ("* Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekPodlogowych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekPodlogowych


def scianaWzorKlasyczny(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3):
    poleScianBezOtworowWzorKlas = poleScianBezOtworowWzorKlasyczny(w, l, h)
    poleScianZotworami = poleScianBezOtworowWzorKlas - poleWszystkichOtworowSciennych(liczbaDrzwi, liczbaOkien,
                                                                                      wysokoscDrzwi, szerokoscDrzwi,
                                                                                      wysokoscOkna, szerokoscOkna)
    pole_plytki_sciennej = polePlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi)
    n = poleScianZotworami / pole_plytki_sciennej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej,
                                                                    szerokoscFugi,
                                                                    wysokoscFugi) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekSciennych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("* Liczba potrzebnych plytek sciennych dla wzoru klasycznego: " + str(liczbaPotrzebnychPlytek))
    print ("* Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekSciennych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekSciennych


def scianaWzorKaro(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3):
    poleScianBezOtworow = poleScianBezOtworowWzorKaro(w, l, h)
    poleScianZotworami = poleScianBezOtworow - poleWszystkichOtworowSciennych(liczbaDrzwi, liczbaOkien, wysokoscDrzwi,
                                                                              szerokoscDrzwi, wysokoscOkna,
                                                                              szerokoscOkna)
    pole_plytki_sciennej = polePlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi)
    n = poleScianZotworami / pole_plytki_sciennej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej,
                                                                    szerokoscFugi,
                                                                    wysokoscFugi) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekSciennych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("")
    print ("* Liczba potrzebnych plytek sciennych dla wzoru karo: " + str(liczbaPotrzebnychPlytek))
    print ("* Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekSciennych) + " kg")

    return wagaPotrzebnejFugiDlaPlytekSciennych


def wyborWzoruDlaPodlogi():

    shouldContinue = True
    while shouldContinue:
        try:
            wzorPodlogi = float(input(
                "Prosze wybrac wzor ulozenia plytek dla podlogi. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: "))

            if ((wzorPodlogi != 1) and (wzorPodlogi != 2)):
                print ("Niepoprawne dane")
            else:
                shouldContinue = False

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

    shouldContinue = True
    while shouldContinue:
        try:
            wzorSciany = float(input(
                "Prosze wybrac wzor ulozenia plytek dla sciany. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: "))

            if ((wzorSciany != 1) and (wzorSciany != 2)):
                print ("Niepoprawne dane")
            else:
                print ("")
                shouldContinue = False

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    return wzorSciany
