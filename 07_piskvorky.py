# Nakonec trošku delší projekt, budeme ho dokončovat v úkolech k další lekci. 
# Jedná se o hru piškvorky, následuje popis hry, ke které se postupně dopracuješ:

# 1-D piškvorky se hrají na řádku s dvaceti políčky. 
# Hráči střídavě přidávají kolečka ('o') a křížky ('x'), třeba:
# 1. kolo: -------x------------
# 2. kolo: -------x--o---------
# 3. kolo: -------xx-o---------
# 4. kolo: -------xxoo---------
# 5. kolo: ------xxxoo---------
# Hráč, který dá tři své symboly vedle sebe, vyhrál.


# Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek 
# a vrátí jednoznakový řetězec podle stavu hry:

# "x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
# "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
# "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


# print(vyhodnot("xxooxxooxxooxoxoxoxoxox"))


# # Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), 
# a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem 
# umístěným na danou pozici.

# Hlavička funkce by tedy měla vypadat nějak takhle:

# def tah(pole, cislo_policka, symbol):
#     "Vrátí herní pole s daným symbolem umístěným na danou pozici"
#     ...
# Můžeš využít nějakou funkci, kterou jsme napsaly už na sraze?

def tah(pole, cislo_policka, symbol):
#     "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    pole = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return(pole)

#print(tah("-------xx-o---------", 9, "x"))

# ano, použila jsem funkci zamen ze srazu :)

# Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, 
# na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče. 
# Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. 
# Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.

# Nezapomeň, že už máš funkci tah z předešlého úkolu.

# for hrac1 symbol = "x" 
# for hrac2 symbol = "o"

def tah_hrace(pole, cislo_hrace):
    dobra_pozice = False
    if cislo_hrace == 1:
        symbol = "x"
    elif cislo_hrace == 2:
        symbol = "o"
    while dobra_pozice != True:
        cislo_policka = int(input("Zadejte číslo pozice, na které chcete hrát: "))
        if cislo_policka < 0 or cislo_policka >= 20:
            print("Dostal jste se mimo herní plochu!")
        # cislo_policka = int(input("Zadejte číslo pozice, na které chcete hrát: "))
        else:
            if pole[cislo_policka] != "-":
                print("Tato pozice je již obsazena")
        # cislo_policka = int(input("Zadejte číslo pozice, na které chcete hrát: "))
            else:
                dobra_pozice = True
    pole = tah(pole, cislo_policka, symbol)
    return pole

    

# print(tah_hrace("-------xx-o---------", 2))
# print(tah_hrace("-o-----xx-o---X-----", 1))

# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, 
# na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

# Použij jednoduchou náhodnou „strategii”:

# Vyber číslo od 0 do 19.
# Pokud je dané políčko volné, hrej na něj.
# Pokud ne, opakuj od bodu 1.
# Můžeš předpokládat, že řetězec s herním polem vždy obsahuje alespoň jednu volnou pozici.

# Hlavička funkce by tedy měla vypadat nějak takhle:

from random import randrange

# def tah_pocitace(pole):
# #   "Vrátí herní pole se zaznamenaným tahem počítače"
# #   počítač má tah 'x'
#     policko = 'x'
#     while policko != '-':
#         cislo_policka = randrange(0, 20)
#         print(cislo_policka)
#         policko = pole[cislo_policka]
#     pole = tah(pole, cislo_policka, 'x')
#     return pole

# print(tah_pocitace('--o----xx-o----o----'))
# print(tah_pocitace('xooooooxxoooooooooo-'))

def tah_hrace(pole):
    dobra_pozice = False
    while dobra_pozice != True:
        cislo_policka = int(input("Zadejte číslo pozice, na které chcete hrát: "))
        if cislo_policka < 0 or cislo_policka >= 20:
            print("Dostal jste se mimo herní plochu!")
        # cislo_policka = int(input("Zadejte číslo pozice, na které chcete hrát: "))
        else:
            if pole[cislo_policka] != "-":
                print("Tato pozice je již obsazena")
        # cislo_policka = int(input("Zadejte číslo pozice, na které chcete hrát: "))
            else:
                dobra_pozice = True
    pole = tah(pole, cislo_policka, 'o')
    return pole


# Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem 
# a střídavě volá funkce tah_hrace a tah_pocitace, dokud někdo 
# nevyhraje nebo nedojde k remíze.

# Nezapomeň kontrolovat stav hry po každém tahu.

# def piskvorky1D():
#     pole = '-'*20
#     print(pole)
#     pole = tah_hrace(pole)
#     print(pole)
#     pole = tah_pocitace(pole)
#     print(pole)
#     vysledek = vyhodnot(pole)
#     while vysledek == '-':
#         pole = tah_hrace(pole)
#         print(pole)
#         pole = tah_pocitace(pole)
#         print(pole)
#         vysledek = vyhodnot(pole)
#     return vysledek

# print('Vyhrál', piskvorky1D())


def tah_pocitace(pole):
#   "Vrátí herní pole se zaznamenaným tahem počítače"
#   počítač má tah 'x'
    neodehrano = True
    for i in range(18):
        if neodehrano:
            if pole[i] == pole[i+1] == 'x' and pole[i+2] == '-':
                pole = tah(pole, i+2, 'x')
                neodehrano = False
            elif pole[i+2] == pole[i+1] == 'x' and pole[i] == '-':
                pole = tah(pole, i, 'x')
                neodehrano = False
            elif pole[i+2] == pole[i] == 'x' and pole[i+1] == '-':
                pole = tah(pole, i+1, 'x')
                neodehrano = False
            elif pole[i] == pole[i+1] == 'o' and pole[i+2] == '-':
                pole = tah(pole, i+2, 'x')
                neodehrano = False
            elif pole[i+2] == pole[i+1] == 'o' and pole[i] == '-':
                pole = tah(pole, i, 'x')
                neodehrano = False
            elif pole[i+2] == pole[i] == 'o' and pole[i+1] == '-':
                pole = tah(pole, i+1, 'x')
                neodehrano = False
    if neodehrano:
        for i in range(19):
            if neodehrano:
                if pole[i] == 'x' and pole[i+1] == '-':
                    pole = tah(pole, i+1, 'x')
                    neodehrano = False
                elif pole[i+1] == 'x' and pole[i] == '-':
                    pole = tah(pole, i, 'x')
                    neodehrano = False
    if neodehrano:
        for i in range(18):
            if neodehrano:
                if pole[i+2] == pole[i] == '-' and pole[i+1] == 'o':
                    pole = tah(pole, i, 'x')
                    neodehrano = False
    return pole

def piskvorky1D():
    pole = '-'*20
    print(pole)
    pole = tah_hrace(pole)
    print(pole)
    pole = tah_pocitace(pole)
    print(pole)
    vysledek = vyhodnot(pole)
    while vysledek == '-':
        pole = tah_hrace(pole)
        print(pole)
        pole = tah_pocitace(pole)
        print(pole)
        vysledek = vyhodnot(pole)
    return vysledek

vitez= piskvorky1D()

if vitez == '!':
    print('Remíza')
else:
    print('Vyhrál', vitez)
