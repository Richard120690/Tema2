def contar_caracteres(frase):

    longitud=len(frase)


    print(frase, "tiene", longitud, "caracteres")


contar_caracteres("La frase 'Aprender Python es divertido'")


def convertir_numero (num):

    numc=str(num)
    numf=float(num)

    print("Entero:" , num , "Tipo:",type(num))
    print("Cedena:" , numc , "Tipo:",type(numc))
    print("Flotante:" , numf , "Tipo:",type(numf))


convertir_numero(42)

