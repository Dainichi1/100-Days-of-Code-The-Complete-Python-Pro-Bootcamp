print ("Benvenuti alle Montagne Russe!")
altezza = int(input("Quanto sei alto in centimetri?"))

if altezza >= 120:
    print("Puoi salire!")
    età = int(input("Quanti anni hai?"))
    # minore di 12 anni
    if età < 12:
        print("il prezzo è 5 euro.")
    # tra 12 e 18 anni
    elif età <= 18:
        print("Il prezzo è 7 euro.")
    #maggiore di 18 anni
    else:
        print("Il prezzo è 12 euro.")
else:
    print("Non puoi salire!")
    