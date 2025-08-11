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

wählen = input("Bitte eine Option auswählen. ")

if wählen == "1":
    PlusRechnen()


if wählen == "2":
    MinusRechnen()


if wählen == "3":
    MalRechnen()


if wählen == "4":
    GeteiltdurchRechnen()