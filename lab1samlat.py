def aritmetisk_summa():
    element1 = int(input("Vad är det första talet i den aritmetiska talföljden? "))
    differens = int(input("Vad är talföljdens differens? "))
    antal_element = int(input("Hur många element ska beräknas? "))
    summa_element = antal_element * ((element1 + (element1 + differens * (antal_element - 1))) / (2))
    print("Summan av talföljden är:", int(summa_element))

"""I den aritmetiska funktionen nedan efterfrågas din input som sedan beräknas och görs om till output i form av summan"""

aritmetisk_summa()


def geometrisk_summa():
    element1g = int(input("Vad är det första värdet i den geometriska talföljden? "))
    kvot = int(input("Vad är talföljdens kvot? "))
    antal_element = int(input("Hur många element ska beräknas? "))
    summa_element = int(element1g * (((kvot ** antal_element ) - 1) / (kvot - 1)))
    print("Summan av talföljden är:", int(summa_element))

"""I den geometriska funktionen nedan efterfrågas din input som sedan beräknas och görs om till output i form av summan"""

geometrisk_summa()
