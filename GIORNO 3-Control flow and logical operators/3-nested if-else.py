print ("Benvenuti alle Montagne Russe!")
altezza = int(input("Quanto sei alto in centimetri?"))

if altezza >= 120:
    print("Puoi salire!")
    età = int(input("Quanti anni hai?"))
    if età <= 18:
        print("Il prezzo è 7 euro")
    else:
        print("Il prezzo è 12 euro")
else:
    print("Non puoi salire!")
    