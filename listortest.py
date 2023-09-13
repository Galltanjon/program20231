"""def välja_funktion():
välja_funktion()

def välja_talföljd():
välja_talföljd()"""



#Det är här minnet för de olika funktionerna finns, här sparas talföljdernas art (aritmetisk/geometrisk)
aritmetiska_summor_lagring = []
geometriska_summor_lagring = []



def aritmetisk_summa():
    """Funktionen undersöker vad användaren vill beräkna och vad denne vill spara, och felsöker ständigt genom while-loopar.
    En while-sats som fortsätter att loopas om inputen till frågorna inte besvaras med heltal (eller floats i nästa version).
    isdigit() kollar att värdena faktiskt är siffror, om de är det görs inputen i varje fall om till heltal och loopen bryts.
    Om else-villkoret uppfylls leder continue-kommandot tillbaka användaren till början av while-loopen och får börja om."""

    while True:
        element1 = input("Vad är det första talet i den aritmetiska talföljden?\n")
        differens = input("Vad är talföljdens differens?\n")
        antal_element = input("Hur många element ska beräknas?\n")

        if element1.isdigit() and differens.isdigit() and antal_element.isdigit():
            element1 = int(element1)
            differens = int(differens)
            antal_element = int(antal_element)
            break

        else:
            print("Skriv heltal eller flyttal på samtliga positioner! Försök igen")
            continue
   
    """Nedan genomförs beräkningen av summan som sedan skrivs ut, om användaren väljer att spara värdena kan denne göra det.
    Dessa kommer sedan kunna användas vid en eventuella framtida jämförelser mellan olika summor (eller typer av summor).
    "flashminne" används för att kunna lägga till flera värden åt gången mha .append()-kommandot som annars bara tar ett.
    Variabeln i som ansätts till 0 används för att på enklast sätt undvika upprepningar av loopen, som bryts då i = 1."""

    summa_element = antal_element * ((element1 + (element1 + differens * (antal_element - 1))) / (2))
    print(f"Summan av den aritmetiska talföljden är:\n{summa_element}")

    i = 0
    while i == 0:
        lagra_summa = input("Vill du lagra denna talföljd? (y/n)\n")

        if lagra_summa == "y":
            flashminne = [element1, differens, antal_element, summa_element]
            aritmetiska_summor_lagring.append(flashminne)
            print(f"Värdena", aritmetiska_summor_lagring, "har lagrats i minnet!\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            i = 1

        elif lagra_summa == "n":
            print("Du har valt att inte spara något värde\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            i = 1

        else:
            print("Skriv 'y' för att spara värdena eller 'n' för att slänga dem! Försök igen\n")
            continue
                  
aritmetisk_summa()


def geometrisk_summa():
    """Den geometriska talföljdsloopen fungerar som den aritmetiska förutom att vi även felsöker division med 0"""
    
    while True:
        element1g = input("Vad är det första talet i den geometriska talföljden?\n")
        kvot = input("Vad är talföljdens kvot?\n")
        antal_element = input("Hur många element ska beräknas?\n")

        if element1g.isdigit() and kvot.isdigit() and antal_element.isdigit():
            element1g = int(element1g)
            kvot = int(kvot)
            antal_element = int(antal_element)
            break

        else:
            print("Skriv heltal eller flyttal på samtliga positioner! Försök igen")
            continue

    """Lagringen för den geometriska talföljden är identisk med den aritmetiska förutom variabelnamnen"""

    summa_element = element1g * (((kvot ** antal_element) -1) / (kvot -1))
    print(f"Summan av den geometriska talföljden är:\n{summa_element}")

    i = 0
    while i == 0:
        lagra_summa = input("Vill du lagra denna talföljd? (y/n)\n")

        if lagra_summa == "y":
            flashminne = [element1g, kvot, antal_element, summa_element]
            geometriska_summor_lagring.append(flashminne)
            print(f"Värdena", geometriska_summor_lagring, "har lagrats i minnet!\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            i = 1

        elif lagra_summa == "n":
            print("Du har valt att inte spara något värde\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            i = 1

        else:
            print("Skriv 'y' för att spara värdena eller 'n' för att slänga dem! Försök igen\n")
            continue
geometrisk_summa()
print(aritmetiska_summor_lagring, geometriska_summor_lagring)
