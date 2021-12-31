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


dlugoscPlytkiPodlogowej = 0.5
szerokoscPlytkiPodlogowej = 0.5
