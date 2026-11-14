
def cislo_text(cislo:int):

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    nactky = ["chyba", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["chyba", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát", "sto"]

    str_cislo = str(cislo)

    if (cislo < 0): # overeni podminky od 0-100
        return "Vstupní číslo < 0."
    elif (cislo > 100):
        return "Vstupní číslo > 100."

    if (cislo == 100): 
        return desitky[10]
    elif (0 <= cislo < 10):
        return jednotky[cislo]
    elif ((cislo % 10) == 0):
        return desitky[int(str_cislo[0])]
    elif (cislo < 20):
        return nactky[cislo - 10]
    else:
        return (desitky[int(str_cislo[0])] + " " + jednotky[int(str_cislo[1])])

    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    # return "dvacet pět"

if __name__ == "__main__":
    print(cislo_text(int(input("Zadej číslo: "))))