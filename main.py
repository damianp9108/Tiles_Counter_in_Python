def main():
    shouldContinue = True
    userWantChoose = True
    wysokoscOkna = 0
    szerokoscOkna = 0
    userChoise = 0
    szerokoscFugi = 0.006
    wysokoscFugi = 0.01
    wagaFugiDla1dm3 = 2
    dlugoscPlytkiPodlogowej = 0.5
    szerokoscPlytkiPodlogowej = 0.5
    liczbaPotrzebnychPlytek = 0

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




    l = input("Prosze podac dlugosc pomieszczenia w metrach: ")
    w = input("Prosze podac szerokosc pomieszczenia w metrach: ")
    h = input("Prosze podac wysokosc pomieszczenia w metrach: ")

    liczbaDrzwi = input("Prosze podac liczbe otworow drzwiowych: ")
    liczbaOkien = input("Prosze podac liczbe otworow okiennych: ")

    wysokoscDrzwi = input("Prosze podac wysokosc otworu drzwiowego w metrach: ")
    szerokoscDrzwi = input("Prosze podac szerokosc otworu drzwiowego w metrach: ")

    wysokoscOkna = input("Prosze podac wysokosc otworu okiennego w metrach: ")
    szerokoscOkna = input("Prosze podac szerokosc otworu okiennego w metrach: ")

    wzorPodlogi = input(
        "Prosze wybrac wzor ulozenia plytek dla podlogi. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: ")
    wzorSciany = input(
        "Prosze wybrac wzor ulozenia plytek dla sciany. Wpisz '1' dla wzoru klasyczego lub '2' dla wzoru karo: ")

    pole_plytki_podlogowej = polePlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi)

    if (wzorPodlogi == 1):
        pole_Podlogi = polePodlogiWzorKlasyczny(l, w)
    n = pole_Podlogi / pole_plytki_podlogowej
    liczbaPotrzebnychPlytek = int(n) + 1

    objetoscFugiDlaWszystkichPlytek = (objetoscFugiDlaPlytkiPodlogowej(dlugoscPlytkiPodlogowej, szerokoscPlytkiPodlogowej, szerokoscFugi, wysokoscFugi)) * liczbaPotrzebnychPlytek
    objetoscFugiDlaWszystkichPlytekWdm3 = objetoscFugiDlaWszystkichPlytek * 1000
    wagaPotrzebnejFugiDlaPlytekPodlogowych = objetoscFugiDlaWszystkichPlytekWdm3 * wagaFugiDla1dm3

    print ("Liczba potrzebnych plytek podlogowych dla wzoru klasycznego: " + str(liczbaPotrzebnychPlytek))
    print ("Waga potrzebnej fugi: " + str(wagaPotrzebnejFugiDlaPlytekPodlogowych) + " kg")


if __name__ == '__main__':
    main()
