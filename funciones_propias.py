def contar_caracteres(arg="La frase 'Aprender Python es divertido' tiene"):

    arg1=arg[8:38]


    #print(arg1)

    longitud=len(arg1)

    print(arg,longitud,"caracteres\n")


contar_caracteres()


def convertir_numero(num1):


    numeroSt= str(num1)
    numeroFlo=float(num1)


    print("Entero",num1, type(num1),"\n")
    print("Cadena",numeroSt, type(numeroSt),"\n")
    print("Flotante",numeroFlo, type(numeroFlo))


convertir_numero(42)



