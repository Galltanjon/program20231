"""Geometrisk talföljd där kvoten mellan elementen är konstant.
Input från användare: första elementet g1, kvoten q, antal element n.
Utifrån dessa kan vi få ut värdet gn på element n, samt talföljdens summa sgn"""

element1 = int(input("Vad är det första värdet i talföljden? "))
kvot = int(input("Vad är talföljdens kvot? "))
antal_element = int(input("Hur många element ska beräknas? "))

element_n = int(element1 * kvot ** (antal_element - 1))
summa_element = int(element1 * (((kvot ** antal_element ) - 1) / (kvot - 1)))

print("\nVärdet på element", antal_element, "är:", element_n)
print("Summan av talföljden är:", summa_element)