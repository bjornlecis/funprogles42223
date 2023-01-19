personen = {"Jan":"Hasselt","Frank":"Genk","Veerle":"Genk","Bert":"Bilzen"}
def keuze():
    print("1: toon namen en woonplaats")
    print("2: voeg een item toe")
    print("3: pas een item aan")
    print("4: verwijder een item")

def gebruikers_invoer():
    keuze()
    invoer = input("geef je keuze in")
    return invoer

invoer = gebruikers_invoer()
while not invoer == "stop":
    if invoer == "1":
        
    elif invoer == "2":

    elif invoer == "3":

    elif invoer == "4":

    else:
        print("foutieve invoer")
    gebruikers_invoer()
