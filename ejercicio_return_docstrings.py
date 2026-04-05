def generar_mensaje(nombre,mensaje="Bienvenido al curso de Python"):

    """
    Genear mensaje.

    Argumentos
    nombre (string): nombre de una persona
    mensaje(String):parámetro con valor por defecto, "Bienvenido al curso de Python"

    Retorna:

    "¡Hola,! Bienvenido al curso de Python"


    """

    return f"Hola {nombre}, {mensaje}"

r=generar_mensaje("Ricardo")


print(r)






