def imprimir_mapa(mapa: list):
    for elem in mapa:
        for elem2 in elem:
            if elem2 != "":
                print("|{:<14}".format(elem2.nombre), end="")
            else:
                print("|{:<14}".format(""), end="")
        print("|")