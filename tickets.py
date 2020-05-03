from os.path import exists
from datetime import datetime
from datetime import timedelta
import flights
import menu

daniNedelje = ("pon", "uto", "sre", "cet", "pet", "sub", "ned", "pon")

def printTicket(ticket_list):
    print u"{0:10}|{1:12}|{2:8}|{3:8}|{4:12}|{5:8}|{6:8}|{7:8}|{7:8}|{8:15}|{9:10}|{10:10}|{11:10}|{12:10}|{13:10}".format(
        ticket_list[0],ticket_list[1],ticket_list[2],ticket_list[3],ticket_list[4],ticket_list[5],ticket_list[6],ticket_list[7],
        ticket_list[8],ticket_list[9],ticket_list[10],ticket_list[11],ticket_list[12],ticket_list[13],ticket_list[14],ticket_list[15])

def printFlight(flight_list):
    print u"{0:10}|{1:8}|{2:8}|{3:8}|{4:8}|{5:30}|{6:30}|{7:8}|{7:8}".format(
        flight_list[0], flight_list[1], flight_list[2], flight_list[3], flight_list[4], flight_list[5], flight_list[6],
        flight_list[7], flight_list[8])


def addTickets(name_user, last_name_user):
    flight, start_date, seat = chooseFlight()                             #Odabir sifre aviona

    ime, prezime, drzavljanstvo, pasos = personsData()
    writeTicket(ime, prezime, drzavljanstvo, pasos, start_date, flight, seat, name_user, last_name_user)
    choice = menu.continueMenu()

    while choice == "1":
        next_flights_list = []                                          #prazna lista sledecih letova
        if timeCompare(flight[3], flight[4]):
            end_date = datetime.strptime(start_date, "%d.%m.%Y.")       #konvertuje taj datum u dan u nedelji
            end_week_day = convertWeekDay(end_date.strftime("%A"))
            end_date2 = end_date
        else:                                                           # ako je nas let isao preko noci i dosao sutradan:
            end_date = datetime.strptime(start_date, "%d.%m.%Y.")
            end_date2 = end_date + timedelta(days=1)                    # dodaj jedan dan na datum, potom konvertuj u dan u nedelji
            end_week_day = convertWeekDay(end_date2.strftime("%A"))
        print end_week_day
        hour_later = minsToTime(timeToMins(flight[4])+60)                 #dodaje jos 60min zbog moguce kupovine naredne karte
        dayweek_tomorrow = (end_date2+timedelta(days=1)).strftime("%A")
        dayweek_tomorrow = convertWeekDay(dayweek_tomorrow)

        file = open("letovi.txt", 'r')
        for i in file.readlines():
            next_flight = i.split("|")
            if next_flight[1] == flight[2]:                                         #ako je mesto dolaska predhonog jednako sa mestom polaska sadasnjeg
                days = next_flight[6].split(",")                                      #lista dana u nedelji kad polece
                if end_week_day in days and timeCompare(hour_later, next_flight[3]):        #ako je dan polaska u toj listi
                    next_flights_list.append(next_flight)
                if dayweek_tomorrow in days and timeCompare(next_flight[3], flight[4]):     #ako je sutrasnji dan u toj listi
                    if next_flight not in next_flights_list:                                #ako let vec nije u listi, onda ga dodaj
                        next_flights_list.append(next_flight)
        for fl in next_flights_list:
            printFlight(fl)

        if next_flights_list == []:
            print "Ne postoje letovi koje biste mogli da nadovezete na prethodno kupljeni."
            return

        next_flight = chooseNewFlight(next_flights_list)
        start_date = newStartDate(flight,next_flight,start_date)

        flight = next_flight
        seat = freeSeats(flight,start_date)
        writeTicket(ime, prezime, drzavljanstvo, pasos, start_date, flight, seat, name_user, last_name_user)
        choice = menu.continueMenu()



def chooseNewFlight(list):
    keys = []
    for i in list:
        keys.append(i[0])
    f = False
    while f == False:
        fl_key = raw_input("Unesite sifru leta koji zelite da nadovezete: ")
        if fl_key.upper() in keys:
            f = True
        else:
            print "Ne postoji let za nadovezivanje sa unetom sifrom. Pokusajte opet!"
    for i in list:
        if fl_key == i[0]:
            break
    return i

def findFlight(let):
    for putnik in tickets:
        if putnik['let'] == let:
            return putnik
    return None

def chooseFlight(): #Poziva se u kupovini, bira se let po sifri dok se ne unese pravilna sifra
    while True:
        f = open("letovi.txt", 'r')
        sifra = raw_input("\nUnesite sifru leta koji hocete da kupite: ")
        for l in f.readlines():
            let = l.split('|')
            if let[0] == sifra.upper():
                f.close()
                datum, seat = chooseDate(let)
                return let, datum, seat
        print("\nNe postoji. Pokusajte opet!")

def chooseDate(flight):   #Biranje datuma pri kupovini
    date = raw_input("\nIzaberite datum poletanja. Datum mora biti dd.mm.yyyy. formata (12.2.2017. npr): ")
    while True:
        if not dateBefore(date):
            if checkDateForFlight(date, flight):
                seat=freeSeats(flight,date)
                return date, seat
            else:
                print "\nLet ciju ste sifru uneli ne leti tog datuma. Pokusajte ponovo!\n"
        else:
            print "\nDatum je prosao. Pokusajte ponovo\n"
        date = raw_input("\nIzaberite datum poletanja. Datum mora biti dd.mm.yyyy. formata (12.2.2017. npr): ")

def today(): #Vraca danasnji datum  bez satnice
    day = datetime.today().strftime('X%d.X%m.X%Y.').replace('X0','X').replace('X','')
    day = datetime.strptime(day,"%d.%m.%Y.")
    return day

def dateBefore(date): #Proverava da li je date prosao u odnosu na danasnji datum
    datum = datetime.strptime(date, "%d.%m.%Y.")
    if datum<today():
        return True
    return False

def checkDateForFlight(date, flight): #proverava da li flight leti datuma date
    datum = datetime.strptime(date, "%d.%m.%Y.")
    week_day = datum.strftime("%A")    #pretvara datum u dan u nedelji
    week_day = convertWeekDay(week_day)
    print week_day
    print flight[6].split(',')
    if week_day in flight[6].split(','):
        return True
    else:
        return False

def freeSeats(flight, start_date): #ispisuje tabelu sedista i vraca listu slobodnih sedista
    dimenzije = flight[7]
    dimenzije_split = dimenzije.split("/")
    rows = int(dimenzije_split[0])
    cols = int(dimenzije_split[1])
    seats = []
    for r in range(1,rows+1):
        for c in range(1,cols+1):
            f = open("karte.txt", 'r')
            free = True
            single_seat = str(r)+"/"+str(c)
            for l in f.readlines():
                ticketT = l.split("|")
                if start_date == ticketT[1] and flight[0] == ticketT[0] and single_seat == ticketT[2].strip():
                    print u"{0:7}".format("X"),
                    free = False
                    break
            if free:
                print u"{0:7}".format(single_seat),
                seats.append(single_seat)
        print ""
    insert_seat = ""
    while insert_seat not in seats:
        insert_seat = raw_input("Izaberite sediste koje biste da rezervisete: ")
    return insert_seat

def personsData():
    ime = raw_input("Ime kupca: ")
    prezime = raw_input("Prezime kupca: ")
    drzava = raw_input("Drzava: ")
    pasos = raw_input("Pasos kupca: ")
    print
    return ime, prezime, drzava, pasos

def writeTicket(name, last_name, state, passport, start_date, flight, seat, name_user, last_name_user):
    f = open("karte.txt",'a')
    line = flight[0] + "|" + start_date + "|" + seat + "|" + flight[8].strip() + "|" + today().strftime('X%d.X%m.X%Y.').replace('X0','X').replace('X','') + "|" + flight[1] + "|" + flight[2] + "|" + flight[3] + "|" + flight[4] + "|" + flight[5] + "|" + name + "|" + last_name + "|" + state + "|" + passport + "|" + name_user + "|" + last_name_user +"\n"
    f.write(line)

def convertWeekDay(day):
    if day == "Monday":
        return "pon"
    if day == "Tuesday":
        return "uto"
    if day == "Wednesday":
        return "sre"
    if day == "Thursday":
        return "cet"
    if day == "Friday":
        return "pet"
    if day == "Saturday":
        return "sub"
    if day == "Sunday":
        return "ned"

def timeToMins(time): #prebacuje vreme u minute
    time = time.split(":")
    mins = int(time[0]) * 60 + int(time[1])
    return mins

def minsToTime(mins): #obrnuto od funkcije iznad, prebacuje minute u vreme
    hours = mins/60
    time = str(hours) + ":" + str(mins%60)
    return time

def timeCompare(time1,time2):  # time1 i time2 su vremena (hh:mm) pretvara ih u minute i poredi. Na taj nacin znam koje vreme je manje a koje vece.
    time1_mins = timeToMins(time1)
    time2_mins = timeToMins(time2)
    if time1_mins < time2_mins:
        return True
    return False

def newStartDate(flight,new_flight,start_date):
    new_start_date = start_date
    if (timeCompare(flight[4], flight[3])):
        new_start_date = datetime.strptime(new_start_date, "%d.%m.%Y.")
        new_start_date = new_start_date + timedelta(days=1)
        new_start_date = new_start_date.strftime('X%d.X%m.X%Y.').replace('X0','X').replace('X','')

    if (timeCompare(new_flight[3], flight[4])):
        new_start_date = datetime.strptime(new_start_date, "%d.%m.%Y.")
        new_start_date = new_start_date + timedelta(days=1)
        new_start_date = new_start_date.strftime('X%d.X%m.X%Y.').replace('X0','X').replace('X','')

    return new_start_date

def deleteTicket():
    flight_key = raw_input("Unesite sifru leta: ")
    flight_date = raw_input("Unesite datum poletanja: ")
    seat = raw_input("Unesite sediste (opciono): ")
    if seat == "":
        passport_num = raw_input("Unesite pasos (opciono): ")
    else:
        passport_num = ""
    f = open("karte.txt",'r')
    tickets = []
    delete = False
    for tick in f.readlines():
        ticket_list = tick.split('|')
        passport_and_seat = {ticket_list[2], ticket_list[13]}  #sediste i broj pasosa
        if ticket_list[0] == flight_key.upper() and ticket_list[1] == flight_date and (seat in passport_and_seat or passport_num in passport_and_seat):
            delete = True
            continue
        else:
            tickets.append(tick)                                                    #sada je lista flights napunjena svim letovima koji ne treba da se brisu
    if not delete:
        print "Ne postoji karta za unete argumente. Pokusajte opet"
        return
    f = open("karte.txt","w")
    for tick in tickets:
        f.write(tick)


def ticketChanging():
    flight_key = raw_input("Unesite sifru leta: ")
    flight_date = raw_input("Unesite datum poletanja: ")
    passport_num = raw_input("Unesite pasos : ")

    f = open("karte.txt", 'r')
    tickets_l = []                                                                              #lista neizmenjenih
    change_ticket = []                                                                          #lista podataka karte za menjanje
    for tick in f.readlines():
        ticket_list = tick.split('|')
        if ticket_list[0] == flight_key.upper() and ticket_list[1] == flight_date and passport_num == ticket_list[-3]:
            change_ticket = ticket_list
            continue
        tickets_l.append(tick)

    if change_ticket == []:
        print "Ne postoji karta za unete argumente"
        return
    else:
        print "*********************************"
        print "a - Izmena leta, datuma i sedista"
        print "b - Izmena datuma i sedista"
        print "c - Izmena sedista"

        choice = raw_input("Unesite slovo ispred zeljene komande: ")
        if choice == "a":
            f = open("letovi.txt", "r")
            for fl in f.readlines():
                if flight_key == fl.split('|')[0]:
                    break

            flight, flight_date, seat = chooseFlight()
            change_ticket[0] = flight[0]
            change_ticket[1] = flight_date
            change_ticket[2] = seat
            change_ticket[3] = flight[8]
            change_ticket[4] = today().strftime("X%d.X%m.X%Y.").replace("X0","X").replace("X","")
            change_ticket[5] = flight[1]
            change_ticket[6] = flight[2]
            change_ticket[7] = flight[3]
            change_ticket[8] = flight[4]
            change_ticket[9] = flight[5]
            f = open("karte.txt","w")
            for tick in tickets_l:
                f.write(tick)
            change_ticket[3] = change_ticket[3].strip() # Ostaje \n na kraju cene
            f.write(('|').join(change_ticket))

        if choice == "b":
            f = open("letovi.txt", "r")
            for fl in f.readlines():
                if flight_key == fl.split('|')[0]:
                    break

            flight_date, seat = chooseDate(fl.split('|'))
            change_ticket[1] = flight_date
            change_ticket[2] = seat
            f = open("karte.txt",'w')
            for tick in tickets_l:
                f.write(tick)
            f.write(('|').join(change_ticket))

        if choice == "c":
            f = open("letovi.txt", "r")
            for fl in f.readlines():
                if flight_key == fl.split('|')[0]:
                    break
            seat = freeSeats(fl.split('|'), flight_date)
            change_ticket[2] = seat
            f = open("karte.txt", 'w')
            for tick in tickets_l:
                f.write(tick)
            f.write(('|').join(change_ticket))

