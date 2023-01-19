def act5():

    frase = input("introduce una frase: ")
    letra = input("Introduce una letra:")
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    print("La leta '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
act5()