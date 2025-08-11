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
    print(zahl1 + "+" + zahl2 + "=" + str(ergibnis))

if option == "2":
    # Minus Rechnen
    ergibnis = int(zahl1) - int(zahl2)
    print(zahl1 + "-" + zahl2 + "=" + str(ergibnis))


if option == "3":
    # Mal Rechnen
    ergibnis = int(zahl1) - int(zahl2)
    print(zahl1 + "x" + zahl2 + "=" + str(ergibnis))


if option == "4":
    # Geteiltdurch Rechnen
    ergibnis = int(zahl1) - int(zahl2)
    print(zahl1 + "/" + zahl2 + "=" + str(ergibnis))