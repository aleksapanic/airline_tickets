import datetime
import tickets

def reportMenu():
    print "**********************************************************************************"
    print "1 - Lista prodatih karata za izabrani dan prodaje"
    print "2 - Lista prodatih karata za izabrani dan polaska"
    print "3 - Lista prodatih karata za izabrani dan prodaje i prodavca"
    print "4 - Ukupan broj i cena prodatih karata za izabrani dan prodaje"
    print "5 - Ukupan broj i cena prodatih karata za izabrani dan polaska"
    print "6 - Ukupan broj i cena prodatih karata za izabrani dan prodaje i izabranog prodavca"
    print "7 - Ukupan broj i cena prodatih karata u poslednjih 30 dana po prodavcima"
    print "X - Nazad"
    print "**********************************************************************************"

    choice = raw_input("Unesite zeljenu operaciju: ")
    return choice

def izvestaji():
    choice = reportMenu()
    if choice == "1":
        repOne()
    if choice == "2":
        repTwo()
    if choice == "3":
        repThree()
    if choice == "4":
        repFour()
    if choice == "5":
        repFive()
    if choice == "6":
        repSix()
    if choice == "7":
        repSeven()

def repOne():
    date = raw_input("Unesite datum prodaje karte. Datum pisati u formatu dd.mm.yyyy. (npr. 12.2.2017.): ")
    file = open("karte.txt","r")
    for i in file.readlines():
        ticket = i.split('|')
        if date == ticket[4]:
            print i

def repTwo():
    date = raw_input("Unesite datum poletanja aviona: ")
    f = open("karte.txt","r")
    for i in f.readlines():
        ticket = i.split('|')
        if date == ticket[1]:
            print i

def repThree():
    date = raw_input("Unesite datum prodaje karte: ")
    name = raw_input("Unesite ime prodavca: ")
    last_name = raw_input("Unesite prezime prodavca: ")

    f = open("karte.txt","r")
    for i in f.readlines():
        ticket=i.split('|')
        if date == ticket[4] and name == ticket[-2] and last_name == ticket[-1].strip():
            print i

def repFour():
    date = raw_input("Unesite datum prodaje karte: ")
    f = open("karte.txt","r")
    num = 0
    z = 0
    for i in f.readlines():
        ticket = i.split('|')
        if date == ticket[4]:
            z = z + int(ticket[3])
            num = num + 1
    print "***********************************************"
    print "Ukupan broj prodatih karata izabrani datum je: ", num
    print "Ukupna cena je: ",z

def repFive():
    start_date = raw_input("Unesite datum polaska: ")
    f = open("karte.txt","r")
    num = 0
    z = 0
    for i in f.readlines():
        ticket = i.split('|')
        if start_date == ticket[1]:
            z = z + int(ticket[3])
            num = num + 1
    print "***********************************************"
    print "Ukupan broj prodatih karata izabrani datum je: ", num
    print "ukupna cena je: ", z

def repSix():
    date = raw_input("Unesite datum prodaje: ")
    name = raw_input("Ime prodavca: ")
    last_name = raw_input("Prezime prodavca: ")

    f = open("karte.txt","r")
    num = 0
    z = 0
    for i in f.readlines():
        ticket = i.split('|')
        if date == ticket[4] and name == ticket[-2] and last_name == ticket[-1].strip():
            z = z + int(ticket[3])
            num = num + 1
    print "***********************************************"
    print "Ukupan broj prodatih karata izabrani datum je: ", num
    print "Ukupna cena je: ", z


def repSeven():

    date_border = tickets.today() - datetime.timedelta(days=30)
    users = []
    f = open("korisnici.txt",'r')
    for k in f.readlines():
        users.append(k.split("|"))
    for k in users:
        f = open("karte.txt", 'r')
        if k[-1].strip() == "0":
            print "**************"
            print "Ime: ", k[2]
            print "Prezime: ", k[3]
            z = 0
            num = 0
            for i in f.readlines():
                ticket = i.split("|")

                if (datetime.datetime.strptime(ticket[4], "%d.%m.%Y.") > date_border and ticket[-1].strip() == k[3] and ticket[-2] == k[2]):
                    z = z + int(ticket[3])
                    num = num + 1
            print "***********************************************"
            print "Ukupan broj prodatih karata izabrani datum je: ", num
            print "Ukupna cena je: ", z