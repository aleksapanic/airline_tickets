import menu
import flights
import tickets
import menadzer

def main():
    name_user, last_name_user = menu.login()
    menu.printMenu()
    getCommand(name_user, last_name_user)

def getCommand(name_user, last_name_user):
    komanda = raw_input("Unesite zeljenu operaciju: ")
    komanda = komanda.upper()
    if(komanda in ('1', '2', '3', '4', '5', 'X')):
        if komanda == '1':
            flights.printFlights()
            checkFlights(name_user, last_name_user)
        elif komanda == '2':
            if menu.tip_korisnika == 0:
                tickets.addTickets(name_user, last_name_user)
                menu.printMenu()
                getCommand(name_user, last_name_user)
            else:
                print "Nemate pristup ovoj funkciji"
                menu.printMenu()
                getCommand(name_user, last_name_user)
        elif komanda == '3':
            if menu.tip_korisnika == 0:
                tickets.ticketChanging()
                menu.printMenu()
                getCommand(name_user, last_name_user)
            else:
                print "Nemate pristup ovoj funkciji"
                menu.printMenu()
                getCommand(name_user, last_name_user)
        elif komanda == '4':
            if menu.tip_korisnika == 0:
                tickets.deleteTicket()
                menu.printMenu()
                getCommand(name_user, last_name_user)
            else:
                print "Nemate pristup ovoj funkciji"
                menu.printMenu()
                getCommand(name_user, last_name_user)
        elif komanda == '5':
            if menu.tip_korisnika == 1:
                menadzer.izvestaji()
                menu.printMenu()
                getCommand(name_user, last_name_user)
            else:
                print "Nemate pristup ovoj funkciji"
                menu.printMenu()
                getCommand(name_user, last_name_user)
        elif komanda == "X":
            print "Prijatan ostatak dana."
            quit()
    else:
        print "\nNiste uneli odgovarajuci komandu\n"
        getCommand(name_user, last_name_user)
        flights.printFlights()
        checkFlights(name_user, last_name_user)


def checkFlights(first_name, last_name):
    komanda = raw_input("Unesite zeljenu operaciju: ")
    komanda = komanda.upper()
    if (komanda.upper() in ('1', '2', '3', '4', '5', '6', '7', 'X')):
        if komanda == '1':
            flights.sortStart()
            checkFlights(first_name, last_name)
        elif komanda == '2':
            flights.sortDestination()
            checkFlights(first_name, last_name)
        elif komanda == '3':
            flights.sortStartDate()
            checkFlights(first_name, last_name)
        elif komanda == '4':
            flights.sortDestinationDate()
            checkFlights(first_name, last_name)
        elif komanda == '5':
            flights.sortTimeLift()
            checkFlights(first_name, last_name)
        elif komanda == '6':
            flights.sortTimeLanding()
            checkFlights(first_name, last_name)
        elif komanda == '7':
            flights.sortCarrier()
            checkFlights(first_name, last_name)
        elif komanda == "X":
            menu.printMenu()
            getCommand(first_name, last_name)
    else:
        print "\nNiste uneli odgovarajuci komandu\n"
        checkFlights(first_name, last_name)

main()