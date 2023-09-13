
#Det är här minnet för de olika funktionerna finns, här sparas talföljdernas art (aritmetisk/geometrisk)
aritmetiska_summor_lagring = []
geometriska_summor_lagring = []

"""Det här är en applikation som låter dig välja värdena du ska beräkna i aritmetiska eller geometriska talföljder.
Du har utöver det även möjligheten att gå in i ett jämförelseläge där du kan jämföra aritmetiska och geometriska talföljder.
Efter att beräkningarna har utförts kan du välja att lagra uträkningarna för att jämföra flera följder i efterhand."""

i = 0
while i == 0:
    aktivitet_val = input("Vad vill du göra?\n\n1) Beräkna aritmetisk summa   (a)\n2) Beräkna geometrisk summa   (g)\n\
3) Jämföra talföljder         (j)\n4) Komma åt lagringen         (l)\n5) Avsluta                    (q)\n")

    if aktivitet_val == "a":          
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

            j = 0
            while j == 0:
                lagra_summa = input("Vill du lagra denna talföljd? (y/n)\n")

                if lagra_summa == "y":
                    flashminne = [element1, differens, antal_element, summa_element]
                    aritmetiska_summor_lagring.append(flashminne)
                    print(f"Värdena", aritmetiska_summor_lagring, "har lagrats i minnet!\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    j = 1

                elif lagra_summa == "n":
                    print("Du har valt att inte spara något värde\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    j = 1

                else:
                    print("Skriv 'y' för att spara värdena eller 'n' för att slänga dem! Försök igen\n")
                    continue
        aritmetisk_summa()
        i = 0

    elif aktivitet_val == "g":
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

            k = 0
            while k == 0:
                lagra_summa = input("Vill du lagra denna talföljd? (y/n)\n")

                if lagra_summa == "y":
                    flashminne = [element1g, kvot, antal_element, summa_element]
                    geometriska_summor_lagring.append(flashminne)
                    print(f"Värdena", geometriska_summor_lagring, "har lagrats i minnet!\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    k = 1

                elif lagra_summa == "n":
                    print("Du har valt att inte spara något värde\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    k = 1

                else:
                    print("Skriv 'y' för att spara värdena eller 'n' för att slänga dem! Försök igen\n")
                    continue
        geometrisk_summa()
        i = 0
    
    elif aktivitet_val == "j":
        #Här borde jag lägga till valet att jämföra lagrade värden, alternativt lägga till det till jämförelseprompten
        def jämförelse_talföljder():
            while True:
                element1 = input("Nu får du börja med den aritmetiska talföljden!\nVad är det första talet i talföljden?\n")
                differens = input("Vad är den aritmetiska talföljdens differens?\n")
                element1g = input("Nu får du välja värdena i den geometriska talföljden, antalet element kommer du snart till!\n\
Vad är det första talet i den geometriska talföljden?\n")
                kvot = input("Vad är talföljdens kvot?\n")
                antal_element = input("Hur många element ska beräknas för talföljderna?\n")

                if element1.isdigit() and differens.isdigit() and antal_element.isdigit() and element1g.isdigit() and kvot.isdigit():
                    element1 = int(element1)
                    differens = int(differens)
                    antal_element = int(antal_element)
                    element1g = int(element1g)
                    kvot = int(kvot)
                    break

                else:
                    print("Skriv heltal eller flyttal på samtliga positioner! Försök igen")
                    continue

            summa_aritmetiska_element = antal_element * ((element1 + (element1 + differens * (antal_element - 1))) / (2))
            summa_geometriska_element = element1g * (((kvot ** antal_element) -1) / (kvot -1))

            print(f"Summan av den geometriska talföljden är:\n{summa_geometriska_element}")
            print(f"Summan av den aritmetiska talföljden är:\n{summa_aritmetiska_element}")

            if summa_aritmetiska_element > summa_geometriska_element:
                print("Den aritmetiska talföljden är större än den geometriska!")

            elif summa_geometriska_element > summa_aritmetiska_element:
                print("Den geometriska talföljden är större än den aritmetiska!")
            
            elif summa_aritmetiska_element == summa_geometriska_element:
                print("WOW! Talföljderna är lika stora!")

            j = 0
            while j == 0:
                lagra_summa = input("\nVill du lagra dessa talföljder? (y/n)\n")

                if lagra_summa == "y":
                    flashminne = [element1, differens, antal_element, summa_aritmetiska_element]
                    aritmetiska_summor_lagring.append(flashminne)
                    flashminne = [element1g, kvot, antal_element, summa_geometriska_element]
                    geometriska_summor_lagring.append(flashminne)
                    print(f"Värdena", aritmetiska_summor_lagring, "samt", geometriska_summor_lagring, "har lagrats i minnet!\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    j = 1

                elif lagra_summa == "n":
                    print("Du har valt att inte spara något värde\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    j = 1

                else:
                    print("Skriv 'y' för att spara värdena eller 'n' för att slänga dem! Försök igen\n")
                    continue          
        jämförelse_talföljder()
        i = 0

    elif aktivitet_val == "l":
        def lagringen():
            print(f"Aritmetiska databasen:\n {aritmetiska_summor_lagring}, \nGeometriska databasen:\n {geometriska_summor_lagring}")
        lagringen()
        i = 0



    elif aktivitet_val == "q":
        print("Välkommen åter!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        exit()
    
    else:
        print("Skriv in något av alternativen till höger!")



