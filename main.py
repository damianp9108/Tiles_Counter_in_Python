from Service import podlogaWzorKlasyczny, podlogaWzorKaro, scianaWzorKlasyczny, scianaWzorKaro, \
    wyborWzoruDlaPodlogi, wyborWzoruDlaSciany


def main():
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

    while not shouldContinue:
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

    while not shouldContinue:
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

    while not shouldContinue:
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

    while not shouldContinue:
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



    while not shouldContinue:
        print ("")
        print ("")
        print ("")
        print ("Wymiary plytki podlogowej: 50 cm x 50 cm")
        print ("Wymiary plytki sciennej: 50 cm x 35 cm")
        print ("Szerokosc fugi: 0.6 cm")
        print ("Wysokosc fugi: 1 cm")
        print ("Waga fugi dla 1 dm3: 2 kg")
        print ("")
        print ("")
        print ("Wybierz opcje (Wpisz cyfre 1-5)")
        print ("1. Oblicz ilosc potrzebnych plytek podlogowych oraz wage potrzebnej fugi dla wzoru klasycznego")
        print ("2. Oblicz ilosc potrzebnych plytek podlogowych oraz wage potrzebnej fugi dla wzoru karo")
        print ("3. Oblicz ilosc potrzebnych plytek sciennych oraz wage potrzebnej fugi dla wzoru klasycznego")
        print ("4. Oblicz ilosc potrzebnych plytek sciennych oraz wage potrzebnej fugi dla wzoru karo")
        print ("5. Oblicz ilosc potrzebnych plytek i wage potrzebnej fugi dla calego pomieszczenia w wybranej przez siebie konfiguracji.")
        print ("6. Wyjscie")
        print ("")


        try:
            userChoice = float(input(""))
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
            podlogaWzorKlasyczny(l, w)

        elif userChoice == 2:
            podlogaWzorKaro(l, w)

        elif userChoice == 3:
            scianaWzorKlasyczny(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna)

        elif userChoice == 4:
            scianaWzorKaro(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna)

        elif userChoice == 5:
            wzorDlaPodlogi = wyborWzoruDlaPodlogi()
            wzorDlaSciany = wyborWzoruDlaSciany()
            if wzorDlaPodlogi == 1:
                wagaFugi = podlogaWzorKlasyczny(l, w)
            else:
                wagaFugi = podlogaWzorKaro(l, w)

            if wzorDlaSciany == 1:
                wagaFugi2 = scianaWzorKlasyczny(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna)
            else:
                wagaFugi2 = scianaWzorKaro(l, w, h, liczbaDrzwi, liczbaOkien, wysokoscDrzwi, szerokoscDrzwi, wysokoscOkna, szerokoscOkna)

            calaFuga = wagaFugi + wagaFugi2
            print ("")
            print ("Laczna waga fugi dla calego pomieszczenia: " + str(calaFuga))


        elif userChoice == 6:
            shouldContinue = True
        else:
            print ("Podaj liczbe od 1 do 5 !!")





if __name__ == '__main__':
    main()
