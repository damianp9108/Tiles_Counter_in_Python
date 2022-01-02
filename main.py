from fuga import szerokoscFugi, wagaFugiDla1dm3, wysokoscFugi
from podloga import polePlytkiPodlogowej, polePodlogiWzorKlasyczny, objetoscFugiDlaPlytkiPodlogowej, \
    dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, polePodlogiWzorKaro
from sciana import polePlytkiSciennej, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, poleWszystkichOtworowSciennych, \
    poleScianBezOtworowWzorKlasyczny, objetoscFugiDlaPlytkiSciennej, poleScianBezOtworowWzorKaro


def main():
    shouldContinue = True
    wagaPotrzebnejFugiDlaPlytekPodlogowych = 0
    wagaPotrzebnejFugiDlaPlytekSciennych = 0


    while shouldContinue == True:
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

    while shouldContinue == False:
        try:
            w = float(input("Prosze podac szerokosc pomieszczenia w metrach: "))
            shouldContinue = True
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    while shouldContinue == True:
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

    while shouldContinue == False:
        try:
            liczbaDrzwi = float(input("Prosze podac liczbe otworow drzwiowych: "))
            if liczbaDrzwi.is_integer():
                shouldContinue = True
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

    while shouldContinue == True:
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

    while shouldContinue == False:
        try:
            wysokoscDrzwi = float(input("Prosze podac wysokosc otworu drzwiowego w metrach: "))
            shouldContinue = True
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    while shouldContinue == True:
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

    while shouldContinue == False:
        try:
            wysokoscOkna = float(input("Prosze podac wysokosc otworu okiennego w metrach: "))
            shouldContinue = True
        except NameError:
            print ("Niepoprawne dane")
        except SyntaxError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")

    while shouldContinue == True:
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

    pole_plytki_podlogowej = polePlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi)

    while shouldContinue == False:
        try:
            wzorPodlogi = float(input(
            "Prosze wybrac wzor ulozenia plytek dla podlogi. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: "))

            if ((wzorPodlogi != 1) and (wzorPodlogi != 2)):
                print ("Niepoprawne dane")
            else:
                shouldContinue = True

        except SyntaxError:
            print ("Niepoprawne dane")
        except NameError:
            print ("Niepoprawne dane")
        except TypeError:
            print ("Niepoprawne dane")
        except ValueError:
            print ("Niepoprawne dane")



    while shouldContinue == True:
        try:
            wzorSciany = float(input(
                "Prosze wybrac wzor ulozenia plytek dla sciany. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: "))

            if ((wzorSciany != 1) and (wzorSciany != 2)):
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




    if (wzorPodlogi == 1):
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


    elif (wzorPodlogi == 2):
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




    pole_plytki_sciennej = polePlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi)
    poleOtworowSciennych = poleWszystkichOtworowSciennych(liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna,szerokoscOkna)




    if (wzorSciany == 1):
        poleScianBezOtworowWzorKlas = poleScianBezOtworowWzorKlasyczny(w, l, h)
        poleScianZotworami = poleScianBezOtworowWzorKlas - poleOtworowSciennych

        n = poleScianZotworami / pole_plytki_sciennej
        liczbaPotrzebnychPlytek = int(n) + 1

        objetoscFugiDlaWszystkichPlytek = objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi) * liczbaPotrzebnychPlytek
        objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
        wagaPotrzebnejFugiDlaPlytekSciennych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

        print ("")
        print ("Liczba potrzebnych plytek sciennych dla wzoru klasycznego: " + str(liczbaPotrzebnychPlytek))
        print ("Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekSciennych) + " kg")



    elif (wzorSciany == 2):

        poleScianBezOtworow = poleScianBezOtworowWzorKaro(w, l, h)
        poleScianZotworami = poleScianBezOtworow - poleOtworowSciennych

        n = poleScianZotworami / pole_plytki_sciennej
        liczbaPotrzebnychPlytek = int(n) + 1

        objetoscFugiDlaWszystkichPlytek = objetoscFugiDlaPlytkiSciennej(dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi)\
                                          * liczbaPotrzebnychPlytek
        objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
        wagaPotrzebnejFugiDlaPlytekSciennych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

        print ("")
        print ("Liczba potrzebnych plytek sciennych dla wzoru karo: " + str(liczbaPotrzebnychPlytek))
        print ("Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekSciennych) + " kg")


    calaFuga = wagaPotrzebnejFugiDlaPlytekPodlogowych + wagaPotrzebnejFugiDlaPlytekSciennych
    print ("")
    print ("Laczna waga fugi dla calego pomieszczenia: " + str(calaFuga))




if __name__ == '__main__':
    main()
