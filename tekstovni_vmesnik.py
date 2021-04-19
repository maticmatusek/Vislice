import model


def izpis_igre(igra):
    return (
        f"Igraš igro vislic:\n" +
        f"Narobe ugibane črke so: {igra.nepravilni_ugibi()}\n" +
        f"Trenutno stanje besede: {igra.pravilni_del_gesla()}\n"
    )


def izpis_poraza(igra):
    return(
        f"Izgubil si, več sreče prihodnjič\n"
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n"
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n"
        f"Pravilno geslo je bilo: {igra.geslo}\n"

    )


def izpis_zmage(igra):
    return(
        f"Zmagal si, bravo\n"
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n"
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n"
        f"Pravilno geslo je bilo: {igra.geslo}\n"
        f"potreboval si {len(igra.crke)} ugibov"
    )


def pozeni_vmesnik():
    igra = model.nova_igra(model.bazen_besed)

    while True:
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
        else:
            print("\n\n\n\n\n\n\n\n\n")
            print(izpis_igre(igra))
            vnos = input("vnesi novo črko:\n")
            print(10 * "\n\n\n\n\n\n\n\n\n")
            igra.ugibaj(vnos)


while True:
    pozeni_vmesnik()
    if (input("Ali bi rad igral/a novo igro (da/ne):")) != "da":
        break
