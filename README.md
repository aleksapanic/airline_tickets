airline_tickets

Python aplikacija za prodaju avionskih karata.

Ovu aplikaciju koriste dve grupe korisnika: prodavci i menadžeri. 

Svaki korisnik je opisan sledećim podacima:

    • Korisničko ime (jedinstveno u celom sistemu)
    • Lozinka
    • Ime
    • Prezime
    • Uloga (prodavac ili menadžer)

Osnovna informacija kojom aplikacija rukuje je avionski let. Avionski let je opisan
sledećim podacima:

    • Broj leta: identifikator oblika <slovo><slovo><cifra><cifra><cifra><cifra>
    • Polazište: troslovna oznaka aerodroma
    • Odredište: troslovna oznaka aerodroma
    • Vreme poletanja
    • Vreme sletanja
    • Prevoznik: naziv aviokompanije koja pruža uslugu prevoza
    • Dani u kojima se obavlja let: niz koji može imati 0 do 7 elemenata (ponedeljak,
    utorak, sreda, četvrtak, petak, subota, nedelja)
    • Model aviona: model aviona koji se koristi za let
    • Cena

Modeli aviona opisani su sledećim podacima:

    • Naziv
    • Broj redova (numeracija 1, 2, 3, ...)
    • Broj sedišta u redu (numeracija A, B, C, ...)

Avionske karte prodaju se pojedinačnim putnicima za koje su vezani sledeći podaci:

    • Ime
    • Prezime
    • Državljanstvo
    • Broj pasoša
