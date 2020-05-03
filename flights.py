from datetime import datetime
pronasaoBaremJednog = False
daniNedelje = ("pon", "uto", "sre", "cet", "pet", "sub", "ned", "pon")

def searchFlights(option, value):
    global daniNedelje
    file = open("letovi.txt","r")

    for l in file.readlines():
        global podaci
        podaci = l.split("|")
        if option == 1:
            if podaci[1] == value.upper():
               printPodaci()                                                        #Gleda polaziste
        elif option == 2:
            if podaci[2] == value.upper():
                printPodaci()
            if podaci[3] == value:
                printPodaci()
        elif option == 3:
            if podaci[3] == value:
                printPodaci()
        elif option == 4:
            if podaci[4] == value:
                printPodaci()
        elif option == 5:
            if podaci[5] == value:
                printPodaci()
        elif option == 6:
            if daniNedelje[value] in podaci[6]:                                     #da li datum koji smo uneli se nalazi u tom sestom splitovanom delu
                printPodaci()
        elif option == 7:
            jedan = podaci[3].split(":")[0]
            dva = podaci[4].split(":")[0]

            if jedan < dva:
                if daniNedelje[value] in podaci[6]:
                    printPodaci()
            else:
                if daniNedelje[value + 1] in podaci[6]:
                    printPodaci()
            #Gleda odrediste

    if not pronasaoBaremJednog:
        print "Ne postoji let sa zadatim parametrima!"


def printFlights():
    print "\n************************"
    print "Mozete pretraziti let po: "
    print "1 - Polaziste"
    print "2 - Odrediste"
    print "3 - Datum polaska"
    print "4 - Datum dolaska"
    print "5 - Vreme poletanja"                                         #kao kod polazista i odredista
    print "6 - Vreme sletanja"
    print "7 - Prevoznik"
    print "X - Izlazak"
    print "*************************\n"

def sortStart():
    polazak = raw_input("Unesite mesto polazka: ")
    searchFlights(1, polazak)

def printPodaci():
    global pronasaoBaremJednog
    if pronasaoBaremJednog == False:                                    # pitamo da li nije true tj da li je false
        pronasaoBaremJednog = True                                      # ako je false postavljamo na true, u suprotnom preskacemo
    print podaci

def sortDestination():
    odrediste = raw_input("Unesite mesto sletanja: ")
    searchFlights(2, odrediste)

def sortCarrier():
    prevoznik = raw_input("Unesite ime prevoznika: ")
    searchFlights(5, prevoznik)

def sortStartDate():
    vreme = raw_input("Unesite datum polaska(exp. 12.3.2017.): ")
    datum = datetime.strptime(vreme, "%d.%m.%Y.")
    searchFlights(6, datum.weekday()-1)                                 #zato sto niz krece od 0, a fja vraca broj pocevsi od 1
    print datum.weekday()
    print datum.weekday()-1

def sortDestinationDate():
    vreme = raw_input("Unesite datum dolaska(exp. 12.3.2017.): ")
    datum = datetime.strptime(vreme, "%d.%m.%Y.")
    searchFlights(7, datum.weekday()-1)
    print datum.weekday()
    print datum.weekday() - 1

def sortTimeLanding():
    vreme = raw_input("Unesite vreme sletanja: ")
    searchFlights(4, vreme)

def sortTimeLift():
    vreme = raw_input("Vreme poletanja: ")
    searchFlights(3, vreme)

def printAllFlights():                                                      #ispis svih letova
    f = open("letovi.txt")
    for l in f.readlines():
        print l