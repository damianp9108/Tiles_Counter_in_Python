from podloga import dlugosc_Podlogi, szerokosc_Podlogi, dlugosc_Plytki_Podlogowej, szerokosc_Plytki_Podlogowej, \
    szerokosc_Fugi
from sciana import wysokoscSciany, dlugosc_Plytki_Sciennej, szerokosc_Plytki_Sciennej, liczba_Drzwi, liczba_Okien, \
    wysokosc_Drzwi, szerokosc_Drzwi, wysokosc_Okna, szerokosc_Okna
from service import podlogaWzorKlasyczny, podlogaWzorKaro, scianaWzorKlasyczny, scianaWzorKaro, \
    wyborWzoruDlaPodlogi, wyborWzoruDlaSciany


def main():
    wysokoscFugi = 0.01
    wagaFugiDla1dm3 = 2

    print ("")
    print ("")
    print ("")
    print (
        "*** Program wyliczy ilosc potrzebnych plytek oraz wage potrzebnej fugi dla podlogi i scian na podstawie danych wprowadzonych przez uzytkownika ***")
    print ("")


    shouldContinue = True
    while shouldContinue:
        print ("")
        print ("")
        print ("")
        print ("** Wybierz opcje (Wpisz cyfre 1-6) **")
        print ("")
        print ("")
        print ("PODLOGA")
        print ("1. Oblicz ilosc potrzebnych plytek podlogowych oraz wage potrzebnej fugi dla wzoru klasycznego")
        print ("2. Oblicz ilosc potrzebnych plytek podlogowych oraz wage potrzebnej fugi dla wzoru karo")
        print ("")
        print ("SCIANY")
        print ("3. Oblicz ilosc potrzebnych plytek sciennych oraz wage potrzebnej fugi dla wzoru klasycznego")
        print ("4. Oblicz ilosc potrzebnych plytek sciennych oraz wage potrzebnej fugi dla wzoru karo")
        print ("")
        print ("CALE POMIESZCZENIE")
        print ("5. Oblicz ilosc potrzebnych plytek i wage potrzebnej fugi dla calego pomieszczenia w wybranej przez siebie konfiguracji.")
        print("")
        print("")
        print ("6. WYJSCIE Z PROGRAMU")
        print ("")

        should_Continue = True
        while should_Continue:
            try:
                userChoice = float(input(""))
                should_Continue = False

            except NameError:
                print ("Niepoprawne dane")
            except SyntaxError:
                print ("Niepoprawne dane")
            except TypeError:
                print ("Niepoprawne dane")
            except ValueError:
                print ("Niepoprawne dane")



        if not userChoice.is_integer():
            print ("To nie jest liczba calkowita!")

        elif userChoice == 1:
            l = dlugosc_Podlogi()
            w = szerokosc_Podlogi()
            dlugoscPlytkiPodlogowej = dlugosc_Plytki_Podlogowej()
            szerokoscPlytkiPodlogowej = szerokosc_Plytki_Podlogowej()
            szerokoscFugi = szerokosc_Fugi()

            podlogaWzorKlasyczny(l, w, dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)

        elif userChoice == 2:
            l = dlugosc_Podlogi()
            w = szerokosc_Podlogi()
            dlugoscPlytkiPodlogowej = dlugosc_Plytki_Podlogowej()
            szerokoscPlytkiPodlogowej = szerokosc_Plytki_Podlogowej()
            szerokoscFugi = szerokosc_Fugi()

            podlogaWzorKaro(l, w, dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)

        elif userChoice == 3:
            l = dlugosc_Podlogi()
            w = szerokosc_Podlogi()
            h = wysokoscSciany()
            liczbaDrzwi = liczba_Drzwi()
            liczbaOkien = liczba_Okien()
            wysokoscDrzwi = wysokosc_Drzwi()
            szerokoscDrzwi = szerokosc_Drzwi()
            wysokoscOkna = wysokosc_Okna()
            szerokoscOkna = szerokosc_Okna()
            dlugoscPlytkiSciennej = dlugosc_Plytki_Sciennej()
            szerokoscPlytkiSciennej = szerokosc_Plytki_Sciennej()
            szerokoscFugi = szerokosc_Fugi()

            scianaWzorKlasyczny(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)

        elif userChoice == 4:
            l = dlugosc_Podlogi()
            w = szerokosc_Podlogi()
            h = wysokoscSciany()
            liczbaDrzwi = liczba_Drzwi()
            liczbaOkien = liczba_Okien()
            wysokoscDrzwi = wysokosc_Drzwi()
            szerokoscDrzwi = szerokosc_Drzwi()
            wysokoscOkna = wysokosc_Okna()
            szerokoscOkna = szerokosc_Okna()
            dlugoscPlytkiSciennej = dlugosc_Plytki_Sciennej()
            szerokoscPlytkiSciennej = szerokosc_Plytki_Sciennej()
            szerokoscFugi = szerokosc_Fugi()

            scianaWzorKaro(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)

        elif userChoice == 5:
            wzorDlaPodlogi = wyborWzoruDlaPodlogi()
            wzorDlaSciany = wyborWzoruDlaSciany()

            l = dlugosc_Podlogi()
            w = szerokosc_Podlogi()
            h = wysokoscSciany()
            liczbaDrzwi = liczba_Drzwi()
            liczbaOkien = liczba_Okien()
            wysokoscDrzwi = wysokosc_Drzwi()
            szerokoscDrzwi = szerokosc_Drzwi()
            wysokoscOkna = wysokosc_Okna()
            szerokoscOkna = szerokosc_Okna()
            dlugoscPlytkiPodlogowej = dlugosc_Plytki_Podlogowej()
            szerokoscPlytkiPodlogowej = szerokosc_Plytki_Podlogowej()
            dlugoscPlytkiSciennej = dlugosc_Plytki_Sciennej()
            szerokoscPlytkiSciennej = szerokosc_Plytki_Sciennej()
            szerokoscFugi = szerokosc_Fugi()

            if wzorDlaPodlogi == 1:
                wagaFugi = podlogaWzorKlasyczny(l, w, dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)
            else:
                wagaFugi = podlogaWzorKaro(l, w, dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)

            if wzorDlaSciany == 1:
                wagaFugi2 = scianaWzorKlasyczny(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)
            else:
                wagaFugi2 = scianaWzorKaro(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna, dlugoscPlytkiSciennej, szerokoscPlytkiSciennej, szerokoscFugi, wysokoscFugi, wagaFugiDla1dm3)


            calaFuga = wagaFugi + wagaFugi2
            print ("")
            print ("* Laczna waga fugi dla calego pomieszczenia: " + str(calaFuga) + " kg")


        elif userChoice == 6:
            shouldContinue = False
        else:
            print ("Podaj cyfre od 1 do 6 !!")





if __name__ == '__main__':
    main()
