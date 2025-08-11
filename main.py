def Return():
    # Frage ob weiterrechnen

    print("")

    print("#######################")
    print("#                     #")
    print("# Terminal-Calculator #")
    print("#                     #")
    print("#######################")

    print("")

    print("########################")
    print("#                      #")
    print("#  Noch etwas rechnen? #")
    print("#                      #")
    print("#       Ja (y)         #")
    print("#      Nein (n)        #")
    print("#                      #")
    print("########################")

    print("")

    weiterrechnen = input("Deine Wahl: ")

    if weiterrechnen == "y":
        print("")
        rechnen()

    if weiterrechnen == "n":
        print("")
        print("Programm Beendet!")

def rechnen():
    print("")

    print("#######################")
    print("#                     #")
    print("# Terminal-Calculator #")
    print("#                     #")
    print("#######################")

    print("")

    print("########################")
    print("#                      #")
    print("#     Optionen:        #")
    print("#                      #")
    print("#      Plus (1)        #")
    print("#      Minus (2)       #")
    print("#       Mal (3)        #")
    print("#  Geteiltdurch (4)    #")
    print("#                      #")
    print("########################")

    print("")

    # Eingabe der Zahlen
    option = input("Option wählen (1-4): ")
    zahl1 = input("Erste Zahl eingeben: ")
    zahl2 = input("Zweite Zahl eingeben: ")


    if option == "1":
        # Plus Rechnen
        ergibnis = int(zahl1) + int(zahl2)
        print(zahl1 + " + " + zahl2 + " = " + str(ergibnis))
        Return()

    if option == "2":
        # Minus Rechnen
        ergibnis = int(zahl1) - int(zahl2)
        print(zahl1 + " - " + zahl2 + " = " + str(ergibnis))
        Return()


    if option == "3":
        # Mal Rechnen
        ergibnis = int(zahl1) - int(zahl2)
        print(zahl1 + " x " + zahl2 + " = " + str(ergibnis))
        Return()


    if option == "4":
        # Geteiltdurch Rechnen
        ergibnis = int(zahl1) - int(zahl2)
        print(zahl1 + " / " + zahl2 + " = " + str(ergibnis))
        Return()