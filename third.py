import math

def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """
        
    try: # overeni hloupych Pepiku
        number = int(cislo)
    except ValueError:
        print("Opakuj pokus a zadej číselnou hodnotu")
        return False
    if(number < 2):
        print("Opakuj pokus a zadej funkční parametr! (>=2)")
        return False

    delitel:int = 2

    while(delitel <= math.sqrt(number)):
        if(number % delitel == 0):
            return False
        delitel += 1

    return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    try: # overeni hloupych Pepiku
        max = int(maximum)
    except ValueError:
        print("Opakuj pokus a zadej číselnou hodnotu")
        return []
    if(max < 2):
        print("Opakuj pokus a zadej funkční parametr! (>=2)")
        return []

    seznam_prvocisel:list[int] = []
    cislo:int = 2

    while(cislo <= max):
        if(je_prvocislo(cislo)):
            seznam_prvocisel.append(cislo)
        cislo += 1
    
    return seznam_prvocisel

if __name__ == "__main__":
    while(True):
        print(vrat_prvocisla(input("Zadej maximum: ")))