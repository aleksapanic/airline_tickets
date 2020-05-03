import tickets
tip_korisnika = 0

def login():
    ulogovan = False
    while ulogovan == False:
        file = open("korisnici.txt","r")
        ime = raw_input("Unesite ime: ")
        pas = raw_input("Unesite lozinku: ")

        global tip_korisnika

        for i in file.readlines():
            podaci = i.split("|")
            if ime == podaci[0]:
                if pas == podaci[1]:
                    tip_korisnika = int(podaci[4])
                    if tip_korisnika == 0:  #nula oznacava prodavca
                        print "\nUlogovani ste kao prodavac"
                    if tip_korisnika == 1:  #jedan oznacava menadzera
                        print "\nUlogovani ste kao menadzer"
                    ulogovan = True
                    name=podaci[2]
                    last_name=podaci[3]
                else:
                    print "Pokusaj ponovo!"
        file.close()
        if ulogovan == False:
            print "Nepostojeci korisnik \n"
        else:
            return name,last_name

def printMenu():
    print "****************************************"
    print "1 - Pretraga letova"
    print "2 - Unos avionskih karata"
    print "3 - Izmena postojecih karata"
    print "4 - Brisanje postojecih karata"
    print "5 - Izvestavanje o prodatim kartama"
    print "X - izlaz iz programa"
    print "**************************************\n"

def continueMenu():
    choice=""
    while choice.upper() not in ("1", "X"):
        print "***************"
        print "1. dalji letovi"
        print "X. izlaz"
        choice = raw_input("Unesite broj: ")
    return choice

def checkUser():
    file = open("korisnici.txt","r")
    global korisnik
    for i in file.readlines():
        korisnik = i.split("|")